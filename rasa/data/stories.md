## say hello
* greet              
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## ask for issues
* list_issues
  - action_list_issues

## create new issue
* create_issue
  - utter_ask_issue_name
* answer_name
  - action_set_issue_name
  - utter_ask_issue_body
* answer_body
  - action_set_issue_body
  - action_create_issue
