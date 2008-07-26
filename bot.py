
from bosnobot.bot import IrcBot
from bosnobot.channel import Channel

from feed_fetcher import ChannelFeedFetcher

class PinaxBot(IrcBot):
    channels = [
        Channel("#django-hotclub"),
    ]
    
    feed_urls = {
        "pinax": "http://code.google.com/feeds/p/django-hotclub/svnchanges/basic",
        "django-bookmarks": "http://code.google.com/feeds/p/django-bookmarks/svnchanges/basic",
        "django-email-confirmation": "http://code.google.com/feeds/p/django-email-confirmation/svnchanges/basic",
        "django-command-extensions": "http://code.google.com/feeds/p/django-command-extensions/svnchanges/basic",
        "django-robots": "http://code.google.com/feeds/p/django-robots/svnchanges/basic",
        "django-databasetemplateloader": "http://code.google.com/feeds/p/django-databasetemplateloader/svnchanges/basic",
        "django-friends": "http://code.google.com/feeds/p/django-friends/svnchanges/basic",
        "django-notification": "http://code.google.com/feeds/p/django-notification/svnchanges/basic",
        "django-mailer": "http://code.google.com/feeds/p/django-mailer/svnchanges/basic",
        "django-messages": "http://code.google.com/feeds/p/django-messages/svnchanges/basic",
        "django-announcements": "http://code.google.com/feeds/p/django-announcements/svnchanges/basic",
        "django-logging": "http://code.google.com/feeds/p/django-logging/svnchanges/basic",
        "django-oembed": "http://code.google.com/feeds/p/django-oembed/svnchanges/basic",
        "django-pagination": "http://code.google.com/feeds/p/django-pagination/svnchanges/basic",
        "django-threadedcomments": "http://code.google.com/feeds/p/django-threadedcomments/svnchanges/basic",
        "django-wikiapp": "http://code.google.com/feeds/p/django-wikiapp/svnchanges/basic",
        "django-timezones": "http://code.google.com/feeds/p/django-timezones/svnchanges/basic",
        "django-feedutil": "http://code.google.com/feeds/p/django-feedutil/svnchanges/basic",
        "django-app-plugins": "http://code.google.com/feeds/p/django-app-plugins/svnchanges/basic",
        "django-voting": "http://code.google.com/feeds/p/django-voting/svnchanges/basic",
        "django-tagging": "http://code.google.com/feeds/p/django-tagging/svnchanges/basic",
        "django-gravatar": "http://code.google.com/feeds/p/django-gravatar/svnchanges/basic",
        "django-ajax-validation": "http://code.google.com/feeds/p/django-ajax-validator/svnchanges/basic",
        "django-crashlog": "http://code.google.com/feeds/p/django-crashlog/svnchanges/basic",
        "django-photologue": "http://code.google.com/feeds/p/django-photologue/svnchanges/basic",
    }
    
    def initialize(self):
        channel_pool = self.protocol.channel_pool
        self.feed_fetchers = []
        for name, url in self.feed_urls.items():
            self.feed_fetchers.append(
                ChannelFeedFetcher(channel_pool.get("#bosnobot"), name, url))
    
    def shutdown(self):
        for feed_fetcher in self.feed_fetchers:
            feed_fetcher.stop()
