
from twisted.internet import reactor

class QuickTest(object):
    def process_message(self, message):
        if unicode(message).startswith("PinaxBot:"):
            message.channel.msg("I am coming soon. brosner just fixed a major "
                "flaw in my messsage dispatch thread. Thank him.", True)
