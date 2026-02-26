Scalable API Automation Framework

A production-ready, scalable API automation framework built using Python, Pytest, and Requests.

This framework supports:

Multi-environment execution (dev / qa)

Retry mechanism with exponential backoff

SLA validation (response time checks)

Parallel test execution

GitHub Actions CI integration

Structured logging

Clean modular architecture

Tech Stack

Python 3.13

Pytest

Requests

Pytest-xdist (Parallel execution)

GitHub Actions (CI/CD)

Project Structure
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
Run Tests (Environment Based)
Run in DEV
pytest -s --env dev
Run in QA
pytest -s --env qa
Run in Parallel
pytest -n auto

Uses all available CPU cores via pytest-xdist.

Retry Logic

Configurable via YAML

Supports exponential backoff

Handles transient API failures

Environment-specific retry count

Example configuration:

retry:
  max_attempts: 3
  backoff_factor: 2
SLA Validation (Response Time Check)

Supports response time validation directly from test cases.

Example:

response = api_client.get("/posts", sla_ms=1000)

Ensures the API responds within the defined SLA threshold (in milliseconds).

CI/CD Integration

This project uses GitHub Actions for automated test execution.

Workflow includes:

Triggered on every push

Installs dependencies

Runs test suite

Reports status in GitHub Actions tab

Why This Project Is Industry-Ready

Clean modular architecture

Environment configuration support

Session-based request handling

Retry with exponential backoff

Parallel execution support

CI/CD enabled

Structured logging

Future Enhancements

Allure reporting

Docker support

API mocking integration

Test data management layer

Author

Pavan Chinta
QA Automation Engineer
Python | API Testing | CI/CD