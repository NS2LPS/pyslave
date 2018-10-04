``pyslave`` scripting language
===============================

A script is a standard Python file including special comments that are interpreted by slave during the conversion.
The only mandatory comment is ``#main``. It separates the script initialization from the main script section.
Everything after the ``#main`` comment is executed in a separate thread.

Here is a simple script example that scans the power of a vna and record the average transmission: ::

    fig, ax = subplots()
    power = linspace(1e-1,0.3,100)
    out = ones_like(power)*nan

    #main
    for index,p in enumerate(power):
        # Change parameter
        vna1.SetPower(power=10*log10(p))
        # Acquire data
        time.sleep(1)
        data = vna1.fetch()
        out[index] = mean(abs(data.Sij)**2)
        # Display data
        ax.clear()
        ax.plot(power,out)
        #draw
        #abort


Comments interpreted by pyslave
----------------------------------

.. function:: #main

    This comment signals the start of the cript main body. Everything after this comment is wrapped in a function
    that will be run in a separate thread. This comment is mandatory and must appear before the other comments listed below.

.. function:: #pause

    This line checks if the user asked for a pause. If yes it will wait until the user resumes or aborts the script.

.. function:: #abort

    This line inserts a Python break statement if the user aborts the script. Multiple ``#abort`` should be used to exit nested loops.
    If the script does not contain any ``#pause`` then ``#abort`` also checks if the user asked for a pause.

.. function:: #disp(string)

    Displays a string in the slave window.

.. function:: #looptime

    Displays the time ellapsed between two calls to the function.

.. function:: #draw

    Tell matplotlib to redraw figures.
