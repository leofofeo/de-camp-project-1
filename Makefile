run:
	python ./src/main.py

conda-freeze:
	pip list --format=freeze > requirements.txt