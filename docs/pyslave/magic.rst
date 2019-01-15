IPython shell ``pyslave`` magic commands
=========================================

Pyslave is designed to be used in the IPython Qt console. Use: ::

    from pyslave.magic import *

to load the magic functions in IPython. These functions are designed to
load instruments, launch scripts and interact with them. The ``pyslave.ini``
file is used to determine which instruments should be loaded.


Loading Instruments
---------------------

**%openall**

    Load all instruments as defined in the ``pyslave.ini`` file (see below). Instruments
    listed in the file but not plugged or not available are skipped. They
    can be loaded later by a new call to the function.

**%openinstr** *name*

    Load the instrument with the specified name, COM port or VISA resource. The function
    first looks into the 'pyslave.ini' file. If no match is found and the name contains COM,
    the corresponding serial port is opened. Otherwise, the function tries to open the VISA
    resource with the given name.

    Examples: ::

        opensintr dmm1
        openinstr COM3
        openinstr GPIB0::23::INSTR


**%openGPIB**

    Load all GPIB devices found on the VISA interface.

**%listall**

    List all loaded instruments.

**%listVISA**

    List all VISA resources present on the system.

**%closeinstr** *instrument_short_name*

    Close the specified instrument.

**%closeall**

    Close all instruments.

**%resetVISA**

    Reset the VISA interface.


The ``pyslave.ini`` file
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The file is organized in sections that gather instruments with the same interface.
Supported section names include ``VISA``, ``NI-DAQ``, ``COM`` and ``Other`` for custom instruments.
Each line of a section defines an instrument. The instrument definition contains
one or two arguments. The first one corresponds to the instrument address or any other string
that identifies the instrument. The second (optional) argument is the python driver that
should be used to load the instrument. This argument is mandatory for NI-DAQ and custom instruments.
The file is reloaded at each call of ``openall`` and ``openinstr``.

File example::

    [VISA]
    # For remote usage, prefix the adrress with the VISA server address
    # If driver is omitted, auto identification is attempted (slow).
    # Auto identification fails with old style Yokogawa's power supply.
    yoko1 = GPIB0::3::INSTR yokogawa.yokogawa7651.yokogawa7651
    dmm1  = GPIB0::21::INSTR agilent.agilent34401A
    gen1  = GPIB0::22::INSTR agilent.agilent33250A.agilent33250A
    zva   = GPIB0::25::INSTR rohdeschwarz.zvx.zva

    [COM]
    # USB instruments
    # If driver is omitted, generic serial port is used
    motor = COM3 connex.motor.motor

    [Other]
    # Custom instruments
    mmr3 = localhost mmr.mmr.mmr3
    mgc3 = 192.168.0.57 mmr.mmr.mgc3




Running Scripts
------------------------------------------------

**%call** *filename*

    Convert and launch a script. If *filename* ends with *converted* or *converted.py*, conversion is skipped.
    
**%convert** *filename*

    For debugging purposes: show how a script is converted by ``pyslave``

**%pause**

    Pause the running script.

**%resume**

    Resume the paused script.

**%abort**

    Abort the running script. The script must contains at least one ``#abort`` statement for this command to have an effect.

**%kill**

    Terminate the running script by sending a kill signal. Files that are left unclosed by the script may be corrupted.
    If the kill happens during communication with an instrument, you may have to close and reopen the instrument.

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
