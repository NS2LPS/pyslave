# Measure IV curves as a function of a extra parameter, e.g. magnetic field

import time
from pyslave.data import xy, increment_file
fig, ax = subplots()

vyoko = r_[ linspace(0,1.,101), linspace(1.,-1.,201), linspace(-1.,0,101) ]
Icoil = linspace(0.251, 0.501, 251)
filename = increment_file('Bsweep.h5')

# Set dmm to fast mode
dmm1._interface.write('VOLT:DC:NPLC 1')
dmm1._interface.write('DET:BAND 200')

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
        # Change Yoko
        dcpwr1(v, 1.)
        dcpwr1.ready()
        # Acquire data
        vmeas[index] = dmm1()
        #abort?
    # Plot I-V
    ax.cla()
    ax.plot(vyoko, vmeas)
    #draw

    # Save as h5 
    iv = xy(x=vyoko, y=vmeas, Icoil=im)
    iv.save(filename)

    #abort?
    #looptime?
