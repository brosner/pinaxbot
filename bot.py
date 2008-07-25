
from bosnobot.bot import IrcBot

from feed_fetcher import FeedFetcher

class PinaxBot(IrcBot):
    def initialize(self):
        self.feed_fetcher = FeedFetcher(self.protocol)
    
    def shutdown(self):
        self.feed_fetcher.stop()
