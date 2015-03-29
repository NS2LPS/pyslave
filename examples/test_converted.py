# Auto generated script file

import time

fig = figure(1)
fig.clf()
ax = fig.add_subplot(111)

x = np.linspace(0,1,1000)

# Main script function
def script_main(thread):
    for i in range(100):
        time.sleep(1)
        thread.display('Step #{0}'.format(i))
        ax.clear()
        ax.plot(x,np.sin(x)+0.01*np.random.rand(len(x)))
        thread.draw()
        thread.looptime()
        thread.pause()
        if thread.stopflag : break
