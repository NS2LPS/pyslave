Getting started
================================

If you start IPython with the ``pyslave`` profile, all magic functions are loaded. Otherwise, you can load them with: ::

    from pyslave.magic import *
    
If you have GPIB instruments connected to your computer, you can load them using: ::

    >>>openGPIB
    dmm1       : Agilent Technologies 34410A GPIB0::21::INSTR
    
Here the instrument was recognized by pyslave and the corresponding driver is used.
If the instrument is not recognized, a generic GPIB instrument is returned: ::

    >>>openGPIB
    instr1     : Unknown instrument GPIB0::21::INSTR

You can write a small script to monitor the output of the instrument: ::

    import time
    fig,ax = subplots()
    out = []
    #main
    while True:
        time.sleep(1)
        res = float(instr1.query('READ?'))
        out.append(res)
        ax.cla()
        ax.plot(out)
        #draw
        #abort
        
Save it as *myscript.py* and launch it with: ::

    >>>call myscript
    Script is running...
    
The statements before the *#main* line are executed and the statements after the *#main* line
are run in a new thread. You can pause or finish the script using the *%pause* or *%abort* magic commands: ::

    >>>abort
    Aborting...
    Use %kill if script does not finish.
    Script finished.
    
The result of the measurement are accessible in the IPython console: ::

    >>>print(out)
    [-0.000138296625, -0.000141686483, -0.000148029773, -0.00014346886, -0.000140373631]
    
In order to customize instrument loading, edit the *pyslave.ini* file. 
