import rszvb as dll
import numpy as np

class zvb:
    def __init__(self, address):
        self.iHandle = dll.rszvb_init(address, 1, 0)
    def __getattr__(self, name):
        dll_fun = getattr(dll, 'rszvb_' + name)
        def fun(*args, **kwargs):
            res = dll_fun(self.iHandle, *args, **kwargs)
            if dll_fun.output : return res
        return fun
    def fetch(self, channel=1):
        n = self.GetSweepNumberOfPoints(channel)
        data = np.empty((n, 2), np.float64)
        r = self.TraceResponseData(channel,0,data)
        if r!=2*n : raise dll.ZVBDLLERROR("TraceResponseData : missing data points.")
        return data
    def wait_for_average(self, channel=1, sleep_time=0.1):
        n_average = zva.GetAverageFactor()
        while zva.GetCurrentSweep(channel)<n_average :
            time.sleep(sleep_time)
    def freq(self, channel=1):
        start = self.GetStartFrequency(channel)
        stop = self.GetStopFrequency(channel)
        npoints = self.GetSweepNumberOfPoints(channel)
        return np.linspace(start, stop, npoints)
    def get_sweep_parameters(self, channel = 1):
        start = self.GetStartFrequency(channel)
        stop = self.GetStopFrequency(channel)
        npoints = self.GetSweepNumberOfPoints(channel)
        power = self.GetPower(channel)
        return dict( start_frequency = start, stop_frequency = stop, number_of_points = npoints, power = power)
    def copy_sweep_parameters(self, d, channel = 1):
        for k,v in self.get_sweep_parameters(channel).iteritems() :
            d[k] = v
    def __del__(self):
        self.close()
