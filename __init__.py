"""Pyslave is a package to script experiment in Python. It contains :
* "Magic" functions to be used in the IPython shell. These functions allow to easily load instruments and launch scripts.
* A GUI to monitor the running script and interact with it.
* Python Instrument drivers
"""

import logging, os, logging.handlers, configparser

########################################################
# Read config file
########################################################
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'pyslave.ini'))
data_directory = config.get('PYSLAVE','data directory',fallback='')
logging = config.getboolean('PYSLAVE','logging',fallback=False)
loadall = config.getboolean('PYSLAVE','loadall',fallback=False)

########################################################
# Logger
########################################################
if logging:
    logger = logging.getLogger('pyslave')
    logger.setLevel(logging.DEBUG)
    logger.propagate = 0
    # Create file handler
    if not logger.handlers:
        logfile = os.path.normpath(os.path.join(os.path.dirname(__file__), 'log/pyslave.log'))
        fh = logging.handlers.TimedRotatingFileHandler(logfile, when='midnight', delay=True)
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        fh.setLevel(logging.DEBUG)
        logger.addHandler(fh)

########################################################
# Load pyslave modules
########################################################
from pyslave.magic_data import *
if loadall:
    from pyslave.magic import *
if logging:
    logger.info('Pyslave loaded')

