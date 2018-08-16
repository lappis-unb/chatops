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
		print '==============================='
		print tracker.current_slot_values()
		print '==============================='
		name = tracker.current_slot_values()['issue_name']
		body = tracker.current_slot_values()['issue_body']
		issue = {'title': name, 'body': body}

		response = requests.post(API_URL,
		headers = {'Authorization': 'token [PLACE HERE YOUR GITHUB TOKEN]'},
		data = json.dumps(issue))
		message = 'New Issue Created \n' + '#'+ str(response.json()["number"]) + ' ' + response.json()["title"] + '\n' + response.json()["body"] + '\n' + response.json()["html_url"]

		print message
		dispatcher.utter_message(message)

class ActionSetIssueName():
	def name(self):
		return 'action_set_issue_name'

	def run(self, dispatcher, tracker, domain):
		issue_name = tracker.latest_message.text

		if issue_name.startswith('/name '):
			issue_name = issue_name[6:]
		elif issue_name.startswith('/name'):
			issue_name = issue_name[5:]

		return [SlotSet("issue_name", issue_name)]


class ActionSetIssueBody():
	def name(self):
		return 'action_set_issue_body'

	def run(self, dispatcher, tracker, domain):
		issue_body = tracker.latest_message.text

		if issue_body.startswith('/body '):
			issue_body = issue_body[6:]
		elif issue_body.startswith('/body'):
			issue_body = issue_body[5:]

		return [SlotSet("issue_body", issue_body)]
