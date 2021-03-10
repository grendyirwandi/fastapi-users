import logging
from logging.handlers import RotatingFileHandler

class Logging:
    def main(self):    
        log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s',datefmt='%d-%b-%y %H:%M:%S')

        logFile = 'app.log'

        my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, 
                                        backupCount=2, encoding=None, delay=0)
        my_handler.setFormatter(log_formatter)
        my_handler.setLevel(logging.DEBUG)

        app_log = logging.getLogger('root')
        app_log.setLevel(logging.INFO)
        app_log.addHandler(my_handler)