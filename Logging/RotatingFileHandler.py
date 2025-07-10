import logging, os
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

rotatingHandler = RotatingFileHandler(os.path.join(os.path.dirname(__file__), "rotating"+".log"), maxBytes=1024*100, backupCount=3)
logger.addHandler(rotatingHandler)

rotatingHandler.setFormatter(logging.Formatter(
    "%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s", datefmt="%d/%Y %I:%M"
))

for i in range(0, 1000 * 3):
    logger.debug(f"Message numero : {i}")
