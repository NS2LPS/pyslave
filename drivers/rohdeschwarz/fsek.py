import visa

# VISA resource manager
visa_rm = visa.ResourceManager()

from pyslave.data import Spec


class fsek:
    """Rohde&Schwarz Spectrum Analyzer (FSEK) driver.
    Direct call to the instrument invokes the fetch method.
    """
    __inst_type__ = 'spectro'
    __inst_id__ = 'Rohde&Schwarz FSEK 30'
    def __init__(self, resource, *args, **kwargs):
        self.instrument = visa_rm.open_resource(resource, *args, **kwargs)
        self.__call__ = self.fetch
    def fetch(self, channel=1):
        """Fetch the trace from the specified channel and return it as a Sij data object."""
        fstart = float(self.instrument.query('FREQ:START?'))
        fstop = float(self.instrument.query('FREQ:STOP?'))
        data = self.instrument.query_ascii_values('TRAC? TRACE{0}'.format(channel))
        return Spec(S=data, start_frequency=fstart, stop_frequency=fstop, number_of_points=len(data))
    def __del__(self):
        self.instrument.close()
