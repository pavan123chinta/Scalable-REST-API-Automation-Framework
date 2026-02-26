import time
from core.logger import setup_logger


class RetryHandler:
    """
    Handles retry logic with exponential backoff.
    """

    def __init__(self, max_attempts: int, backoff_factor: int):
        self.max_attempts = max_attempts
        self.backoff_factor = backoff_factor
        self.logger = setup_logger()

    def execute(self, func, *args, **kwargs):
        """
        Executes a function with retry logic.
        Retries only for server-side errors (500–599).
        """

        attempt = 0

        while attempt < self.max_attempts:
            try:
                response = func(*args, **kwargs)

                # Retry only for server errors
                if 500 <= response.status_code < 600:
                    raise Exception(f"Server error: {response.status_code}")

                return response

            except Exception as e:
                attempt += 1

                if attempt >= self.max_attempts:
                    self.logger.error(
                        f"Max retry attempts reached ({self.max_attempts})."
                    )
                    raise

                wait_time = self.backoff_factor ** attempt

                self.logger.warning(
                    f"Retry attempt {attempt}/{self.max_attempts} "
                    f"after error: {e}. Waiting {wait_time} seconds..."
                )

                time.sleep(wait_time)