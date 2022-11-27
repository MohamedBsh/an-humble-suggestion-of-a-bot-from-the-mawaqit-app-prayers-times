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

clean-venv: check-pipenv
	pipenv --rm || echo "No virtualenv has been created yet; that is all good"
	\rm -f Pipfile.lock

format-check:
	pipenv run black --check .
	pipenv run isort . --check-only --profile black

format:
	pipenv run black .
	pipenv run isort . --profile black

install-dependencies: clean-venv
	source install.sh

control-quality-check: format-check