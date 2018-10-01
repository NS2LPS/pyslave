import numpy as np
import visa

# VISA resource manager
visa_rm = visa.ResourceManager()


class PM6681:
    """Fluke PM6681 instrument driver.
    Direct call to the instrument invokes the outp method.
    """
    __inst_id__ = 'PHILIPS  PM6681'
    __inst_type__ = 'counter'
    def __init__(self, resource, *args, **kwargs):
        self.instrument = visa_rm.open_resource(resource, *args, **kwargs)

    def fastmode(self):
        #Set fast mode : up to ~ 1000 counts/s
        self.write(':FORM REAL;')
        self.write(':ACQ:APER MIN;')
        self.write(':AVER:STAT OFF;')
        self.write(':INP:LEV:AUTO OFF;')        # Gain 70 ms
        self.write(':DISP:ENAB OFF;')
        self.write(':INT:FORM PACK;')           # Gain 1.2 ms
        self.write(':SENS:ACQ:RES LOW;')
        self.write(':FORM:TINF OFF;')
        self.write(':STAT:OPER:ENAB 1;')

    def normalmode(self):
        #Set normal mode : up to ~ 100 counts/s
        self.write(':FORM REAL;')
        self.write(':ACQ:APER MIN;')
        self.write(':AVER:STAT OFF;')
        self.write(':INP:LEV:AUTO OFF;')
        self.write(':DISP:ENAB ON;')
        self.write(':INT:FORM REAL;')
        self.write(':SENS:ACQ:RES HIGH;')
        self.write(':FORM:TINF OFF;')
        self.write(':STAT:OPER:ENAB 1;')

    def set_counts(self, n):
        self.write(':TRIG:COUN {0};:ARM:COUN 1'.format(n))
        self.counts = n

    def start(self):
        self.write(':ABORT;:INIT')

    def fetch(self):
        self.write(':FETCH:ARR? {0}'.format(self.counts))
        res = self.instrument.read_raw()
        res = np.fromstring(res, dtype='c,c,c,>d,c')['f3']
        return res


    def write(self, str):
        self.instrument.write(str)

    def query(self, str):
        return self.instrument.query(str)

    def close(self):
        self.instrument.close()
