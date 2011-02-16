import re

from CommandHandler import CommandHandler

class ExampleCommandHandler(CommandHandler):
    def __init__(self, callback, nickname):
        self.callback = callback
        self.direct_prefix = nickname + ":"

    def handle(self, user, channel, message):

        if message.startswith(self.direct_prefix):
            message = message[len(self.direct_prefix):].lstrip()

            self.handleDictionary(self.directCommandDictionary(), user, channel, message)
        else:
            self.handleDictionary(self.globalCommandDictionary(), user, channel, message)

    def handleDictionary(self, dictionary, user, channel, message):
        for pattern, handler in dictionary.items():
            if re.match(pattern, message):
                self.processActions(handler(user, channel, message))        

    def processActions(self, actions):
        if isinstance(actions, list):
            for action in actions:
                self.processAction(action)
        else:
            self.processAction(actions)

    def processAction(self, action):
        target = action.get("target")
        if isinstance(action.get("message"), list):
            for message in action.get("message"):
                self.callback(action.get("target"), message)
        else:
            self.callback(action.get("target"), action.get("message"))

    def globalCommandDictionary(self):
        return {"help$": self.help}

    def directCommandDictionary(self):
        return {"help": self.help}

    def help(self, user, channel, input):
        message = ["Available commands:","  help - display this message"]
        return {"target": user, "message": message}