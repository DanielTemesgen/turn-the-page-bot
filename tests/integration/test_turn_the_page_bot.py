from typing import List

import pytest
from pytest_mock import MockerFixture

from tests.integration.mocks.mock_twitter_client import MockTwitterClient
from tests.test_config import TestConfig
from turn_the_page_bot.config import Config
from turn_the_page_bot.turn_the_page_bot import TurnThePageBot

config = TestConfig()


class TestIntegrationTurnThePageBot:

    @pytest.fixture
    def mock_bot(self, tmp_path) -> TurnThePageBot:
        tmp_path = tmp_path.joinpath("test_run_data.txt")
        bot = TurnThePageBot(twitter=MockTwitterClient(tmp_path))
        return bot

    @pytest.fixture
    def mock_config(self, mocker: MockerFixture) -> None:
        mocker.patch.object(Config, "TWEET_INTERVAL_SECONDS", 0.01)

    @pytest.fixture
    def expected(self) -> List[str]:
        return config.INTEGRATION_RESOURCES_DIR.joinpath("test_data_200_iterations.txt").read_text()

    def test_run_200_iterations(self, mock_config, mock_bot, expected):
        for _ in range(200):
            mock_bot.run()
        actual = mock_bot.twitter.path.read_text()
        assert actual == expected
