import os
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from connectors.database import create_tables, tables_exist, drop_tables
from pipelines.extract import extract_data

if __name__=='__main__':
    from logger import logger
    logger.info("Starting the application") 

    drop_tables();

    if not tables_exist():
        logger.info("Creating tables")
        create_tables()

        db_name = os.getenv("DB_NAME", "data_ticker")
        db_user = os.getenv("DB_USER", "postgres")
        db_password = os.getenv("DB_PASSWORD", "")
        db_host = os.getenv("DB_HOST", "localhost")
        db_port = os.getenv("DB_PORT", 5432)

        connection_url = URL.create(
            drivername="postgresql+psycopg2",
            username=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name,
        )
        engine = create_engine(connection_url)
        extract_data(engine)
    else:
        logger.info("Tables already exist")
        
    # TODO; create annual company data

    logger.info("Finished the application")