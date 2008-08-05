
from twisted.python import log

import time
import threading
import feedparser

class FeedFetcherThread(threading.Thread):
    def __init__(self, name, url, channel, interval=60):
        self.name = name
        self.url = url
        self.channel = channel
        self.interval = interval
        self.shutdown = False
        self.seen_entries = {}
        self.first_flag = True
        super(FeedFetcherThread, self).__init__()
    
    def run(self):
        counter = 0
        while not self.shutdown:
            if self.interval == counter:
                counter = 0
                self.fetch()
            else:
                counter += 1
            time.sleep(1)
    
    def fetch(self):
        feed = feedparser.parse(self.url)
        entries = []
        for entry in feed.entries:
            if entry.id not in self.seen_entries:
                msg = "[%s] %s - %s - %s" % (self.name, entry.author, entry.title, entry.link)
                msg = msg.replace("\n", " ")
                entries.append(msg.encode("utf-8"))
            self.seen_entries[entry.id] = True
        if self.first_flag:
            self.first_flag = False
            return
        for entry in entries[:5]:
            self.channel.msg(entry, True)

class ChannelFeedFetcher(object):
    def __init__(self, channel, name, url):
        self.feed_fetcher_thread = FeedFetcherThread(name, url, channel)
        log.msg("Starting thread for %s [%s]" % (name, url))
        self.feed_fetcher_thread.start()
    
    def stop(self):
        self.feed_fetcher_thread.shutdown = True
        