# Scan the power of the vna and acquire spectra

import time

fig,ax = subplots()
power = linspace(1e-4,1,100)

# Set number of averages
vna1.SetAverageFactor(channel=1, averageFactor=20)

#main
for p in enumerate(power):
    #pause?

    # Change parameter
    vna1.SetPower(10*log10(p))
    vna1.RestartAverage()

    # Acquire data
    vna1.wait_for_average()
    data = vna1()

    # Display data
    ax.clear()
    data.plot(ax)
    #draw

    # Save data
    data.save('power_scan.h5')

    #abort?
    #looptime?
