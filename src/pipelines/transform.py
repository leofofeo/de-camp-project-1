import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

from connectors.database import enact_db_transaction
from logger import logger

def create_annual_company_data_table(db_conn_data):
    logger.info("Creating annual_company_data table")

    current_dir = Path(__file__).parent
    parallel_dir = current_dir.parent / 'data' / 'jobs'

    file_path = parallel_dir / 'seed_annual_company_data_table.sql'
    fd = open(file_path, 'r')
    sql_file = fd.read()
    fd.close()

    enact_db_transaction(sql_file, db_conn_data)

def run_transformations(db_conn_data):
    logger.info("Creating annual_company_data table")

    current_dir = Path(__file__).parent
    parallel_dir = current_dir.parent / 'data' / 'migrations'

    file_path = parallel_dir / '002_alter_senator_trades_add_transaction_columns.sql'
    fd = open(file_path, 'r')
    sql_file = fd.read()
    fd.close()

    enact_db_transaction(sql_file, db_conn_data)