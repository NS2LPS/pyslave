"""The *pyslave* module provides function to open instruments and load them as Python objects.
It also provides an easy way to run scripts in a seperate thread to control an experiment.

The module contains :

* "Magic" functions to be used in the IPython shell. These functions are shortcuts to load instruments and launch scripts.
* A GUI to monitor the running script and interact with it.
* Python Instrument drivers

"""

import logging, os, logging.handlers

########################################################
# Start logging pyslave activity
########################################################
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
logger.info('Pyslave loaded')

