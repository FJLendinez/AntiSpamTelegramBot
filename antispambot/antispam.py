import telebot


class AntiSpamBot:

    def __init__(self, token, spammers):
        bot = telebot.AsyncTeleBot(token)

        @bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
        def on_user_joins(message):

            name = message.new_chat_participant.first_name
            if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
                name += " {}".format(message.new_chat_participant.last_name)

            if spammers in name:
                bot.delete_message(message.chat.id, message.id)
                bot.kick_chat_member(message.chat.id, message.new_chat_participant.id)
        self.bot = bot

    def run(self):
        self.bot.polling()