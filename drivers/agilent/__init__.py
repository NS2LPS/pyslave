"""Agilent devices are suppported via their IVI drivers. See the Python IVI documentation."""
from ivi.agilent import agilent34401A as __agilent34401A__
from ivi.agilent import agilentE3641A as __agilentE3641A__

class agilent34401A(__agilent34401A__):
    def __call__(self, max_time=1):
        """Read a measurement and return its value."""
        return self.measurement.read(max_time)

class agilentE3641A(__agilentE3641A__):
    def __call__(self, value, output=0):
        """Set the voltage of the specified output."""
        self.outputs[output].voltage_level = value 
