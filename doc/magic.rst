IPython shell magic commands
============================

.. :module:: magic

Pyslave is designed to be used in the IPython Qt console. Importing the magic module defines the magic functions listed below
and also creates the slave window to monitor running scripts.

The magic functions can be automatically loaded by including the following line in the startup configuration of IPython:

::
    from pyslave.magic import *

Instrument functions (shortcuts to the instruments module)
----------------------------------------------------------       

.. function:: %openall

    Load all GPIB instruments.

.. function:: %listall

    List all loaded instruments.

Slave functions (run and interact with scripts )
------------------------------------------------

.. function:: %call *filename*

    Convert and launch a script. If *filename* ends with converted or converted.py, conversion is skipped.

.. function:: %pause

    Pause the running script.

.. function:: %resume

    Resume the paused script.

.. function:: %abort

    Abort the running script. If the script does not finish within 10 s, a dialog appears to eventually force the script to terminate.

.. function:: %window

    Show the slave window if it was closed.

Miscellaneous functions
-----------------------

.. function:: %today

    Change directory to today's data directory, create it if it does not exist.
    The root data directory is defined in magic.py.

.. function:: %lastday

    Change directory to the last day of data. 