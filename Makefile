clean-test: ## Remove test and coverage artifacts (e.g., .tox, .coverage)
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

check-pipenv: ## Check that pipenv has been installed
	@if ! command -v pipenv 1> /dev/null 2>&1; \
	then \
		echo "Installing pipenv..."; \
		python -mpip install pipenv; \
		echo "... pipenv installed"; \
	fi
	@if ! command -v pipenv 1> /dev/null 2>&1; \
	then \
		echo "Error - pipenv cannot be installed"; \
		exit 1; \
	fi

clean-venv: check-pipenv ## Remove any install Python virtual environment
	pipenv --rm || echo "No virtualenv has been created yet; that is all good"
	\rm -f Pipfile.lock

test: check-pipenv clean-test
	pipenv run python3 -m pytest tests/test.py

install-dependencies: clean-venv ## Install Python dependencies thanks to pipenv
	pipenv install
	pipenv install --dev
	pipenv shell

format-check: ## Black formater (check only for ci)
	pipenv run black --check .

format:  ## Autoformat project codebase with black
	pipenv run black .

control-quality-check: test