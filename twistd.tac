
from twisted.application import service
from bosnobot import IrcBotService

application = service.Application("pinaxbot")
ircbot = IrcBotService()
ircbot.setServiceParent(application)
