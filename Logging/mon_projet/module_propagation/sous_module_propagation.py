import logging
import os

logger = logging.getLogger(__name__)
handler = logging.FileHandler(os.path.join(os.path.dirname(__file__),"module_propagation.log"))
formatter = logging.Formatter(
    "%(name)s - %(funcName)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

def fonction_sous_module_propagation():
    logger.info("Exécution de fonction_sous_module_propagation.")
    logger.debug("Debugging dans fonction_sous_module_propagation")
