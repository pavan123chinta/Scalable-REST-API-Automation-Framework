import yaml
import os


class ConfigLoader:
    """
    Loads YAML configuration files dynamically
    based on selected environment.
    """

    def __init__(self, environment: str):
        config_path = os.path.join("config", f"{environment}.yaml")

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def get_nested(self, key1, key2, default=None):
        """
        Safely fetch nested config values.
        Example: retry -> max_attempts
        """
        return self.config.get(key1, {}).get(key2, default)