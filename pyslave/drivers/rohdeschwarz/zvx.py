import numpy as np
import time
from pydata import Sij, Data
import warnings

from .__zvb__ import rszvb as dll

class zva:
    """Rohde&Schwarz Vector Network Analyzer (ZVA) driver.
    All the functions from the rszvb DLL are available as well as extra home made functions.
    Direct call to the instrument invokes the fetch method.
    """
    __inst_type__ = 'vna'
    __inst_id__ = 'Rohde&Schwarz ZVA'
    def __init__(self, address):
        self.iHandle = dll.rszvb_init(address.encode(), 0, 0)
        self.__class__.__call__ = self.__class__.fetch
    def __getattr__(self, name):
        dll_fun = getattr(dll, 'rszvb_' + name)
        def fun(*args, **kwargs):
            res = dll_fun(self.iHandle, *args, **kwargs)
            if dll_fun.output : return res
        return fun
    def fetch(self, channel=1, refresh_parameters=True):
        """Fetch the trace from the specified channel and return it as a Sij data object."""
        n = self.GetSweepNumberOfPoints(channel)
        data = np.empty((n, 2), np.float64)
        r = self.TraceResponseData(channel,0,data)
        if r!=2*n : raise dll.ZVBDLLERROR("TraceResponseData : missing data points.")
        if refresh_parameters : self.refresh_parameters(channel)
        return Sij( Sij = data[:,0] + 1j*data[:,1], **self.__acquisition_parameters__ )
    def fetch_cw(self, channel=1, refresh_parameters=True):
        """Fetch the trace from the specified channel and return it as a data object."""
        n = self.GetSweepNumberOfPoints(channel)
        data = np.empty((n, 2), np.float64)
        r = self.TraceResponseData(channel,0,data)
        if r!=2*n : raise dll.ZVBDLLERROR("TraceResponseData : missing data points.")
        if refresh_parameters : self.refresh_parameters_cw(channel)
        return Data( Sij = data[:,0] + 1j*data[:,1], **self.__acquisition_parameters__ )        
    def fetch_raw(self, channel=1):
        """Fetch the trace from the specified channel and return it as a complex array."""
        n = self.GetSweepNumberOfPoints(channel)
        data = np.empty((n, 2), np.float64)
        r = self.TraceResponseData(channel,0,data)
        if r!=2*n : raise dll.ZVBDLLERROR("TraceResponseData : missing data points.")
        return data[:,0] + 1j*data[:,1]
    def fetch_segments(self, nsegments, npoints, channel=1):
        n = nsegments*npoints
        data = np.empty((n, 2), np.float64)
        r = self.TraceResponseData(channel,0,data)
        if r!=2*n : raise dll.ZVBDLLERROR("TraceResponseData : missing data points.")
        data = data.reshape((nsegments,npoints,2))
        return data[:,:,0] + 1j*data[:,:,1]
    def wait_for_average(self, channel=1, sleep_time=0.5):
        """Blocks until the enough traces are acquired to perform the average."""
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
        rbw = self.GetMeasBandwidth(channel)
        return dict( start_frequency = start, stop_frequency = stop, number_of_points = npoints, power = power, rbw = rbw )
    def acquisition_parameters_cw(self, channel = 1):
        """Return the acquisition parameters for the specified channel."""
        npoints = self.GetSweepNumberOfPoints(channel)
        power = self.GetPower(channel)
        rbw = self.GetMeasBandwidth(channel)
        sweeptime = self.GetSweepTime(channel)
        freq = self.GetCWFrequency(channel)
        return dict( number_of_points = npoints, power = power, rbw=rbw, sweeptime=sweeptime, freq=freq)
    def refresh_parameters(self, channel = 1):
        """Refresh the acquisition paramters and store them"""
        self.__acquisition_parameters__ = self.acquisition_parameters(channel)
    def refresh_parameters_cw(self, channel = 1):
        """Refresh the acquisition paramters and store them"""
        self.__acquisition_parameters__ = self.acquisition_parameters_cw(channel)
    def __del__(self):
        try:
            self.close()
        except:
            pass

class zvb(zva):
    """Rohde&Schwarz Vector Network Analyzer (ZVB) driver.
    All the functions from the rszvb DLL are available as well as extra home made functions.
    Direct call to the instrument invokes the fetch method.
    """
    __inst_id__ =  'Rohde&Schwarz ZVB'
    def wait_for_average(self, channel=1, sleep_time=0.5):
        """Not implemented in ZVB."""
        warnings.warn("The wait_for_average method is not implemented.")

class znd(zva):
    """Rohde&Schwarz Vector Network Analyzer (ZND) driver.
    All the functions from the rszvb DLL are available as well as extra home made functions.
    Direct call to the instrument invokes the fetch method.
    """
    __inst_id__ =  'Rohde&Schwarz ZND'
