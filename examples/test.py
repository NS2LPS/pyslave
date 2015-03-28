import time

fig,ax = subplots()
x = np.linspace(0,1,1000)

#main
for i in range(10):
    time.sleep(1)
    #disp('Step #{0}'.format(i))
    ax.clear()
    ax.plot(x,np.sin(x)+0.01*np.random.rand(len(x)))
    #draw
    #looptime?
    #pause?
    #break?
