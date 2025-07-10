import logging, os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

filehandler = logging.FileHandler(os.path.join(os.path.dirname(__file__), "file"+".log"), mode='w')
logger.addHandler(filehandler)

filehandler.setFormatter(logging.Formatter(
    "%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s", datefmt="%d/%Y %I:%M"
))

for i in range(0, 1000 * 3):
    logger.debug(f"QUOI Message numero : {i}")
