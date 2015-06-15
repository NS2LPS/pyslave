"""Agilent devices are suppported via their IVI drivers. See the Python IVI documentation."""
from ivi.agilent import agilent34401A
from ivi.agilent import agilentE3641A as __agilentE3641A__

class agilentE3641A(__agilentE3641A__):
    def __call__(self, max_time=1):
        return dmm1.measurement.read(max_time)
