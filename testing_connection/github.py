import json
import requests



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
	headers = {'Authorization': 'token 1fb78288a200219b9ef664f8598d82c3e8242c4e'},
	data = json.dumps(issue))
	message = 'New Issue Created \n' + '#'+ str(response.json()["number"]) + ' ' + response.json()["title"] + '\n' + response.json()["body"] + '\n' + response.json()["html_url"]
	return message

print create_issue()
print list_issues()
