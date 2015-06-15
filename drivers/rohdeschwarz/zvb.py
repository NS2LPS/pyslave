from __zvb__ import rszvb as dll
import numpy as np
import time
from pyslave.data import Sij

class zvb:
    """Rohde&Schwarz Vector Network Analyzer (ZVA,ZVB) driver. All the functions from the rszvb DLL are available as well as extra home made functions."""
    def __init__(self, address):
        self.iHandle = dll.rszvb_init(address, 1, 0)
    def __getattr__(self, name):
        dll_fun = getattr(dll, 'rszvb_' + name)
        def fun(*args, **kwargs):
            res = dll_fun(self.iHandle, *args, **kwargs)
            if dll_fun.output : return res
        return fun
    def __call__(self, channel=1):
        """Fetch the trace from the specified channel and return it as a Sij data object."""
        n = self.GetSweepNumberOfPoints(channel)
        data = np.empty((n, 2), np.float64)
        r = self.TraceResponseData(channel,0,data)
        if r!=2*n : raise dll.ZVBDLLERROR("TraceResponseData : missing data points.")
        return Sij( Sij=data, **self.acquisition_parameters(channel) )
    def wait_for_average(self, channel=1, sleep_time=0.5):
        """Only works with the ZVA."""
        n_average = self.GetAverageFactor(channel)
        time.sleep(sleep_time)
        while self.GetCurrentSweep(channel)<n_average :
            time.sleep(sleep_time)
    def acquisition_parameters(self, channel = 1):
        """Return the acquisition parameters for the specified channel."""
        start = self.GetStartFrequency(channel)
        stop = self.GetStopFrequency(channel)
        npoints = self.GetSweepNumberOfPoints(channel)
        power = self.GetPower(channel)
        return dict( start_frequency = start, stop_frequency = stop, number_of_points = npoints, power = power)
    def __del__(self):
        self.close()
