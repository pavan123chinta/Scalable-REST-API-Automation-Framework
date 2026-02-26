from utils.config_loader import ConfigLoader


def test_load_config():
    config = ConfigLoader("dev")

    assert config.get("environment") == "dev"
    assert config.get("base_url") is not None
    assert config.get_nested("retry", "max_attempts") == 3