Rohde Schwarz instrument drivers
================================

.. automodule:: pyslave.drivers.rohdeschwarz

.. autoclass:: pyslave.drivers.rohdeschwarz.zvb.zvb
    
    .. method:: fetch(self, channel=1)    
    
        Fetch the trace from the specified channel and return it as a numpy array with two columns (real and imaginary parts).
    
    .. method:: freq(self) 
    
        Return the frequency vector corresponding to the last acquired trace.
    
    .. method:: acquisition_parameters(self, channel = 1)
    
        Return the acquisition parameters for the specified channel.
    
    .. include:: ./txt/rszvb.txt
    

