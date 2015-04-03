IPython shell magic commands
============================

.. :module:: magic

Pyslave is designed to be used in the IPython Qt console. 
Importing the magic module defines functions to load instruments, launch scripts and interact with them.

The magic functions can be automatically loaded by including the following line in the profile configuration of IPython:

::

    from pyslave.magic import *

Instrument functions (shortcuts to the instruments module)
----------------------------------------------------------

**%openinst** *resource*

    Load the VISA instrument at the specified resource.

**%openall**

    Load all GPIB instruments.

**%listall**

    List all loaded instruments.

**%closeinst** *instrument_short_name*

    Close the specified instrument.
    
    
Slave functions (run and interact with scripts )
------------------------------------------------

**%call** *filename*

    Convert and launch a script. If *filename* ends with *converted* or *converted.py*, conversion is skipped.

**%pause**

    Pause the running script.

**%resume**

    Resume the paused script.

**%abort**

    Abort the running script. If the script does not finish within 10 s, a dialog appears to eventually force the script to terminate.

**%window**

    Show the slave window if it was closed.

Miscellaneous functions
-----------------------

**%today**

    Change directory to today's data directory, create it if it does not exist.
    The root data directory is defined in magic.py.

**%lastday**

    Change directory to the last day of data.

**%fetch_txt** *instrument* *filename*

    Fetch data from an instrument and save them to a text file.
  
**%fetch_txt** *instrument* *filename* *keywords ...*

    Fetch data from an instrument and save them to a HDF5 file. The extra keywords are passed to the save_h5 function (see pyslave.script).