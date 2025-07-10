import os
import logging

logger = logging.getLogger(__name__)
#logger.disabled = True
logger.setLevel(logging.WARNING)
filehandler = logging.FileHandler(os.path.join(os.path.dirname(__file__), __name__+".log"))
logger.addHandler(filehandler)
logger.warning("QUOIIIIIIIIIIIIIIIIIIIIIIIIIII")


