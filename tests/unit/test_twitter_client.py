from collections import namedtuple

import pytest
from pytest_mock import MockerFixture

from turn_the_page_bot.config import Config
from turn_the_page_bot.twitter_client import TwitterClient

UpdateStatusResponse = namedtuple('UpdateStatusResponse', 'text')
GetUserResponse = namedtuple('GetUserResponse', ('id', 'description'))
UpdateProfileResponse = namedtuple('UpdateProfileResponse', 'description')


class TestTwitterClient:
    test_tweet = "test tweet"
    test_description = "test description"

    @pytest.fixture
    def mock_api(self, mocker: MockerFixture) -> None:
        def _mock_update_status(tweet: str) -> UpdateStatusResponse:
            response = UpdateStatusResponse(text=tweet)
            return response

        def _mock_update_profile(description: str) -> UpdateProfileResponse:
            response = UpdateProfileResponse(description=description)
            return response
        _api = mocker.Mock()
        _api.update_status.side_effect = _mock_update_status
        _api.update_profile.side_effect = _mock_update_profile
        mocker.patch.object(TwitterClient, "_api", _api)

    @pytest.fixture
    def mock_get_user(self, mocker: MockerFixture) -> None:
        def _mock_get_user(user_id: int) -> GetUserResponse:
            response = GetUserResponse(id=user_id, description=self.test_description)
            return response
        _api = mocker.Mock()
        _api.get_user.side_effect = _mock_get_user
        mocker.patch.object(TwitterClient, "_api", _api)

    def test_get_description_calls_get_user_correctly(self, mocker: MockerFixture, mock_get_user):
        spy = mocker.spy(TwitterClient, '_api')
        twitter = TwitterClient()
        _ = twitter.description
        spy.get_user.assert_called_once_with(user_id=Config().TWITTER_USER_ID)

    def test_tweet_calls_update_status_correctly(self, mocker: MockerFixture, mock_api):
        spy = mocker.spy(TwitterClient, '_api')
        _ = TwitterClient().tweet(self.test_tweet)
        spy.update_status.assert_called_once_with(self.test_tweet)

    def test_set_description_calls_update_profile_correctly(self, mocker: MockerFixture, mock_api):
        spy = mocker.spy(TwitterClient, '_api')
        TwitterClient().description = self.test_description
        spy.update_profile.assert_called_once_with(description=self.test_description)

    def test_description_returns_expected_response(self, mock_get_user):
        actual = TwitterClient().description
        assert actual == self.test_description

    def test_tweet_returns_expected_response(self, mock_api):
        expected = UpdateStatusResponse(text=self.test_tweet)
        actual = TwitterClient().tweet(self.test_tweet)
        assert actual == expected
