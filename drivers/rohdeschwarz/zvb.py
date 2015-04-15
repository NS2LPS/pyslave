from __zvb__ import rszvb as dll
import numpy as np
import h5py
import time

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
    def fetch(self, channel=1):
        """Fetch the trace from the specified channel and return it as a numpy array with two columns (real and imaginary parts)."""
        n = self.GetSweepNumberOfPoints(channel)
        data = np.empty((n, 2), np.float64)
        r = self.TraceResponseData(channel,0,data)
        if r!=2*n : raise dll.ZVBDLLERROR("TraceResponseData : missing data points.")
        self.last_data = data
        self.last_acquisition_parameters = self.acquisition_parameters(channel)
        return data
    def __save_txt__(self):
        return np.c_[self.freq(), self.last_data]
    def __save_h5__(self):
        return self.last_data, self.last_acquisition_parameters
    def wait_for_average(self, channel=1, sleep_time=0.5):
        """Broken function."""
        n_average = self.GetAverageFactor(channel)
        time.sleep(sleep_time)
        while self.GetCurrentSweep(channel)<n_average :
            time.sleep(sleep_time)
    def freq(self):
        """Return the frequency vector corresponding to the last acquired trace."""
        start = self.last_acquisition_parameters['start_frequency']
        stop = self.last_acquisition_parameters['stop_frequency']
        npoints = self.last_acquisition_parameters['number_of_points']
        return np.linspace(start, stop, npoints)
    def acquisition_parameters(self, channel = 1):
        """Return the acquisition parameters for the specified channel."""
        start = self.GetStartFrequency(channel)
        stop = self.GetStopFrequency(channel)
        npoints = self.GetSweepNumberOfPoints(channel)
        power = self.GetPower(channel)
        return dict( start_frequency = start, stop_frequency = stop, number_of_points = npoints, power = power)
    def __del__(self):
        self.close()
