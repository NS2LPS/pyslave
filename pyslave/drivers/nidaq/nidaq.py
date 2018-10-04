try:
    import PyDAQmx as ni
except:
    print("DAQmx library could not be loaded")
    
import ctypes
import numpy as np

class nidaq_generic_ao:
    """Class for NI-DAQ analog output boards.
    Direct call to the object invokes the out method."""
    __inst_type__ = 'ao'
    __inst_id__ = 'NIDAQ analog outputs'
    def __init__(self, devname, reset=True):
        self.devname = devname
        # Reset device
        if reset : ni.DAQmxResetDevice(devname)
        # Get output names
        buffer = ctypes.create_string_buffer('',1024)
        ni.DAQmxGetDeviceAttribute(devname, ni.DAQmx_Dev_AO_PhysicalChans, buffer, 1024)
        self.ao = [x.strip() for x in buffer.value.split(',')]
        self.__class__.__call__ = self.__class__.out

    def out(self, voltage, output=1):
        """Output a DC voltage on the specified output."""
        task = ni.Task()
        if voltage>0:
            rmin, rmax = 0, voltage
        elif voltage < 0:
            rmin, rmax = voltage, 0
        else:
            rmin, rmax = 0, 1e-3
        task.CreateAOVoltageChan(self.ao[output-1], "", rmin, rmax, ni.DAQmx_Val_Volts, None)
        task.WriteAnalogScalarF64(True, 1, voltage, None)
        task.ClearTask()


class nidaq_generic_ai:
    """Class for NI-DAQ analog input boards.
    Direct call to the object invokes the read method."""
    __inst_type__ = 'ai'
    __inst_id__ = 'NIDAQ analog inputs'
    def __init__(self, devname, reset=True):
        self.devname = devname
        # Reset device
        if reset : ni.DAQmxResetDevice(devname)
        # Get output names
        buffer = ctypes.create_string_buffer('',1024)
        ni.DAQmxGetDeviceAttribute(devname, ni.DAQmx_Dev_AI_PhysicalChans, buffer, 1024)
        self.ai = [x.strip() for x in buffer.value.split(',')]
        self.__class__.__call__ = self.__class__.read

    def read(self, output=1, sampling_rate=1000, Nsamples=100, vmin=-10, vmax=10):
        """Sample the specified output."""
        task = ni.Task()
        task.CreateAIVoltageChan( self.ai[output-1], "", ni.DAQmx_Val_Cfg_Default, vmin, vmax, ni.DAQmx_Val_Volts, None)
        task.CfgSampClkTiming("", sampling_rate, ni.DAQmx_Val_Rising, ni.DAQmx_Val_FiniteSamps, Nsamples)
        task.StartTask()
        read = ctypes.c_int()
        data = np.zeros(Nsamples)
        task.ReadAnalogF64(Nsamples, -1, ni.DAQmx_Val_GroupByScanNumber, data, Nsamples, ctypes.byref(read), None)
        task.ClearTask()
        return data
