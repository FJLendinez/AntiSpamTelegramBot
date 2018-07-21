import os

from antispambot import AntiSpamBot


TOKEN = os.environ.get('ANTISPAMBOT', '')
spammers = ['tlgaren',
            'popularity gro',
            'ANY NUMBER REAL',
            'QUANTITY GUARANTEED']

AntiSpamBot(TOKEN, spammers).run()
