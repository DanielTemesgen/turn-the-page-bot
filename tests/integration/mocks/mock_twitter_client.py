import logging
from pathlib import Path
from typing import List

from turn_the_page_bot.config import Config


class MockTwitterClient:
    def __init__(self, path: Path) -> None:
        self.config = Config()
        self.logger = logging.getLogger(__name__)
        self.path = path
        self.description_prefix = "Description: "
        self.tweet_prefix = "Tweet: "
        self.path.write_text(self.description_prefix + "0 lines down, 0 pages turned.\n")

    @property
    def description(self) -> str:
        reversed_log: List[str] = self.path.read_text().splitlines()[::-1]
        for line in reversed_log:
            if line.startswith(self.description_prefix):
                return line.lstrip(self.description_prefix)

    @description.setter
    def description(self, description: str) -> None:
        with self.path.open(mode="a") as f:
            f.write(self.description_prefix + description + '\n')

    def tweet(self, tweet: str) -> None:
        with self.path.open(mode="a") as f:
            f.write(self.tweet_prefix + tweet + '\n')
