from __zvb__ import rszvb as dll
import numpy as np

class zvb:
    """Rohde&Schwarz Vector Network Analyzer (ZVA,ZVB) driver.
    All the functions from the rszvb DLL are available.
    See the DLL help in the ./__zvb__ directory.
        Example : zvb.SetPower(channel=1, power=-10)
    The channel keyword argument is set to 1 by default.
    """
    def __init__(self, address):
        self.iHandle = dll.rszvb_init(address, 1, 0)
    def __getattr__(self, name):
        dll_fun = getattr(dll, 'rszvb_' + name)
        def fun(*args, **kwargs):
            res = dll_fun(self.iHandle, *args, **kwargs)
            if dll_fun.output : return res
        return fun
    def fetch(self, channel=1):
        """Retrieve data from the specified channel.
        Data are returned as a numpy two column vector."""
        n = self.GetSweepNumberOfPoints(channel)
        data = np.empty((n, 2), np.float64)
        r = self.TraceResponseData(channel,0,data)
        if r!=2*n : raise dll.ZVBDLLERROR("TraceResponseData : missing data points.")
        return data
    def wait_for_average(self, channel=1, sleep_time=0.1):
        """Broken function."""
        n_average = self.GetAverageFactor(channel)
        while self.GetCurrentSweep(channel)<n_average :
            time.sleep(sleep_time)
    def freq(self, channel=1):
        """Get the start,stop frequency and number of points and generate the corresponding frequency vector."""
        start = self.GetStartFrequency(channel)
        stop = self.GetStopFrequency(channel)
        npoints = self.GetSweepNumberOfPoints(channel)
        return np.linspace(start, stop, npoints)
    def get_sweep_parameters(self, channel = 1):
        """Return the start,stop frequency and number of points for the specified channel."""
        start = self.GetStartFrequency(channel)
        stop = self.GetStopFrequency(channel)
        npoints = self.GetSweepNumberOfPoints(channel)
        power = self.GetPower(channel)
        return dict( start_frequency = start, stop_frequency = stop, number_of_points = npoints, power = power)
    def copy_sweep_parameters(self, hd5attrs, channel = 1):
        """Copy the sweep parameters (see get_sweep_parameters) to the dictionary (e.g. hd5 attributes)."""
        for k,v in self.get_sweep_parameters(channel).iteritems() :
            hd5attrs[k] = v
    def __del__(self):
        self.close()
