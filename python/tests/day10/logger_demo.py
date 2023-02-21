import logging

class LoggerDemo:

    def sample_logger(self):
        #create logger
        logger=logging.getLogger(LoggerDemo.__name__)
        logger.setLevel(logging.DEBUG)
        #create console handler or file handler and set the log level
        ch=logging.StreamHandler()
        fh=logging.FileHandler('../logs/demologfile.log')
        #create formatter - how you want your logs to be formatted
        formatter=logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #add formatter to console or file handler
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        #add console handler to logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        #application code - log messages
        logger.debug("This is debug logging message")
        logger.info("This is info logging message")
        logger.warning("This is warning logging message")
        logger.error("This is error logging message")
        logger.critical("This is critical logging message")

ld=LoggerDemo()
ld.sample_logger()