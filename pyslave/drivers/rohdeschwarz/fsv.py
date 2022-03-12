import numpy as np
import time
from pydata import Spec

# VISA resource manager
try:
    from pyslave.instruments import __visa_rm__
except:
    __visa_rm__ = None

if __visa_rm__ is None:
    import pyvisa as visa
    __visa_rm__ = visa.ResourceManager()


class fsv:
    """Rohde&Schwarz Spectrum analyzer (FSV) driver.
    Direct call to the instrument invokes the fetch method.
    """
    __inst_type__ = 'spectro'
    __inst_id__ = 'Rohde&Schwarz FSV3013'
    def __init__(self, resource, *args, **kwargs):
        self.instrument = __visa_rm__.open_resource(resource, *args, **kwargs)
        self.__class__.__call__ = self.__class__.fetch
        self.instrument.write('FORM REAL,32')
    def __del__(self):
        self.instrument.close()
    def write(self, *args, **kwargs):
        return self.instrument.write(*args,**kwargs)
    def query(self, *args, **kwargs):
        return self.instrument.query(*args,**kwargs)
    def query_binary_values(self, *args, **kwargs):
        return self.instrument.query_binary_values(*args,**kwargs)        
    def fetch(self, window=1, trace=1, refresh_parameters=True):
        """Fetch the trace from the specified window and return it as a data object."""
        data = self.fetch_raw(window, trace)
        if refresh_parameters : self.refresh_parameters()
        res = Spec( S = data, **self.__acquisition_parameters__ )
        res['number_of_points'] = len(data)
        return res
    def fetch_raw(self, window=1, trace=1):
        """Fetch the trace from the specified window and return it as an array."""
        return self.query_binary_values(f'TRAC{window}? TRACE{trace}',container=np.array)    
    def fetch_x(self, window=1, trace=1):
        """Fetch the x axis of the trace from the specified window and return it as an array."""
        return self.query_binary_values(f'TRAC{window}:X? TRACE{trace}',container=np.array)    
    def acquisition_parameters(self):
        """Return the acquisition parameters."""
        fstart = float(self.instrument.query('FREQ:START?'))
        fstop = float(self.instrument.query('FREQ:STOP?'))
        rbw = float(self.instrument.query('BAND:RES?'))
        vbw = float(self.instrument.query('BAND:VID?'))
        count = int(self.instrument.query('SWE:COUNT?'))
        typ = self.instrument.query('SWE:TYPE?')
        det = self.instrument.query('DET?')
        aver = int(self.instrument.query('AVER?'))
        unit = self.instrument.query('CALC:UNIT:POW?')
        rlev = self.instrument.query('DISP:TRAC:Y:RLEV?')    
        return dict( start_frequency = fstart, stop_frequency = fstop, rlev=rlev, rbw = rbw, vbw = vbw, count = count, typ = typ.strip(), det=det.strip(), aver=aver, unit=unit.strip() )
    def refresh_parameters(self):
        """Refresh the acquisition paramters and store them"""
        self.__acquisition_parameters__ = self.acquisition_parameters()

