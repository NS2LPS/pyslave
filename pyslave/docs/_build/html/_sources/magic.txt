IPython shell magic commands
============================

.. :module:: magic

Pyslave is designed to be used in the IPython Qt console. Loading pyslave imports the "magic" functions defined in the ``magic`` module.
These functions are designed to load instruments, launch scripts and interact with them.



Instrument functions (shortcuts to the instruments module)
----------------------------------------------------------

**%openinstr** *resource*

    Load the VISA instrument at the specified resource.

**%openall**

    Load all GPIB instruments.

**%listall**

    List all loaded instruments.

**%closeinstr** *instrument_short_name*

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

Quick measurement functions
---------------------------

**%capture** *instrument_method* *filename* *key=value ...*

    Fetch data from an instrument, plot them and save them to a file if filename is given.
    If parentheses are omitted in ``instrument_method`` then ``instrument_method()`` is called.
    Extra keyword arguments are passed to the save function. See the ``data`` module for more information.

        ::

            capture vna1 trace.txt
            capture vna1 trace.h5 compression='gzip'
            capture vna1(channel=2) trace.h5 compression='gzip'

        Fetch channel 1 data from the VNA and save them to trace000.txt. Fetch channel 1 & 2 from the VNA and save them as two datasets in a HDF5 file.


**%monitor** *instrument_method* *time_interval*

    Monitor the output of an instrument and plot it. If parentheses are omitted in ``instrument_method`` then ``instrument_method()`` is called.
    If the time interval is not given, it is set to one second.
    Data are available in the shell using the ``monitor_out`` variable.

        ::

            monitor dmm1 5

        Monitor the dmm1 output every 5 seconds

**%measure** *key=value ...*

    Scan one value while monitoring the output of an instrument. Just enter ``measure`` and follow the instructions. As above, parentheses can be omitted
    and will be added automatically with the specific case that the ``set_function`` will be changed to ``set_function(x)`` where ``x`` is the scanned parameter.
    Data are available in the shell using the ``measure_out`` variable.


Miscellaneous functions
-----------------------

**%today**

    Change directory to today's data directory, create it if it does not exist.
    The root data directory is defined in magic.py.

**%lastday**

    Change directory to the last day of data.
