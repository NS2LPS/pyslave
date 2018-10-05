"""Some Agilent devices are supported via their IVI drivers. See the Python IVI documentation."""
from ivi.agilent import agilent34401A as __agilent34401A__
from ivi.agilent import agilentE3641A as __agilentE3641A__

__drivers__ = {'HEWLETT-PACKARD 34401A' : 'agilent.agilent34401A',
               'Agilent Technologies 34410A' : 'agilent.agilent34401A',
               'HEWLETT-PACKARD E3631A' : 'agilent.agilentE3641A',
               'Agilent Technologies 33250A' : 'agilent.agilent33250A.agilent33250A',}

class agilent34401A(__agilent34401A__):
    __inst_type__ = 'dmm'
    __inst_id__ = 'Agilent Technologies 34410A'
    def __call__(self, max_time=1):
        """Read a measurement and return its value."""
        return self.measurement.read(max_time)

class agilentE3641A(__agilentE3641A__):
    __inst_type__ = 'dcpwr'
    __inst_id__ = 'HEWLETT-PACKARD E3631A'
    def __call__(self, value, output=0):
        """Set the voltage of the specified output."""
        self.outputs[output].voltage_level = value
