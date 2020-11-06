SHELL := /bin/bash

venv: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test:
	py.test tests

.PHONY: clean-pyc clean-build