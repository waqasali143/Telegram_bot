
from telegram import Bot, Update

import telegram.ext

from telegram.ext import Updater, CommandHandler


API_TOKEN = ('Enter The Telegram Token')


def start(update, context):
        update.message.reply_text("Hello Wellcome Message")

# similarly difine the different function according to needs
def help(update, context):
    update.message.reply_text(
        """
        PIAIC
        /Course 
        /contact
        /ImportantLinks
        """)
          
    #===========================================================
def contact(update, context):
    update.message.reply_text(
        """
       PIAIC HELP LINE 
       03082220203
        """)
def ImportantLinks(update, context):
    update.message.reply_text(
        """
        PIAIC
       /FaceBook
       /Website
        """)
def FaceBook(update, context):
    update.message.reply_text(
        """
        PIAIC
        https://rb.gy/oji0g
        https://shorturl.at/dkpU5
        """)
#==============================================================================
                        #Message Handle

def handle_message(update, context):
        update.message.reply_text(f"""
        Wrong Command=> {update.message.text}\n
        Select the command from it
        /help
        """)


updater = telegram.ext.Updater(API_TOKEN, use_context = True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', start))
dispatch.add_handler(telegram.ext.CommandHandler('help', help))

dispatch.add_handler(telegram.ext.CommandHandler('contact', contact))

# Any Message Handle
dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))


updater.start_polling()
updater.idle()

