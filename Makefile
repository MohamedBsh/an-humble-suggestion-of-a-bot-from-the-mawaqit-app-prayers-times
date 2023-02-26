clean-venv:
	pipenv --rm || echo "No virtualenv has been created yet; that is all good"
	\rm -f Pipfile.lock

format-check:
	pipenv run black --check .
	pipenv run isort . --check-only --profile black

format:
	pipenv run black .
	pipenv run isort . --profile black

install-dependencies: clean-venv
	pipenv install -r requirements.txt --dev

control-quality-check: format-check