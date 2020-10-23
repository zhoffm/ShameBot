import logging
from os import environ
import telegram
from telegram.botcommand import BotCommand
from flask import Flask, request
app = Flask(__name__)

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

shamebot_logs_url = 'https://console.cloud.google.com/run/detail/us-central1/telegram-shame-bot/logs?project=telegram-shame-bot-277421'


@app.route('/', methods=['POST'])
def shame_bot():
    bot = telegram.Bot(token='1063153614:AAER4WaltVeBUrXZAZta07R4OLCh-ZwHaKY')
    logging.info(request.get_json())
    logging.info(bot.getMyCommands())
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        logging.info(update)
        message = update.message
        if message:
            handle_commands(message, bot)
    return "Finished!", 200


def handle_commands(message, bot):
    chat_id = message.chat.id
    from_user = message.from_user
    mentions = message.parse_entities(['mention'])
    mention_entity_list = list(mentions)

    def do_echo():
        bot.sendMessage(chat_id, text=message.text)

    def do_help():
        bot.sendMessage(chat_id, text='lol fuck off'),

    def do_willsucks():
        bot.sendMessage(chat_id, text="haha Zach's old")

    def do_rollme():
        bot.sendDice(chat_id)

    def do_peoplescourt():
        bot.sendPoll(chat_id, question="People's court?", is_anonymous=False, open_period=600,
                     options=["People's Court!", "Not People's Court!"])

    def do_yipos():
        bot.sendMessage(chat_id, text=f"you inflammatory piece of shit")

    def handle_empty_command():
        bot.sendMessage(chat_id, text=f"{message.text} isn't a command, dumbass!")

    def debug():
        if from_user.username == 'zhoffm':
            logging.info(message)
            logging.info(f'Chat ID: {chat_id}')
            logging.info(f'From User: {from_user}')
            logging.info(f'Mentions: {mentions}')
            logging.debug(mentions)
            bot.sendMessage(chat_id, text=f"Papa! I've put my logs here: {shamebot_logs_url}")
        else:
            bot.sendMessage(chat_id, text=f"How dare you?! You're not my dad!")

    dispatch = {
        'debug': debug,
        'echo': do_echo,
        'help': do_help,
        'old': do_willsucks,
        'willsucks': do_willsucks,
        'rollme': do_rollme,
        'peoplescourt': do_peoplescourt,
        'yipos': do_yipos,
        '': handle_empty_command
    }

    for command in dispatch:
        if f'/{command}' in message.text:
            dispatch[command]()
            return


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 8080)))