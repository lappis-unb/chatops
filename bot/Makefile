.PHONY: clean train-nlu train-core run-bash run-telegram

help:
	@echo ""
	@echo "	- clean:"
	@echo "		Remove python artifacts and build artifacts."
	@echo ""
	@echo "	- train-nlu:"
	@echo "		Trains a new nlu model using the projects Rasa NLU config"
	@echo ""
	@echo "	- train-core:"
	@echo "		Trains a new dialogue model using the story training data"
	@echo ""
	@echo "	- run-bash:"
	@echo "		Runs the chatbot on bash"
	@echo ""
	@echo "	- run-telegram:"
	@echo "		Runs the chatbot on telegram. You should configure the telegram_credentials.yml file before running this command"
	@echo ""

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf docs/_build
	rm -rf models/

train-nlu:
	python -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose

train-core:
	python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue --epochs 200

run-bash:
	python -m rasa_core.run -d models/current/dialogue -u models/current/nlu

run-telegram:
	python -m rasa_core.run -d models/current/dialogue -u models/current/nlu --port 5002 -c telegram --credentials telegram_credentials.yml
