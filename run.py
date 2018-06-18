import os

from .antispambot import AntiSpamBot


TOKEN = os.environ.get('ANTISPAMBOT', '')
spammers = ['tlgaren']

AntiSpamBot(TOKEN, spammers)