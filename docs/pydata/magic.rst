IPython shell ``pydata`` magic commands
=========================================
Use::

    from pydata.magic import *

to load the magic functions in IPython. These functions are designed to
quickly access data folder that are stored in a root data folder.
This folder is set in the ``pydata.ini`` file. The directory of the configuration
file can be located using::

    import pydata
    print(pydata.__file__)


**%today**

    Change directory to today's data directory, create it if it does not exist.
    The root data directory is defined in magic.py.

**%lastday**

    Change directory to the last day of data.

**%rmlast**

    Remove the last created file in the current directory.
