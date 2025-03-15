import logging

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_action(action, status, details=""):
    logging.info(f"{action} - {status} - {details}")
