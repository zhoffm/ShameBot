from telebot import TeleBot
import logging
logging.basicConfig(level=logging.DEBUG)

bot = TeleBot("1063153614:AAER4WaltVeBUrXZAZta07R4OLCh-ZwHaKY")


@bot.message_handler(commands=['help'])
def fuck_off(message):
    bot.reply_to(message, "Fuck off")


@bot.message_handler(commands=['old'])
def zachs_old(message):
    bot.reply_to(message, "haha Zach's old")


@bot.message_handler(commands=['willsucks'])
def will_sucks(message):
    bot.reply_to(message, "Will sucks!")

# @bot.message_handler(commands=['PeoplesCourt'])
# def peoples_court(message):
#     total_group_memebers = bot.get_chat_members_count(-355911031) - 1
#     bot.send_poll()


if __name__ == '__main__':
    bot.polling()
