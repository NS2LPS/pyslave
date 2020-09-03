# VISA resource manager
try:
    from pyslave.instruments import __visa_rm__
except:
    __visa_rm__ = None

if __visa_rm__ is None:
    import visa
    __visa_rm__ = visa.ResourceManager()


from pydata import Spec
import time

class fsek:
    """Rohde&Schwarz Spectrum Analyzer (FSEK) driver.
    Direct call to the instrument invokes the fetch method.
    """
    __inst_type__ = 'spectro'
    __inst_id__ = 'Rohde&Schwarz FSEK 30'
    def __init__(self, resource, *args, **kwargs):
        self.instrument = __visa_rm__.open_resource(resource, *args, **kwargs)
        self.__class__.__call__ = self.__class__.fetch
        self.instrument.write('FORMAT REAL,32')
    def fetch(self, channel=1):
        """Fetch the trace from the specified channel and return it as a data object."""
        fstart = float(self.instrument.query('FREQ:START?'))
        fstop = float(self.instrument.query('FREQ:STOP?'))
        data = self.instrument.query_binary_values('TRAC? TRACE{0}'.format(channel))
        return Spec(S=data, start_frequency=fstart, stop_frequency=fstop, number_of_points=len(data))
    # def set_startfrequency(self,fstart)
        # self.instrument.write('FREQ:STOP {0}GHZ'.format(fstart)
    # def set_stopfrequency(self,fstop)
        # self.instrument.write('FREQ:STOP {0}GHZ'.format(fstop)
    # def get_sweeptime()
        # return self.instrument.query(':SWE:TIME?')
    def __del__(self):
        self.instrument.close()
