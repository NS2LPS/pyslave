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


class Agilent33250A:
    """Agilent 33250A instrument driver.
    Direct call to the instrument sets the amplitude.
    """
    __inst_type__ = 'gen'
    __inst_id__ = 'Agilent Technologies 33250A'
    def __init__(self, resource, *args, **kwargs):
        self.instrument = __visa_rm__.open_resource(resource, *args, **kwargs)
        self.__class__.__call__ = self.__class__.setamplitude
        self.close = self.instrument.close

    def setamplitude(self, value):
        """Set the amplitude (Vpp)
        SCPI : AMPL value"""
        self.instrument.write('AMPL {0}'.format(value))

    def setoffset(self,value):
        """Set the offset (V)
        SCPI : VOLT:OFFS value"""
        self.instrument.write('VOLT:OFFS {0}'.format(value))

    def setfrequency(self, value):
        """Set the frequency (Hz)
        SCPI : FREQ value"""
        self.instrument.write('FREQ {0}'.format(value))

    def geterror(self):
        """Read last error.
        SCPI : SYST:ERR?"""
        return self.instrument.ask('SYST:ERR?')

    def output(self,val):
        """Turn the output on or off
        SCPI : OUPT ON or OUTP OFF"""
        self.instrument.write('OUTP {0}'.format('ON' if val else 'OFF'))

    def loadarb(self,wfm):
        """Load arbitrary waveform into volatile memory.
        Values ot the wfm array must be between -2047 and +2047, which corresponds
        to the DAC range. This maximum range is -10V and +10V or -5V to +5V
        depending on the output impedance.
        SCPI : DATA:DAC VOLATILE, #len(l),l,wfm"""
        wfm = wfm.astype('int16')
        l = str(2*len(wfm))
        self.instrument.write_raw('DATA:DAC VOLATILE, #{0}{1}{2}'.format(len(l),l,wfm.byteswap().tostring()))
