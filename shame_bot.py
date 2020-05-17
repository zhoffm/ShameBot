import logging
from os import environ
import telegram
from flask import Flask, request
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

@app.route('/', methods=['POST'])
def shame_bot():
    logging.info(request.args)
    logging.info(request.get_json())
    bot = telegram.Bot(token='1063153614:AAER4WaltVeBUrXZAZta07R4OLCh-ZwHaKY')
    logging.info(bot.commands)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        if '/echo' in update.message.text:
            bot.sendMessage(chat_id=chat_id, text=update.message.text)
        elif '/help' in update.message.text:
            bot.sendMessage(chat_id=chat_id, text='Fuck off!')
        elif '/old' in update.message.text:
            bot.sendMessage(chat_id=chat_id, text="haha Zach's old")
        elif '/willsucks' in update.message.text:
            bot.sendMessage(chat_id=chat_id, text="haha Will sucks!")
        elif '/rollme' in update.message.text:
            bot.sendDice(chat_id=chat_id)
        elif '/peoplescourt' in update.message.text:
            bot.sendPoll(chat_id=chat_id, question="People's court?", is_anonymous=False, open_period=600,
                         options=["People's Court!", "Not People's Court!"])
        elif '/' in update.message.text:
            bot.sendMessage(chat_id=chat_id, text=f"{update.message.text} isn't a command, dumbass")
        else:
            return "Finished!", 200
    return "Finished!", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 8080)))
