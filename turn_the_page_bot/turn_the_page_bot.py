import logging
import time

from turn_the_page_bot.config import Config
from turn_the_page_bot.twitter_client import TwitterClient


class TurnThePageBot:
    def __init__(self,
                 twitter=TwitterClient()) -> None:
        self.twitter = twitter
        self.config = Config()
        self.logger = logging.getLogger(__name__)
        self.lyrics = self.config.LYRICS_PATH.read_text().splitlines()
        self.lyric_length = len(self.lyrics)

    def create_description(self, line: int, page: int) -> str:
        """Creates the description to be tweeted.

        Args:
            line: line number to go into description.
            page: page number to go into description.

        Returns:
            the description
        """
        self.logger.debug("Creating description.")
        if line == 1:
            second_word = 'line'
        else:
            second_word = 'lines'
        description = f"{line} {second_word} down, {page} pages turned."
        return description

    def get_line(self) -> int:
        """Gets the line number from Twitter.

        Returns:
            the line number
        """
        self.logger.debug("Getting line.")
        line = int(self.twitter.description.split()[0])
        return line

    def get_page(self) -> int:
        """Gets the page number from Twitter.

        Returns:
            the page number
        """
        self.logger.debug("Getting page.")
        page = int(self.twitter.description.split()[3])
        return page

    def increment_line(self) -> str:
        """Gets the description from Twitter and increments the line.

        Returns:
            the new description
        """
        line = self.get_line()
        page = self.get_page()
        self.logger.debug("Incrementing line.")
        line += 1
        new_description = self.create_description(line, page)
        return new_description

    def increment_page(self) -> str:
        """Gets the description from Twitter and increments the page.

        '52 lines down. 2 pages turned.' becomes '0 lines down. 3 pages turned.'

        Returns:
              the new description
        """

        page = self.get_page()
        self.logger.debug("Incrementing page.")
        page += 1
        new_description = self.create_description(1, page)
        return new_description

    def update_description(self) -> None:
        """Updates the Twitter description.
        """
        new_description = self.increment_line()
        end_of_lyrics = self.get_line() == self.lyric_length
        if end_of_lyrics:
            self.logger.debug("End of lyrics.")
            new_description = self.increment_page()
        self.logger.debug("Updating description.")
        self.twitter.description = new_description

    def run(self) -> None:
        """Run the bot.
        """
        self.update_description()
        zero_indexed_line = self.get_line() - 1
        lyric = self.lyrics[zero_indexed_line]
        self.twitter.tweet(lyric)
        time.sleep(self.config.TWEET_INTERVAL_SECONDS)
