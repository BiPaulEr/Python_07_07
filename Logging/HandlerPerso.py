import logging
import sentry_sdk

class SentryHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        url = os.getenv("URL_SENTRY_SERVEUR")
        sentry_sdk.init(url)

    def emit(self, record):
        real = self.foramt(record)
        sentry_sdk.capture_messeage(real)
    