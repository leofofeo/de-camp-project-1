import os
from dotenv import load_dotenv

import psycopg2
from pathlib import Path

load_dotenv()

def database_exists():
    load_dotenv()
    db_name = os.getenv("DB_NAME", "data_ticker")
    db_user = os.getenv("DB_USER", "postgres")
    db_password = os.getenv("DB_PASSWORD", "")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", 5432)

    with psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        port=db_port,
        host=db_host,
    ) as connection:
        db_exists = False
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM pg_database where datname=%s;", (os.getenv("DB_NAME"),))
            connection.commit()
        
            exists = cursor.fetchone()
            print(exists)
            if exists:
                print("database exists")
                db_exists = True
            else:
                print("databse doesn't exist")

    return db_exists
    
def initialize_database():
    print("Initializing the database")

    current_dir = Path(__file__).parent
    parallel_dir = current_dir.parent / 'data' / 'migrations'
    file_path = parallel_dir / '001_initial_migration.sql'
    print(file_path)
    fd = open(file_path, 'r')
    sql_file = fd.read()
    fd.close()

    enact_db_transaction(sql_file)


def enact_db_transaction(statement):
    load_dotenv()
    db_name = os.getenv("DB_NAME", "data_ticker")
    db_user = os.getenv("DB_USER", "postgres")
    db_password = os.getenv("DB_PASSWORD", "")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", 5432)
    print("Executing statement: ", statement)

    with psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        port=db_port,
        host=db_host,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(statement)
            connection.commit()
            print("Transaction committed")
            