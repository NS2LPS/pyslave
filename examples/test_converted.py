# Auto generated script file

#from matplotlib.pyplot import subplots
import time
#import numpy as np

fig,ax = subplots()
#x = np.linspace(0,1,1000)

# Main script function
def script_main(thread):
    for i in range(10):
        time.sleep(1)
        thread.display('Step #{0}'.format(i))
        ax.clear()
        ax.plot(x,np.sin(x)+0.01*np.random.rand(len(x)))
        thread.draw()
        thread.looptime()
        thread.pause()
        if thread.stopflag : break
