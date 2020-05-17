import logging
from os import environ
import telegram
from flask import Flask, request
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


@app.route('/')
def shame_bot():
    logging.info(request.args)
    logging.info(request.data)
    logging.info(request.get_json())
    bot = telegram.Bot(token='1063153614:AAER4WaltVeBUrXZAZta07R4OLCh-ZwHaKY')
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return "Finished!", 200

    # def fuck_off(update, context):
    #     context.bot.send_message(chat_id=update.effective_chat.id, text="Fuck off")
    #
    # @bot.message_handler(commands=['old'])
    # def zachs_old(message):
    #     bot.reply_to(message, "haha Zach's old")
    #
    # @bot.message_handler(commands=['willsucks'])
    # def will_sucks(message):
    #     bot.reply_to(message, "haha Will Sucks")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 8080)))
