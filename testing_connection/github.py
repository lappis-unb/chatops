import json
import requests
import re
from token import GITHUB_TOKEN

def list_issues():
	response = requests.get("https://api.github.com/repos/gabibguedes/teste/issues")
	api_list = response.json()
	message = ''
	for issue in api_list:
		message += str(issue['number'])+ " - " + issue['title'] + '\n'

	return message

def create_issue():
	response1 = requests.get("https://api.github.com/repos/gabibguedes/teste/issues")
	issue = {'title': 'new bot issue (' + str(response1.json()[0]["number"]+1)+')', 'body': 'hello github'}

	response = requests.post('https://api.github.com/repos/gabibguedes/teste/issues',
	headers = {'Authorization': 'token ' + GITHUB_TOKEN},
	data = json.dumps(issue))
	message = 'New Issue Created \n' + '#'+ str(response.json()["number"]) + ' ' + response.json()["title"] + '\n' + response.json()["body"] + '\n' + response.json()["html_url"]
	return message

def split_string():
	issue_name = '/namemy issue'
	if issue_name.startswith('/name '):
		issue_name = issue_name[6:]
	elif issue_name.startswith('/name'):
		issue_name = issue_name[5:]
	return issue_name

print split_string()
