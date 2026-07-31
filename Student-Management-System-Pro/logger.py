import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=os.path.join("logs", "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_message(message):
    logging.info(message)