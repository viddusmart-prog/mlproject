
import logging
import os
from datetime import datetime

# Create a log file name with timestamp
LOG_FILE = datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".log"

# Ensure there is a "logs" directory in the current working directory
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s in %(name)s "
           "(%(filename)s:%(lineno)d): %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
    print(f"Logging to: {LOG_FILE_PATH}")
