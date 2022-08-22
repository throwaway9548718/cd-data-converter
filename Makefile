.PHONY: setup
setup: venv
	@echo "Done"


.PHONY: test
test: venv
	. venv/bin/activate && \
	black . && \
	isort . && \
	flake8 src/ && \
	bandit -r src/ && \
	python3 -m pytest tests/ -vv


venv: 
	python3 -m venv venv && \
	. venv/bin/activate && \
	venv/bin/pip install --upgrade pip && \
	venv/bin/pip install --upgrade setuptools && \
	venv/bin/pip install -e ".[dev]" && \
	venv/bin/pip list


.PHONY: clean
clean:
	find . -name venv \
	-or -name build \
	-or -name __pycache__ \
	-or -name .pytest_cache \
	-or -name *.egg-info \
	-or -name .mypy_cache \
	-or -name .tox \
	| xargs rm -rf