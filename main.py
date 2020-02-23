from telebot import TeleBot
from flask import Flask
app = Flask(__name__)


@app.route('/')
def shame_bot():
    bot = TeleBot("1063153614:AAER4WaltVeBUrXZAZta07R4OLCh-ZwHaKY")

    @bot.message_handler(commands=['help'])
    def fuck_off(message):
        bot.reply_to(message, "Fuck off")

    @bot.message_handler(commands=['old'])
    def zachs_old(message):
        bot.reply_to(message, "haha Zach's old")

    @bot.message_handler(commands=['willsucks'])
    def zachs_old(message):
        bot.reply_to(message, "haha Will Sucks")

    bot.polling()


if __name__ == '__main__':
    app.run()
