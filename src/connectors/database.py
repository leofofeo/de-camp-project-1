import os
from typing import TypedDict
from dotenv import load_dotenv

import psycopg2
from pathlib import Path

from logger import logger

load_dotenv()


class DBConnData(TypedDict):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int


def tables_exist(db_conn_data: DBConnData) -> bool:
    logger.info("Checking if tables exist")
    with psycopg2.connect(
        dbname=db_conn_data["db_name"],
        user=db_conn_data["db_user"],
        password=db_conn_data["db_password"],
        port=db_conn_data["db_port"],
        host=db_conn_data["db_host"],
    ) as connection:
        db_exists = False
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM information_schema.tables
                    WHERE table_schema = 'public'
                AND table_name = %s
                );
            """, ("company_profiles",))
            connection.commit()
        
            exists = cursor.fetchone()[0]
            if exists:
                db_exists = True

    return db_exists
    

def create_tables(db_conn_data: DBConnData):
    logger.info("Creating initial tables")

    current_dir = Path(__file__).parent
    parallel_dir = current_dir.parent / 'data' / 'migrations'
    file_path = parallel_dir / '001_create_primary_tables.sql'
    fd = open(file_path, 'r')
    sql_file = fd.read()
    fd.close()

    enact_db_transaction(sql_file, db_conn_data)


def drop_tables(db_conn_data: DBConnData):
    logger.info("Dropping tables")

    current_dir = Path(__file__).parent
    parallel_dir = current_dir.parent / 'data' / 'jobs'
    file_path = parallel_dir / 'drop_tables.sql'
    fd = open(file_path, 'r')
    sql_file = fd.read()
    fd.close()

    enact_db_transaction(sql_file, db_conn_data)


def enact_db_transaction(statement: str, db_conn_data: DBConnData):
    with psycopg2.connect(
        dbname=db_conn_data["db_name"],
        user=db_conn_data["db_user"],
        password=db_conn_data["db_password"],
        port=db_conn_data["db_port"],
        host=db_conn_data["db_host"],
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            connection.commit()
            print("Transaction committed")


def create_views(db_conn_data: DBConnData):
    logger.info("Creating views")

    current_dir = Path(__file__).parent
    parallel_dir = current_dir.parent / 'data' / 'jobs'
    file_path = parallel_dir / 'create_views.sql'
    fd = open(file_path, 'r')
    sql_file = fd.read()
    fd.close()

    enact_db_transaction(sql_file, db_conn_data)


def get_db_conn_data() ->  DBConnData:
    return {
        "db_name": os.getenv("DB_NAME", "data_ticker"),
        "db_user": os.getenv("DB_USER", "postgres"),
        "db_password": os.getenv("DB_PASSWORD", ""),
        "db_host": os.getenv("DB_HOST", "localhost"),
        "db_port": os.getenv("DB_PORT", 5432),
    }

