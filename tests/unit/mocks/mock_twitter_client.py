from collections import namedtuple


class MockTwitterClient:
    def __init__(self, description_return_value):
        self.description_return_value = description_return_value

    @property
    def description(self):
        return self.description_return_value

    @staticmethod
    def tweet(tweet: str):
        Response = namedtuple('Response', 'text')
        response = Response(text=tweet)
        return response
