import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

def init_system_logging():
    logger.debug('Message From DEBUG')
    logger.info('Message From INFO')
    logger.warning('Message From WARNING!')      
    logger.error('Message From ERROR')
    logger.critical('Message From CRITICAL')

init_system_logging()


logger.setLevel(logging.ERROR)
print("\nApres set niveau log à ERROR :")
init_system_logging()