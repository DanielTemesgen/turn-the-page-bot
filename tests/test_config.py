from pathlib import Path


class TestConfig:
    RESOURCES_DIR = Path(__file__).parent.joinpath('resources')
    INTEGRATION_RESOURCES_DIR = RESOURCES_DIR.joinpath('integration')
