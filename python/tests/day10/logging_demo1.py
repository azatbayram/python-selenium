#logging come with python built-in, you do not install extra library
import logging

logging.basicConfig(level=logging.DEBUG, filename='../logs/demologging.log', filemode='a', format='%(asctime)s - %(levelname)s : %(message)s' )


logging.debug("This is debug logging message")
logging.info("This is info logging message")
logging.warning("This is warning logging message")
logging.error("This is error logging message")
logging.critical("This is critical logging message")