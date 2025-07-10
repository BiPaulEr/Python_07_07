import logging

class MyFilter(logging.Filter):
    def filter(self, record):
        return not "TOKEN" in record.msg

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
logger.addHandler(streamHandler)


myfilter = MyFilter()
logger.addFilter(myfilter)


logger.debug("TOKEN glt")
logger.debug("Bonjour ")