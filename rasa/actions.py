import json
import requests
import time
from rasa_core.actions import Action
from rasa_core.events import SlotSet
from rocketchat_py_sdk.driver import Driver

bot_username = 'rouana'
bot_password = 'rouana'
rocket_url = 'localhost:3000'
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
	return message

class ActionTaisOn():

	def name(self):
		return "action_tais_on"

	def run(self, dispatcher, tracker, domain):
		tais = My_bot()
		tais.hello = 'Ola meu nome e Tais'
		message = start(Driver(url=rocket_url, ssl=False, debug=True), tais)

		dispatcher.utter_message(message)
