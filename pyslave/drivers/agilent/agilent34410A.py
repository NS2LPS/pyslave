# VISA resource manager
try:
    from pyslave.instruments import __visa_rm__
except:
    __visa_rm__ = None

if __visa_rm__ is None:
    import pyvisa as visa
    __visa_rm__ = visa.ResourceManager()



class Agilent34410A:
    """Agilent 34410A instrument driver.
    Direct call to the instrument invokes the read method.
    """
    __inst_type__ = 'dmm'
    __inst_id__ = 'Agilent Technologies 34410A'
    def __init__(self, resource, *args, **kwargs):
        self.instrument = __visa_rm__.open_resource(resource, *args, **kwargs)
        self.__class__.__call__ = self.__class__.read

    def read(self):
        """Acquire and return one value (blocking)"""
        res = self.instrument.query('READ?')
        return float(res)

    def fetch(self):
        """Wait for acquisition to finish and return one value (blocking)"""
        res = self.instrument.query('FETCH?')
        return float(res)

    def init(self):
        """Start acquiring one value (non-blocking). 
        Use fetch to retrieve the value."""
        self.instrument.write('INIT:IMM')
        
    def nplc(self, val):
        """Set voltage averaging time in number of power line cycles (20 ms)"""
        self.instrument.write(f'SENS:VOLT:DC:NPLC {val:d}')