from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from connectors.database import (
    create_tables, 
    tables_exist, 
    drop_tables,
    get_db_conn_data,
    create_views,
)
from pipelines.extract import extract_data
from pipelines.transform import run_transformations

if __name__=='__main__':
    from logger import logger
    logger.info("Starting the application") 
    logger.disabled = True

    db_conn_data = get_db_conn_data()

    drop_tables(db_conn_data);

    if not tables_exist(db_conn_data):
        logger.info("Creating tables")
        create_tables(db_conn_data)
        connection_url = URL.create(
            drivername="postgresql+psycopg2",
            username=db_conn_data["db_user"],
            password=db_conn_data["db_password"],
            host=db_conn_data["db_host"],
            port=db_conn_data["db_port"],
            database=db_conn_data["db_name"],
        )
        engine = create_engine(connection_url)
        extract_data(engine, db_conn_data)
    
    else:
        logger.info("Tables already exist")
    
    run_transformations(db_conn_data)
    create_views(db_conn_data)

    logger.info("Finished the application")