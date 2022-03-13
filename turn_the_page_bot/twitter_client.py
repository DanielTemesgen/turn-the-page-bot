import functools
import logging
import os

import tweepy

from turn_the_page_bot.config import Config


class TwitterClient:

    def __init__(self) -> None:
        self.config = Config()
        self.logger = logging.getLogger(__name__)

    @functools.cached_property
    def _api(self) -> tweepy.API:
        auth = tweepy.OAuth1UserHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
        auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
        return tweepy.API(auth)

    @property
    def description(self) -> str:
        """Gets the Twitter description.

        Returns:
            the description
        """
        self.logger.debug("Getting description.")
        description = self._api.get_user(user_id=self.config.TWITTER_USER_ID).description
        return description

    @description.setter
    def description(self, description: str) -> None:
        """Sets the Twitter description.

        Args:
            description: the description to be updated.

        Returns:
            the API response
        """
        self._api.update_profile(description=description)

    def tweet(self, tweet: str) -> str:
        """Tweet a line.

        Args:
            tweet: the string to be tweeted.

        Returns:
            the API response
        """
        return self._api.update_status(tweet)
