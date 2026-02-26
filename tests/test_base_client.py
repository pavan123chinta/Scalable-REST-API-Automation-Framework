from utils.schema_validator import SchemaValidator


def test_get_posts(api_client):
    """
    Validates:
    - API returns 200
    - Response time is within SLA
    - Response schema is valid
    """

    # SLA set to 1000 ms (1 second)
    response = api_client.get("/posts", sla_ms=1000)

    # Functional validation
    assert response.status_code == 200

    # Schema validation
    SchemaValidator.validate_schema(
        response.json(),
        "posts_schema.json"
    )