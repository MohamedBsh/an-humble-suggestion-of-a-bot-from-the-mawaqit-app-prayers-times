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

format-check: ## Black formater and isort (check only for ci)
	pipenv run black --check .
	pipenv run isort . --check-only --profile black

format:  ## Autoformat project codebase with black and isort
	pipenv run black .
	pipenv run isort . --profile black

install-dependencies: clean-venv ## Install Python dependencies thanks to pipenv
	source install.sh

control-quality-check: format-check