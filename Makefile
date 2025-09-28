.PHONY: run lint test fmt

run:
	uvicorn app.main:app --reload

lint:
	ruff check --fix .
	black .

fmt:
	black .
	ruff check --fix .

test:
	pytest
