
import visa

# VISA resource manager
visa_rm = visa.ResourceManager()


class Keithley2700:
    """Keithley 2700 instrument driver.
    Direct call to the instrument invokes the read method.
    """
    __inst_id__ = 'KEITHLEY INSTRUMENTS INC. MODEL 2700'
    __inst_type__ = dmm
    def __init__(self, resource, *args, **kwargs):
        self.instrument = visa_rm.open_resource(resource, *args, **kwargs)
        self.__call__ = self.read

    def read(self):
        res = self.instrument.ask('DATA?')
        return float(res.split(',')[0][:-3])
