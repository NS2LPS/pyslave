# Scan the power of the vna and acquire spectra

import time
from pyslave.data import increment_file

fig,ax = subplots()
power = linspace(1e-4,1,100)

# Set number of averages
vna1.SetAverageState(1, True)
vna1.SetAverageFactor(1, 20)

filename = increment_file('power_scan_.h5')

#main
for p in power:
    #pause?

    # Change parameter
    vna1.SetPower(power=10*log10(p))
    vna1.RestartAverage()

    # Acquire data
    vna1.wait_for_average()
    data = vna1()

    # Display data
    ax.clear()
    data.plot(ax)
    #draw

    # Save data
    data.save(filename)

    #abort?
    #looptime?
