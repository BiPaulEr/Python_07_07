import logging, os, time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

timeHandler = TimedRotatingFileHandler(os.path.join(os.path.dirname(__file__), "time"+".log"), interval=1, when="M", backupCount=3)
logger.addHandler(timeHandler)

timeHandler.setFormatter(logging.Formatter(
    "%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s", datefmt="%d/%Y %I:%M"
))

for i in range(0, 1000):
    time.sleep(1)
    logger.debug(f"Message numero : {i}")
