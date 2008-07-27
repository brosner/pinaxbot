
import urllib2
import urlparse

from bosnobot.bot import IrcBot
from bosnobot.channel import Channel

from feed_fetcher import ChannelFeedFetcher

class PinaxBot(IrcBot):
    channels = [
        Channel("#django-hotclub"),
    ]
    
    def initialize(self):
        channel_pool = self.protocol.channel_pool
        self.feed_fetchers = []
        for name, url in self.get_feed_urls().items():
            self.feed_fetchers.append(
                ChannelFeedFetcher(channel_pool.get("#django-hotclub"), name, url))
    
    def shutdown(self):
        for feed_fetcher in self.feed_fetchers:
            feed_fetcher.stop()
    
    def get_feed_urls(self):
        feed_urls = {}
        urls = self.parse_svn_externals()
        for url in urls:
            parts = urlparse.urlparse(url)
            bits = parts[1].split(".")
            feed_urls[bits[0]] = "http://code.google.com/feeds/p/%s/svnchanges/basic" % bits[0]
        return feed_urls
    
    def parse_svn_externals(self):
        urls = []
        raw_data = urllib2.urlopen("http://django-hotclub.googlecode.com/svn/trunk/apps/svn.externals").read()
        for line in raw_data.split("\n"):
            if line:
                bits = line.split()
                if not bits[0].startswith("#"):
                    urls.append(bits[-1])
        return urls
