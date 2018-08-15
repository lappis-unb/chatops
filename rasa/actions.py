import json
import requests
from rasa_core.actions import Action
from rasa_core.events import SlotSet
API_URL = "https://api.github.com/repos/gabibguedes/teste/issues"
URL = "https://github.com/gabibguedes/teste"

class ActionListIssues():
	def name(self):
		return "action_list_issues"

	def run(self, dispatcher, tracker, domain):
		response = requests.get(API_URL)

		api_list = response.json()

		message = 'Open issues on ' + URL + ':\n'
		for issue in api_list:
			message += '#' + str(issue['number'])+ " " + issue['title'] + '\n'

		print message
		dispatcher.utter_message(message)

class ActionCreateIssues():
	def name(self):
		return 'action_create_issue'

	def run(self, dispatcher, tracker, domain):
		issue = {'title': 'Bot Issue (created on telegram)', 'body': 'hello github'}

		response = requests.post(API_URL,
		headers = {'Authorization': 'token [PLACE HERE YOUR GITHUB TOKEN]'},
		data = json.dumps(issue))
		message = 'New Issue Created \n' + '#'+ str(response.json()["number"]) + ' ' + response.json()["title"] + '\n' + response.json()["body"] + '\n' + response.json()["html_url"]

		print message
		dispatcher.utter_message(message)
