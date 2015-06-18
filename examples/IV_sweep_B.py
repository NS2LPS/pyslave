# Measure IV curves as a function of a extra parameter, e.g. magnetic field

import time
from pyslave.data import xy, increment_file
fig, ax = subplots()

vyoko = r_[ linspace(0,1,51), linspace(1,-1,101), linspace(-1,0,51) ]
Icoil = linspace(0, 0.1, 30)
filename = increment_file('Bsweep.h5')

#main
for im in Icoil:
    # Set current through the coil
    dcpwr2.outputs[0].current_limit = im
    time.sleep(1)
    #disp('Icoil set to {0}'.format(im))

    # Acquire IV
    vmeas = ones_like(vyoko)*nan
    for index,v in enumerate(vyoko):
        #pause?
        # Change parameter
        dcpwr1(v)
        dcpwr1.ready()
        # Acquire data
        vmeas[index] = dmm1()
        # Plot I-V
        ax.cla()
        ax.plot(vyoko, vmeas)
        #draw
        #abort?

    # Save as h5 
    iv = xy(x=vyoko, y=vmeas)
    iv.save(filename)

    #abort?
    #looptime?
