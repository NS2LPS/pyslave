# VISA resource manager
try:
    from pyslave.instruments import __visa_rm__
except:
    __visa_rm__ = None

if __visa_rm__ is None:
    import visa
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
        res = self.instrument.query('READ?')
        return float(res)
