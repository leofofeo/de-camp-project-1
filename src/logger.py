import logging

    # Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file named app.log
        logging.StreamHandler()  # Also log to console (standard output)
    ]
)

logger = logging.getLogger(__name__)