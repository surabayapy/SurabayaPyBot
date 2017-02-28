'''
    SurabayaPyBot
    oleh Tegar Imansyah
    ---------------------------------------
    Bot ini berfungsi untuk sistem informasi komunitas Surabaya.py
    Kamu bisa mengetahui kegiatan kami selanjutnya, mendaftar kegiatan itu, 
    notulen kuliah tamu, kenalan dengan anggota lain dan sebagainya.

    Menggunakan library python-telegram-bot
'''

from rahasia import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

def baru(bot, update):
    update.message.reply_text(''' 
Selamat datang di Bot Surabaya.py

Bot ini bisa menyapamu, memberi tau dan mengingatkan kegiatan kami selanjutnya, mendaftar kegiatan atau kenalan ke sesama pengguna Python di Surabaya.
Jangan lupa untuk gabung di grup telegram kita: t.me/surabayadotpy , Enjoy
            ''')
    update.message.reply_text('Ada yang bisa saya bantu?')

def sapa(bot, update):
	update.message.reply_text('Hai %s, ada yang bisa saya bantu?' % update['message']['chat']['first_name'])

def kegiatan(bot, update):
	update.message.reply_text('Kami lagi ada di Surabaya Developer Day 2017')

def daftar(bot, update):
	update.message.reply_text('Selamat datang %s, anda telah terdaftar!' % update['message']['chat']['first_name'])

def baca(bot, update):
	switcher = {
        'hai': sapa,
        'kegiatan': kegiatan,
        'daftar': daftar
    }

    # Get the function from switcher dictionary
	for i in switcher.keys():
		if i in update['message']['text'].lower():
			execfunc = switcher.get(i)
			execfunc(bot, update)
			break


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler('start', baru))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, baca))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

''' Update chat

{'message': 
	{'migrate_to_chat_id': 0,
	 'delete_chat_photo': False,
	 'new_chat_photo': [],
	 'entities': [],
	 'text': u'hai',
	 'migrate_from_chat_id': 0,
	 'channel_chat_created': False,
	 'from': {
	 	'username': u'TegarImansyah',
		 'first_name': u'Tegar',
		 'last_name': u'Imansyah',
		 'type': '',
		 'id': 130727531
	 },
	 'supergroup_chat_created': False,
	 'chat': {
	 	'username': u'TegarImansyah',
		'first_name': u'Tegar',
		'all_members_are_admins': False,
		'title': '',
		'last_name': u'Imansyah',
		'type': u'private',
		'id': 130727531
	 },
	 'photo': [],
	 'date': 1488090821,
	 'group_chat_created': False,
	 'caption': '',
	 'message_id': 224,
	 'new_chat_title': ''
	 },
 'update_id': 834960664
 }
'''