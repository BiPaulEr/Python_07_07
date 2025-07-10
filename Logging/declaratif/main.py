import logging, os, yaml 
from logging.config import dictConfig

principale = logging.getLogger("principale")

with open(os.path.join(os.path.dirname(__file__), 'config_log.yaml'), 'r') as f:
    config = yaml.safe_load(f.read())
    dictConfig(config)

def log():
    principale.debug("DEBUG MSG")
    principale.info("Application démarrée avec succès.")
    principale.warning("WARNING MSG")
    principale.error("Échec de la connexion à la base de données.")
    principale.critical("C'est la guerre")

log()