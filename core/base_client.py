import time
import requests
from utils.config_loader import ConfigLoader
from core.logger import setup_logger


class BaseClient:
    def __init__(self, environment: str):
        self.config = ConfigLoader(environment)
        self.logger = setup_logger()

        self.base_url = self.config.get("base_url")
        self.timeout = self.config.get("timeout", 10)
        self.headers = self.config.get("headers", {})

        # Retry configuration
        self.max_attempts = self.config.get_nested("retry", "max_attempts") or 1
        self.backoff_factor = self.config.get_nested("retry", "backoff_factor") or 1

        # 🔥 NEW: Session object (connection pooling)
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _make_request(self, method, endpoint, sla_ms=None, **kwargs):
        url = endpoint if endpoint.startswith("http") else f"{self.base_url}{endpoint}"

        attempt = 0
        while attempt < self.max_attempts:
            try:
                self.logger.info(f"Sending {method} request to: {url}")

                start_time = time.time()

                response = self.session.request(
                    method=method,
                    url=url,
                    timeout=self.timeout,
                    **kwargs
                )

                response_time = (time.time() - start_time) * 1000

                self.logger.info(
                    f"Received response | Status Code: {response.status_code} | "
                    f"Response Time: {response_time:.2f} ms"
                )

                # SLA validation
                if sla_ms and response_time > sla_ms:
                    raise Exception(
                        f"SLA Breached: Response time {response_time:.2f} ms "
                        f"exceeded {sla_ms} ms"
                    )

                return response

            except Exception as e:
                attempt += 1

                if attempt >= self.max_attempts:
                    self.logger.error(f"Max retry attempts reached ({self.max_attempts}).")
                    raise

                wait_time = self.backoff_factor * (2 ** (attempt - 1))
                self.logger.warning(
                    f"Retry attempt {attempt}/{self.max_attempts} after error: {e}. "
                    f"Waiting {wait_time} seconds..."
                )
                time.sleep(wait_time)

    def get(self, endpoint, **kwargs):
        return self._make_request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._make_request("POST", endpoint, **kwargs)

    def close(self):
        """Cleanly close session"""
        self.session.close()