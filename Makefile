# Makefile

install:
	poetry install

format:
	isort .
	black .

lint:
	isort . --check
	black . --check
	prospector --with-tool pep-257
test:
	ward
