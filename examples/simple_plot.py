# Simple script that can run without instruements

from pyslave.data import xy

fig, ax = subplots()
values_to_scan = np.linspace(0,1,100)
values_measured = ones_like(values_to_scan)*nan

#main
for i, x in enumerate(values_to_scan) :
    # Fake measurement
    values_measured[i] = sin(x)
    #disp('Step #{0}'.format(i))

    # Plot the data
    ax.clear()
    ax.plot(values_to_scan, values_measured)
    #draw

    #looptime?
    #pause?
    #abort?

# Save data
data = xy(x=values_to_scan, y=values_measured)
data.save('mydata.txt')
