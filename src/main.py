from pipelines.database import database_exists, initialize_database

if __name__=='__main__':
    from logger import logger
    logger.info("Starting the application") 

    initialize_database()
    
    
    logger.info("Finished the application")