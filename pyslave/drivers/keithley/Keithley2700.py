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



class Keithley2700:
    """Keithley 2700 instrument driver.
    Direct call to the instrument invokes the read method.
    """
    __inst_id__ = 'KEITHLEY INSTRUMENTS INC. MODEL 2700'
    __inst_type__ = dmm
    def __init__(self, resource, *args, **kwargs):
        self.instrument = __visa_rm__.open_resource(resource, *args, **kwargs)
        self.__class__.__call__ = self.__class__.read

    def read(self):
        """Read one value from the dmm.
        SCPI : DATA?"""
        res = self.instrument.ask('DATA?')
        return float(res.split(',')[0][:-3])
