import json
import requests
from rasa_core.actions import Action
from rasa_core.events import SlotSet

class ActionListIssues():
	def name(self):
		return "action_list_issues"

	def run(self, dispatcher, tracker, domain):
		response = requests.get("https://api.github.com/repos/lappis-unb/EcossistemasSWLivre/issues")

		api_list = response.json()

		message = ''
		for issue in api_list:
			message += str(issue['number'])+" - " + issue['title'] + '\n'

		print message
		dispatcher.utter_message(message)
		
		return [SlotSet("issues", message)]

