from typing import Callable

import pytest

from tests.unit.mocks.mock_twitter_client import MockTwitterClient
from turn_the_page_bot.turn_the_page_bot import TurnThePageBot


class TestTurnThePageBot:
    @pytest.fixture
    def mock_bot(self, tmp_path) -> Callable:
        def _mock_bot(description_return_value):
            bot = TurnThePageBot(twitter=MockTwitterClient(description_return_value))
            return bot

        return _mock_bot

    def test_get_line_returns_correct_line(self, mock_bot):
        expected = 0
        bot = mock_bot(description_return_value='0 lines down, 219 pages turned.')
        actual = bot.get_line()
        assert actual == expected

    def test_get_page_returns_correct_page(self, mock_bot):
        expected = 219
        bot = mock_bot(description_return_value='0 lines down, 219 pages turned.')
        actual = bot.get_page()
        assert actual == expected

    @pytest.mark.parametrize("description, expected",
                             [('0 lines down, 219 pages turned.', '1 line down, 219 pages turned.'),
                              ('1 line down, 219 pages turned.', '2 lines down, 219 pages turned.'),
                              ('2 lines down, 219 pages turned.', '3 lines down, 219 pages turned.')],
                             ids=['0 lines to 1 line', '1 line to 2 lines', '2 lines to 3 lines'])
    def test_increment_line_returns_correct_description(self, mock_bot, description, expected):
        bot = mock_bot(description_return_value=description)
        actual = bot.increment_line()
        assert actual == expected

    def test_increment_page_returns_correct_description(self, mock_bot):
        expected = "1 line down, 220 pages turned."
        bot = mock_bot(description_return_value='52 lines down, 219 pages turned.')
        actual = bot.increment_page()
        assert actual == expected

