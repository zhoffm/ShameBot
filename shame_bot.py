import logging
from os import environ

from telegram import Update, Bot
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters

from flask import Flask, request
app = Flask(__name__)

TOKEN = '1063153614:AAER4WaltVeBUrXZAZta07R4OLCh-ZwHaKY'
bot = Bot(token=TOKEN)
updater = Updater(bot=bot, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

shamebot_logs_url = 'https://console.cloud.google.com/run/detail/us-central1/telegram-shame-bot/logs?project=telegram-shame-bot-277421'


@app.post('/')
def shame_bot():
    logging.info(request.get_json())
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "Finished!", 200


def do_echo(update: Update, context: CallbackContext):
    entities = update.message.parse_entities(types=['bot_command'])
    for entity, entity_text in entities.items():
        stripped_text = update.message.text.lstrip(entity_text).strip()
        context.bot.send_message(chat_id=update.effective_chat.id, text=stripped_text)


def do_help(update: Update, context: CallbackContext):
    context.bot.sendMessage(update.effective_chat.id, text='lol fuck off')


def do_old(update: Update, context: CallbackContext):
    context.bot.sendMessage(update.effective_chat.id, text="haha Zach's old")


def do_willsucks(update: Update, context: CallbackContext):
    context.bot.sendMessage(update.effective_chat.id, text="haha Will sucks")


def do_rollme(update: Update, context: CallbackContext):
    context.bot.sendDice(update.effective_chat.id)


def do_peoplescourt(update: Update, context: CallbackContext):
    context.bot.sendPoll(update.effective_chat.id, question="People's court?", is_anonymous=False, open_period=600,
                    options=["People's Court!", "Not People's Court!"])


def do_yipos(update: Update, context: CallbackContext):
    entities = update.message.parse_entities(types=['mention'])
    if entities:
        for entity, entity_text in entities.items():
            context.bot.sendMessage(update.effective_chat.id, text=f"{entity_text}, you inflammatory piece of shit")
    else:
        context.bot.sendMessage(update.effective_chat.id, text=f"you inflammatory piece of shit")


def do_hammyspammy(update: Update, context: CallbackContext):
    hammy_spammy_photo_url = 'https://storage.googleapis.com/telegram-shame-bot-staticfiles/nathansdumbhammyspammy.jpg'
    caption = "Here's your rat, you animal"
    context.bot.sendPhoto(update.effective_chat.id, hammy_spammy_photo_url, caption=caption)


def handle_empty_command(update: Update, context: CallbackContext):
    entities = update.message.parse_entities(types=['bot_command'])
    for entity, entity_text in entities.items():
        context.bot.sendMessage(update.effective_chat.id, text=f"{entity_text} isn't a command, dumbass!")


dispatcher.add_handler(CommandHandler('help', do_help))
dispatcher.add_handler(CommandHandler('echo', do_echo))
dispatcher.add_handler(CommandHandler('old', do_old))
dispatcher.add_handler(CommandHandler('willsucks', do_willsucks))
dispatcher.add_handler(CommandHandler('rollme', do_rollme))
dispatcher.add_handler(CommandHandler('peoplescourt', do_peoplescourt))
dispatcher.add_handler(CommandHandler('yipos', do_yipos))
dispatcher.add_handler(CommandHandler('hammyspammy', do_hammyspammy))
dispatcher.add_handler(CommandHandler('spammyhammy', do_hammyspammy))
dispatcher.add_handler(MessageHandler(Filters.command, handle_empty_command))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 8080)))
    # updater.start_polling()
