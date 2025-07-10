import logging

logger = logging.getLogger() #Recup instance de RootLogger
#logger.disabled = True
print(type(logger)) #<class 'logging.RootLogger'>
logger.setLevel(logging.INFO) # niveau de log

console_handler = logging.StreamHandler() #Isntanciation d'un Handler
logger.addHandler(console_handler) #attache handler au logger

def log():
    logger.debug("DEBUG MSG")
    logger.info("Application démarrée avec succès.")
    logger.warning("WARNING MSG")
    logger.error("Échec de la connexion à la base de données.")
    logger.critical("C'est la guerre")

log()