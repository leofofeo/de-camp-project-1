## Instructions for running pipeline locally
1. Create a database called `ticker_data` and ensure that postgres is running your machine
2. Run `git checkout main` and do a `git pull`
3. Create a `.env`  file in your project root - you can copy the `template.env` file and adjust the values as needed based on your local environment

From here, you can either:
 - activate your conda environment and run `pip install -r requirements.txt` from the project root, then run `make run`
 - make sure docker is running, and run `docker compose up` from the project root

Available tables are:
- `company_profiles`
- `company_historical_data`
- `companny_annual_financial_data`
- `senators`
- `senator_trades`

Available views:

Data set used:

Extraction method:

Load method:

Transformations:

Test coverage:

Logging method:

Containerization:

