SHELL := /bin/bash -O extglob

# Credentials

credentials.json:
	$(info Run python ./auth_setup.py to generate credentials)
	$(error $(@) not found)

google_credentials.json:
	$(info Get project ID and API key from https://console.developers.google.com/)
	$(info Put into JSON with keys GoogleID, GoogleKey)
	$(error $(@) not found)

CREDENTIALS := credentials.json google_credentials.json

# Assets

dist:
	mkdir -p $(@)

adjectives.txt: | $(ENV_DEV)
	$(ENV)/bin/python getadjectives.py

people.txt: | $(ENV_DEV)
	$(ENV)/bin/python getpeople.py

ASSETS := adjectives.txt people.txt

.PHONY: clean
clean:
	rm -rf dist

# Dev

ENV_DEV := .env_dev

$(ENV_DEV):
	virtualenv $(@)
	$(@)/bin/pip install -e .[dev]

.PHONY: test
test: | $(ENV_DEV)
	$(ENV_DEV)/bin/python wtffuture.py
	$(ENV_DEV)/bin/python search.py

# Lambda

AWS_ARGS ?=
LAMBDA_NAME := WtfFutureTwitterBot
PAYLOAD := dist/lambda-deploy.zip

ENV_RELEASE := .env_release

$(ENV_RELEASE):
	virtualenv $(@)
	$(@)/bin/pip install -e .

.PHONY: zip
zip: $(PAYLOAD)

$(PAYLOAD): *.py $(CREDENTIALS) $(ASSETS) | $(ENV_RELEASE) dist
	rm -rf $(@)
	zip $(@) $(^) -x \*.pyc
	cd $(ENV_RELEASE)/lib/python3.*/site-packages; \
		zip -r $(PWD)/$(@) ./!(pip*|wheel*|setuptools*|easy_install*|) -x \*.pyc

.PHONY: deploy
deploy: $(PAYLOAD)
	aws $(AWS_ARGS) lambda update-function-code \
		--function-name $(LAMBDA_NAME) \
		--zip-file fileb://$$(pwd)/$(<)

.PHONY: invoke
invoke:
	aws $(AWS_ARGS) lambda invoke \
		--function-name $(LAMBDA_NAME) \
		/dev/null
