# Scalable REST API Automation Framework

Production-ready REST API automation framework built using Python, Pytest, and Requests.

## Features

- Multi-environment execution (DEV / QA)
- Retry mechanism with exponential backoff
- SLA validation (response time checks)
- Parallel test execution
- GitHub Actions CI integration
- Structured logging
- Modular and reusable framework architecture

---

## Tech Stack

- Python 3
- Pytest
- Requests
- Pytest-xdist
- GitHub Actions

---

## Project Structure

```bash
scalable_api_automation_framework/

├── clients/
├── config/
│   ├── dev.yaml
│   └── qa.yaml
├── core/
│   ├── base_client.py
│   ├── retry_handler.py
│   ├── auth_manager.py
│   └── logger.py
├── schemas/
├── tests/
├── utils/
├── .github/workflows/api-tests.yml
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

## Running Tests

### Run in DEV Environment

```bash
pytest -s --env dev
```

### Run in QA Environment

```bash
pytest -s --env qa
```

### Run Tests in Parallel

```bash
pytest -n auto
```

Uses `pytest-xdist` for parallel execution.

---

## Retry Logic

- Configurable through YAML
- Supports exponential backoff
- Handles transient API failures
- Environment-specific retry configuration

Example:

```yaml
retry:
  max_attempts: 3
  backoff_factor: 2
```

---

## SLA Validation

Supports response-time validation directly in test cases.

Example:

```python
response = api_client.get("/posts", sla_ms=1000)
```

Ensures APIs respond within defined SLA thresholds.

---

## CI/CD Integration

GitHub Actions workflow includes:

- Automatic execution on push
- Dependency installation
- Test execution
- CI status reporting

---

## Industry-Level Concepts Used

- Modular framework design
- Environment-based configuration
- Session management
- Retry handling
- Parallel execution
- CI/CD workflow integration
- Structured logging

---

## Future Enhancements

- Allure Reporting
- Docker Integration
- API Mocking
- Test Data Management Layer

---

## Author

**Pavan Chinta**  
QA Automation Engineer | Python | API Testing | CI/CD
