class controle:
    def __init__(self, reset=False):
        # Reset device
        if reset : ni.DAQmxResetDevice("Dev1")
        self.voltage = 0.
        # Zero output
        aout = ni.Task()
        self.__add_ao__(aout, 'ao1')
        aout.WriteAnalogScalarF64(True, 1, 0, None)
        aout.ClearTask()
        aout = ni.Task()
        self.__add_ao__(aout, 'ao2')
        aout.WriteAnalogScalarF64(True, 1, 0, None)
        aout.ClearTask()
        # Read buffer
        self.data = []
        self.delay = 5e-6
        self.frequency=100
        self.sampling_rate=1e6
        #pulse
        self.pulse_length = int(self.sampling_rate/self.frequency)
        self.Nsamples = self.pulse_length
        self.data = np.zeros(self.Nsamples)

    def inittask(self):
        # Create analog output task for pulse
        self.aout = ni.Task()
        self.__add_ao__(self.aout, 'ao1')
        # Create analog input task
        self.ain = ni.Task()
        self.__add_ai__(self.ain, 'ai5')
        # Create analog output task for power controle
        self.aout_p = ni.Task()
        self.__add_ao__(self.aout_p, 'ao2')
        # Trigger
        self.aout.CfgDigEdgeStartTrig("/Dev1/ai/StartTrigger", ni.DAQmx_Val_Rising)
        self.sampling_rate = int(self.sampling_rate)
        self.aout.CfgSampClkTiming("", self.sampling_rate, ni.DAQmx_Val_Rising, ni.DAQmx_Val_ContSamps, self.Nsamples )
        self.ain.CfgSampClkTiming("", self.sampling_rate, ni.DAQmx_Val_Rising, ni.DAQmx_Val_ContSamps, self.Nsamples)
        #self.aout_p.CfgSampClkTiming("", self.sampling_rate, ni.DAQmx_Val_Rising, ni.DAQmx_Val_ContSamps, self.Nsamples)

    @staticmethod
    def __add_ai__(task, channel, min = 0, max = 10):
        task.CreateAIVoltageChan( "Dev1/"+channel, "", ni.DAQmx_Val_Cfg_Default, min, max, ni.DAQmx_Val_Volts, None)

    @staticmethod
    def __add_ao__(task, channel, min = 0, max = 10):
        task.CreateAOVoltageChan("Dev1/"+channel, "", min, max, ni.DAQmx_Val_Volts, None)

    def pulse(self, lowvalue, highvalue, duty_cycle):
        # Create pulse
        nhigh = int( self.pulse_length * duty_cycle )
        pulse_vector = np.r_[ np.ones( nhigh )*highvalue, np.ones( self.pulse_length-nhigh )*lowvalue ]
        self.pulse_vector = pulse_vector
        self.index = np.arange(int( self.delay*self.sampling_rate), nhigh)
        self.indexb= np.arange(nhigh +int(self.delay*self.sampling_rate), self.pulse_length)
        # Trigger
        written = ni.c_int()
        try:
            devnull = open(os.devnull, 'w')
            with RedirectStdStreams(stdout=devnull, stderr=devnull):
                self.aout.WriteAnalogF64(self.Nsamples, False, -1, ni.DAQmx_Val_GroupByChannel, pulse_vector, ni.byref(written), None)
        except:
            pass
        time.sleep(0.2)

    def pulse_high(self, value):
        self.aout_p.WriteAnalogScalarF64(True, 1, value, None)
        time.sleep(0.2)


    def starttask(self):
        self.aout.StartTask()
        self.ain.StartTask()
        self.aout_p.StartTask()

    def read(self, stats=False):
        data = self.data
        read = ni.c_int()
        try:
            self.ain.ReadAnalogF64(len(data), -1, ni.DAQmx_Val_GroupByScanNumber, data, len(data), ni.byref(read), None)
        except:
            pass
        high_level = self.data[self.index]
        low_level = self.data[self.indexb]
        res = high_level.mean() - low_level.mean()
        if stats:
            stats = {'min_high_level': high_level.min(),
                     'max_high_level': high_level.max(),
                     'min_low_level':  low_level.min(),
                     'max_low_level': low_level.max(),
                     'mean_low_level': low_level.mean(),
                     'mean_high_level': high_level.mean(),
                     'std_high_level' : high_level.std(),
                     'std_low_level' : low_level.std(),
                     }
            return res, stats
        return res


    def stop(self):
        try:
            self.ain.StopTask()
            self.ain.ClearTask()
        except:
            pass
        self.aout.StopTask()
        self.aout.ClearTask()
        self.aout_p.StopTask()
        self.aout_p.ClearTask()
        #put laser to zero
        aout = ni.Task()
        self.__add_ao__(aout, 'ao1')
        aout.WriteAnalogScalarF64(True, 1, 0, None)
        aout.ClearTask()
        aout = ni.Task()
        self.__add_ao__(aout, 'ao2')
        aout.WriteAnalogScalarF64(True, 1, 0, None)
        aout.ClearTask()
    
