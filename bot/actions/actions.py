import json
import requests
import time
import os

from rasa_core_sdk import Action
from rasa_core.events import SlotSet
from rocketchat_py_sdk.driver import Driver

bot_username = os.getenv('BOT_USERNAME', 'bot')
bot_password = os.getenv('BOT_PASSWORD', 'bot')
rocket_url = os.getenv('BOT_URL', 'localhost:3000')
use_ssl = False
if 'True' in os.getenv('BOT_SSL', 'True'):
    use_ssl = True

header = None

class My_bot(object):
    hello = ''
    is_online = False
    livechat_data = None

def verify_logged(bot, tais):

    def get_data(error, data):
        if error:
            print((50*'=') + ' ERRO ' + (50 * '='))
            return
        tais.livechat_data = data
        tais.is_online = data['online']

    bot.call('livechat:getInitialData',[bot._login_token], get_data)

def start(bot, tais):
    try:
        bot.connect()
        bot.login(user=bot_username, password=bot_password)
        bot.subscribe_to_messages()
        verify_logged(bot, tais)
        time.sleep(1)
        print('----------> Tais logou?')
        print('----------> ' +str(tais.is_online))
        print(tais.livechat_data)
        if tais.is_online:
            message = 'Tais esta online'
        else:
            message = 'Tais esta offline'
    except ConnectionRefusedError:
            message = 'Desculpe, não consegui me conectar =/'

    return message

class ActionTaisOn(Action):

    def name(self):
        return 'action_tais_on'

    def run(self, dispatcher, tracker, domain):
        tais = My_bot()
        tais.hello = 'Ola meu nome e Tais'
        message = start(Driver(url=rocket_url, ssl=use_ssl, debug=True), tais)

        dispatcher.utter_message(message)
