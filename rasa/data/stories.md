## happy path               <!-- name of the story - just for debugging -->
* greet              
  - utter_greet
* mood_great               <!-- user utterance, in format _intent[entities] -->
  - utter_happy

## sad path 1               <!-- this is already the start of the next story -->
* greet
  - utter_greet             <!-- action of the bot to execute -->
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## issues path
* greet
  - utter_greet
* list_issues
  - action_list_issues

## create issues path
* greet
  - utter_greet
* create_issues
  - action_create_issue

## ask for issues
* list_issues
  - action_list_issues

## create new issue
* create_issue
  - action_create_issue
