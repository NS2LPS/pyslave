import numpy as np
import time
from pydata import Sij, Data
import warnings

# VISA resource manager
try:
    from pyslave.instruments import __visa_rm__
except:
    __visa_rm__ = None

if __visa_rm__ is None:
    try:
        import pyvisa as visa
        __visa_rm__ = visa.ResourceManager()
    except:
        __visa_rm__ = None

from .__zvb__ import myrszvb 

class zva(myrszvb.rszvb):
    """Rohde&Schwarz Vector Network Analyzer (ZVA) driver.
    Includes some functions from the R&S DLL as well as home made functions.
    Direct call to the instrument invokes the fetch method.
    """
    __inst_type__ = 'vna'
    __inst_id__ = 'Rohde&Schwarz ZVA'
    def __init__(self, resource, *args, **kwargs):
        self.instrument = __visa_rm__.open_resource(resource, *args, **kwargs)
        self.__class__.__call__ = self.__class__.fetch
        self.close = self.instrument.close
        self.write = self.instrument.write
        self.query = self.instrument.query
        self.read = self.instrument.read
        self.write('FORM REAL ,32')
    
    def fetch(self, channel=1, refresh_parameters=True):
        """Fetch the trace from the specified channel and return it as a Sij data object.
        
        :param channel: Channel number, defaults to 1
        :param refresh_parameters: Refresh the VNA parameters before saving, defaults to True"""
        data = self.TraceResponseData(channel)
        if refresh_parameters : self.refresh_parameters(channel)
        return Sij( Sij = data, **self.__acquisition_parameters__ )
    
    def fetch_cw(self, channel=1, refresh_parameters=True):
        """Fetch the trace from the specified channel and return it as a data object.
        
        :param channel: Channel number, defaults to 1
        :param refresh_parameters: Refresh the VNA parameters before saving, defaults to True"""
        data = self.TraceResponseData(channel)
        if refresh_parameters : self.refresh_parameters_cw(channel)
        return Data( Sij = data, **self.__acquisition_parameters__ )        
    
    def fetch_raw(self, channel=1):
        """Fetch the trace from the specified channel and return it as a complex array.
        
        :param channel: Channel number, defaults to 1"""
        return self.TraceResponseData(channel)
    def fetch_segments(self, nsegments, npoints, channel=1):
        """Fetch the segemented trace from the specified channel and return it as a complex array.
        
        :param nsegments: Number of segments
        :param npoints: Number of points per sweep segment
        :param channel: Channel number, defaults to 1"""
        data = self.TraceResponseData(channel).reshape(nsegments,npoints,2)
        return data

    def wait_for_average(self, channel=1, sleeptime=0.5):
        """Blocks until the enough traces are acquired to perform the average.
        
        :param channel: Channel number, defaults to 1
        :param sleeptime: Polling interval, defaults to 0.5"""
        n_average = self.GetAverageFactor(channel)
        time.sleep(sleeptime)
        while self.GetCurrentSweep(channel)<n_average :
            time.sleep(sleeptime)

    def acquisition_parameters(self, channel = 1):
        """Return the acquisition parameters for the specified channel.
        
        :param channel: Channel number, defaults to 1"""
        start = self.GetStartFrequency(channel)
        stop = self.GetStopFrequency(channel)
        npoints = self.GetSweepNumberOfPoints(channel)
        power = self.GetPower(channel)
        rbw = self.GetMeasBandwidth(channel)
        return dict( start_frequency = start, stop_frequency = stop, number_of_points = npoints, power = power, rbw = rbw )
    
    def acquisition_parameters_cw(self, channel = 1):
        """Return the acquisition parameters for the specified channel.

        :param channel: Channel number, defaults to 1"""
        npoints = self.GetSweepNumberOfPoints(channel)
        power = self.GetPower(channel)
        rbw = self.GetMeasBandwidth(channel)
        sweeptime = self.GetSweepTime(channel)
        freq = self.GetCWFrequency(channel)
        return dict( number_of_points = npoints, power = power, rbw=rbw, sweeptime=sweeptime, freq=freq)
    
    def refresh_parameters(self, channel = 1):
        """Refresh the acquisition paramters and store them
        
        :param channel: Channel number, defaults to 1"""
        self.__acquisition_parameters__ = self.acquisition_parameters(channel)
    
    def refresh_parameters_cw(self, channel = 1):
        """Refresh the acquisition paramters and store them
        
        :param channel: Channel number, defaults to 1"""
        self.__acquisition_parameters__ = self.acquisition_parameters_cw(channel)
    
    def __del__(self):
        try:
            self.close()
        except:
            pass

class zvb(zva):
    """Rohde&Schwarz Vector Network Analyzer (ZVB) driver.
    Includes some functions from the R&S DLL as well as home made functions.
    Direct call to the instrument invokes the fetch method.
    """
    __inst_id__ =  'Rohde&Schwarz ZVB'
    def wait_for_average(self, channel=1, sleep_time=0.5):
        """Not implemented in ZVB.
        """
        warnings.warn("The wait_for_average method is not implemented.")

class znd(zva):
    """Rohde&Schwarz Vector Network Analyzer (ZND) driver.
    Includes some functions from the R&S DLL as well as home made functions.
    Direct call to the instrument invokes the fetch method.
    """
    __inst_id__ =  'Rohde&Schwarz ZND'
