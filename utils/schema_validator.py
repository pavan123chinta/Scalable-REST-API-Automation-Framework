import json
import os
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class SchemaValidator:
    """
    Validates API responses against JSON schemas.
    """

    @staticmethod
    def validate_schema(response_data, schema_name: str):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        schema_path = os.path.join(base_dir, "schemas", schema_name)

        with open(schema_path, "r") as schema_file:
            schema = json.load(schema_file)

        try:
            validate(instance=response_data, schema=schema)
        except ValidationError as e:
            raise AssertionError(f"Schema validation failed: {e.message}")