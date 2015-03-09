#import

fig,ax = subplots()

power = linspace(1e-4,1,100)

# Number of averages
zva.SetAverageFactor(channel=1, averageFactor=20)

#main
with h5py.File('power_dependence_00.h5','w') as hdf:
    for index,p in enumerate(power):
        #pause?
        # Change parameter
        zva.SetPower(10*log10(p))
        zva.RestartAverage()
        # Acquire data
        zva.wait_for_average()
        rcernox =  dmm3.measurement.read()
        data = zva.fetch()
        # Display data
        #disp('#{0:03d} Rc {1}'.format(index,rcernox))
        ax.plot(data)
        #draw
        # Save data
        dset = hdf.create_dataset("data{0:03d}".format(index), data=data, compression = "gzip")
        dset.attrs['rcernox'] = rcernox
        zva.copy_sweep_parameters(dset.attrs)
        hdf.flush()
        #break?
        #looptime?
