import logging


# logging.basicConfig(filename="chat-gebeta.log",
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('chat-gebeta.log')
formatter = logging.Formatter(
    '%(asctime)s:%(name)s:%(message)s', datefmt="%H:%M:%S")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
