class CommandHandler:
    """A class defining the command handling interface.

    A CommandHandler implementing this interface must be generated by the
    CommandHandlerFactory provided to a CommandBotFactory.
    """

    def __init__(self, callback, nickname):
        """This method should store the callback and nickname as neccessary.

        Keyword arguments:
        callback -- A function which takes a target (such as a user or channel)
                    and a message. It is expected that this method will send
                    the supplied message to the supplied target.
        nickname -- The current nickname of the bot. This is necessary to be able
                    to distinguish between general messages and direct messages.
        """
	pass

    def handle(self, username, channel, message):
        """This method will be called on each message received.

	Keyword arguments:
	username -- The username of the user sending the message.
        channel -- The channel that the message was sent in.
        message -- The message which was received.
	"""
	pass
