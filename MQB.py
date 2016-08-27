from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Methods handling commands

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="I'm a bot, please talk to me!")

def hello(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Hello {}'.format(update.message.from_user.first_name))

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

def icebreaker(bot, update):
    bot.sendPhoto(update.message.chat_id, photo='http://67.media.tumblr.com/19ac78e1747fe210c164aa12882bbc35/tumblr_nd23pns3Z41rx3q30o1_500.gif')

def silence(bot, update):
    bot.sendPhoto(update.message.chat_id, photo='http://67.media.tumblr.com/05ab4de70d2195e3ba0b2338eca31005/tumblr_o0on44BT1l1uhipc8o1_1280.jpg')

def idontcare(bot, update):
    bot.sendPhoto(update.message.chat_id, photo='http://67.media.tumblr.com/4174671f266454da747190b386a265f6/tumblr_ockh8oJJaC1vewk1qo1_1280.jpg')




# Helpers

echo_handler = MessageHandler([Filters.text], echo)
caps_handler = CommandHandler('caps', caps, pass_args=True)

updater = Updater('221355228:AAEaNilNWb1_P32QSEXhovNVJTzO8aZX-4g')


# For quicker access to the Dispatcher used by your Updater
dispatcher = updater.dispatcher

# Register the methods handling commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(CommandHandler('icebreaker', icebreaker))
dispatcher.add_handler(CommandHandler('idontcare', idontcare))
dispatcher.add_handler(CommandHandler('silence', silence))

updater.start_polling()
