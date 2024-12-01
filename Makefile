# Run FastAPI app
run: ## Run FastAPI app
	uvicorn main:app --reload

activate:
	source venv/bin/activate

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

