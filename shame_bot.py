import logging
from os import environ
import telegram
from flask import Flask, request
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = telegram.Bot(token='1063153614:AAER4WaltVeBUrXZAZta07R4OLCh-ZwHaKY')


@app.route('/', methods=['POST'])
def shame_bot():
    logging.info(request.get_json())
    logging.info(bot.getMyCommands())
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        if update.message:
            chat_id = update.message.chat.id
            options = {
                '/echo': {
                    'function': bot.sendMessage,
                    'params': [
                        chat_id,
                        update.message.text
                    ]
                },
                '/help': {
                    'function': bot.sendMessage,
                    'params': [
                        chat_id,
                        'lol fuck off'
                    ]
                },
                '/old': {
                    'function': bot.sendMessage,
                    'params': [
                        chat_id,
                        "haha Zach's old"
                    ]
                },
                '/willsucks': {
                    'function': bot.sendMessage,
                    'params': [
                        chat_id,
                        'haha Will sucks!'
                    ]
                },
                '/rollme': {
                    'function': bot.sendDice,
                    'params': [
                        chat_id,
                    ]
                },
                '/peoplescourt': {
                    'function': bot.sendPoll,
                    'params': [
                        chat_id,
                        "People's court?",
                        False,
                        600,
                        ["People's Court!", "Not People's Court!"]
                    ]
                },
                '/': {
                    'function': bot.sendMessage,
                    'params': [
                        chat_id,
                        f"{update.message.text} isn't a command, dumbass"
                    ]
                }
            }
            for cmd, action in options.values():
                if cmd in update.message.text:
                    function = cmd.get('function')
                    parameters = cmd.get('params')
                    function(*parameters)

    return "Finished!", 200

# BAD RUSTY OLD CODE
# if '/echo' in update.message.text:
#     bot.sendMessage(chat_id=chat_id, text=update.message.text)
# elif '/help' in update.message.text:
#     bot.sendMessage(chat_id=chat_id, text='lol fuck off')
# elif '/old' in update.message.text:
#     bot.sendMessage(chat_id=chat_id, text="haha Zach's old")
# elif '/willsucks' in update.message.text:
#     bot.sendMessage(chat_id=chat_id, text="haha Will sucks!")
# elif '/rollme' in update.message.text:
#     bot.sendDice(chat_id=chat_id)
# elif '/peoplescourt' in update.message.text:
#     bot.sendPoll(chat_id=chat_id, question="People's court?", is_anonymous=False, open_period=600,
#                  options=["People's Court!", "Not People's Court!"])
# elif '/' in update.message.text:
#     bot.sendMessage(chat_id=chat_id, text=f"{update.message.text} isn't a command, dumbass")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 8080)))
