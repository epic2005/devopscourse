import logging
from logging.handlers import *

import sys


logger = logging.getLogger(name='error')
logger.setLevel(logging.NOTSET)

handle = logging.FileHandler('/tmp/aaa.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handle.setLevel(logging.ERROR)
handle.setFormatter(formatter)
logger.addHandler(handle)

debug_handler = logging.StreamHandler()
debug_handler.setLevel(logging.DEBUG)
logger.addHandler(debug_handler)

if sys.argv[1] == 'debug':
    logger.setLevel(logging.DEBUG)

logger.error('I am a error log')
logger.debug('I am a debug log')