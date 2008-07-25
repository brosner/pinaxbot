
from twisted.python import log

import time
import threading
import feedparser

class FeedFetcherThread(threading.Thread):
    def __init__(self, url, protocol, interval=20):
        self.protocol = protocol
        self.url = url
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
                msg = "%s (%s)" % (entry.title, entry.link)
                entries.append(msg.encode("utf-8"))
            self.seen_entries[entry.id] = True
        if self.first_flag:
            self.first_flag = False
            # return
        for entry in entries[:1]:
            self.protocol.msg("#bosnobot", entry)

class FeedFetcher(object):
    def __init__(self, protocol):
        url = "http://code.google.com/feeds/p/django-hotclub/svnchanges/basic"
        self.feed_fetcher_thread = FeedFetcherThread(url, protocol)
        self.feed_fetcher_thread.start()
    
    def stop(self):
        self.feed_fetcher_thread.shutdown = True
        