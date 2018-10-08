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
    counter = os.getenv('SLAVE_ID',0)
    logfile = os.path.normpath(os.path.join(os.path.dirname(__file__), 'log/pyslave_{0}.log'.format(counter)))
    fh = logging.handlers.TimedRotatingFileHandler(logfile, when='midnight')
    fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
logger.info('Pyslave loaded')

# Reference to slave window
__slave__ = {'window':None}

# Slave disp
def __slave_disp__(msg):
    logger.info(msg)
    if __slave__['window'] is None:
        print(msg)
    else:
        __slave_window__ = __slave__['window']
        if __slave_window__.thread and __slave_window__.thread.isRunning():
            __slave_window__.thread.display(msg, echo=False, log=False)
        else:
            print(msg)
