IPython shell magic commands
============================

.. :module:: magic

Pyslave is designed to be used in the IPython Qt console. Loading pyslave imports the "magic" functions defined in the ``magic`` module.
These functions are designed to load instruments, launch scripts and interact with them.



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
    
Quick measurement functions
---------------------------

**%fetch_txt** *instrument* *filename* *increment=True*

    Fetch data from an instrument and save them to a text file. If no fetch method is specified, fetch() is used. The filename is automatically incremented unless specified with increment=False.

        ::
        
            fetch_txt vna1 trace.txt
            fetch_txt vna1.fetch(channel=2) trace.txt
        
          
        Fetch channel 1 data from the VNA and save them to trace000.txt. Then fetch channel 2 data from the VNA and save them to trace001.txt
  
**%fetch_h5** *instrument* *filename* *key=value ...*

    Fetch data from an instrument and save them to a HDF5 file. If no fetch method is specified, fetch() is used. The filename is automatically incremented unless specified with increment=False.
    The extra keywords are passed to the save_h5 function (see pyslave.script.save_h5).    

        ::
        
            fetch_h5 vna1 trace.h5 dataset='channel 1' increment=False compression='gzip' 
            fetch_h5 vna1.fetch(channel=2) trace.h5 dataset='channel 2' increment=False
        
            
        Fetch channel 1 data from the VNA and save them to trace.h5 with compression. Then fetch channel 2 data from the VNA and save them to a different dataset in trace.h5.

**%monitor** *instrument_read_method* *time_interval*

    Monitor the output of an instrument and plot it. If the time interval is not given, it is set to one second.
    
        ::
        
            monitor dmm1.measurement.read(1) 5
            
        Monitor the dmm1 output every 5 seconds 

**%measure** *key=value ...*

    Scan one value while monitoring the output of an instrument. Just enter ``measure`` and follow the instructions.
            
Miscellaneous functions
-----------------------

**%today**

    Change directory to today's data directory, create it if it does not exist.
    The root data directory is defined in magic.py.

**%lastday**

    Change directory to the last day of data.

