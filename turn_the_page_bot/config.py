from pathlib import Path


class Config:
    TWITTER_USER_ID = 1025844712794718209
    TWEET_INTERVAL_SECONDS = 3 * 60 * 60
    LYRICS_PATH = Path(__file__).parents[1].joinpath("resources", "lyrics.txt")
