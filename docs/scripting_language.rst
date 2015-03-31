Scripting language
==================

A script is a standard Python file including special comments that are interpreted by slave during the conversion.
The only mandatory comment is ``#main``. It separates the script initialization from the main script section.
Everything after the ``#main`` comment is executed in a separate thread.

Here is a simple script example that scans the power of a vna and record the average transmission :
::
    fig = figure(1)
    fig.clf()
    ax = fig.add_subplot(111)
    power = linspace(1e-1,0.3,100)
    power = r_[power,flipud(power)]
    out = ones_like(power)*nan

    #main
    for index,p in enumerate(power):
        #pause?
        # Change parameter
        vna1.SetPower(power=10*log10(p))
        # Acquire data
        time.sleep(1)
        data = vna1.fetch()
        out[index] = mean(data[:,0]**2+data[:,1]**2)
        # Display data
        ax.clear()
        ax.plot(power,out)
        #draw
        #break?
        #looptime?


Comments interpreted by slave
-----------------------------

.. function:: #main


