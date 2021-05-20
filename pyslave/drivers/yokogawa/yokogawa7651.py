""" Filename: yokogawa7651.py

Original author: Steven Casagrande (stevencasagrande@gmail.com)
2012

This work is released under the Creative Commons Attribution-Sharealike 3.0 license.
See http://creativecommons.org/licenses/by-sa/3.0/ or the included license/LICENSE.TXT file for more information.

Attribution requirements can be found in license/ATTRIBUTION.TXT"""

import numpy as np
import time


# VISA resource manager
try:
    from pyslave.instruments import __visa_rm__
except:
    __visa_rm__ = None

if __visa_rm__ is None:
    import pyvisa as visa
    __visa_rm__ = visa.ResourceManager()



class yokogawa7651:
    __inst_type__ = 'dcpwr'
    __inst_id__ = 'Yokogawa 7651'
    """Yokogawa 7651 instrument driver.
    Direct call to the instrument invokes the ramp method."""
    def __init__(self, resource, *args, **kwargs):
        self.instrument = __visa_rm__.open_resource(resource, *args, **kwargs)
        self.value = 0
        self.points_per_second = 20
        self.__class__.__call__ = self.__class__.ramp

    def trigger(self):
        '''
        Triggering function for the Yokogawa 7651.

        After changing any parameters of the instrument (for example, output voltage), the device needs to be triggered before it will update.
        '''
        self.write('E;')

    # Set Voltage Range
    def setVoltageRange(self,value):
        '''
        Function changes the voltage range of the power supply.
        A float representing the desired voltage will have the range adjusted accordingly, or a string specifying the range will also work.

        :param value: Desired voltage or directly specified voltage range as a string (10mV, 100mV, 1V, 10V, 30V)
        '''
        try :
            value = abs(float(value))
        except ValueError:
            value = str(value)

        if type(value) is float:
            if value <= 10e-3:
                yokoRange = 2
            elif ( value > 10e-3 ) and ( value <= 100e-3 ):
                yokoRange = 3
            elif ( value > 100e-3 ) and ( value <= 1 ):
                yokoRange = 4
            elif ( value > 1 ) and ( value <= 10 ):
                yokoRange = 5
            else:
                yokoRange = 6
        elif type(value) is str :
            value = value.lower()
            valid = ['10mv','100mv','1v','10v','30v']
            if value not in valid:
                raise Exception('Allowed voltage range values are 10mV, 100mV, 1V, 10V and 30V.')
            else:
                yokoRange = valid.index(value) + 2

        self.write( 'R%i;' % (yokoRange) )
        self.trigger()

    # Set Current Range
    def setCurrentRange(self,value):
        '''
        Function changes the current range of the power supply.
        A float representing the desired current will have the range adjusted accordingly, or a string specifying the range will also work.

        :param value: Desired current or directly specified current range as a string (1mA, 10mA, 100mA)
        '''
        try :
            value = abs(float(value))
        except ValueError:
            value = str(value)

        if type(value) is float:
            if value <= 1.2e-3:
                yokoRange = 4
            elif ( value > 1.2e-3 ) and ( value <= 12e-3 ):
                yokoRange = 5
            else:
                yokoRange = 6
        elif type(value) == str:
            value = value.lower()
            valid = ['1ma','10ma','100ma']
            if value not in valid:
                raise Exception('Allowed current range values are 1mA, 10mA and 100mA.')
            else:
                yokoRange = valid.index(value) + 4

        self.write( 'R%i;' % (yokoRange) )
        self.trigger()

    # Set Function
    def setFunction(self,func):
        '''
        Set the output of the Yokogawa 7651 to either constant voltage or constant current mode.

        :param func: Desired mode as a string ('voltage' or 'current')
        '''
        if type(func) != type(str()):
            raise Exception('Parameter "func" must be a string.')

        func = func.lower()

        if func == 'voltage':
            setting = 1
        elif func == 'current':
            setting = 5
        else:
            raise Exception('Only allowed values are "voltage" and "current".')

        self.write( 'F%i;' % (setting) )
        self.trigger()

    # Set output value
    def setValue(self, value, autorange=True):
        '''
        Set the output value of the power supply.

        :param value: Desired constant output value in V or A
        :param autorange: If True, the instrument will automatically adapt its range to the value
        '''
        value = float(value)
        if autorange:
            self.write( 'SA%.10f;' % (value) )
        else:
            self.write( 'S%.10f;' % (value) )
        self.trigger()
        self.value = value


    # Output
    def setOutput(self,setting):
        '''
        Enable or disable the output of the Yokogawa 7651.

        :param setting: Specify the state of the power supply output (True or False).
        '''
        setting = '1' if setting else '0'
        self.write('O{0};'.format(setting))
        self.trigger()

    # Ramp output
    def ramp(self, value, slope=0.1):
        '''
        Ramp the output value of the power supply at the given slope.

        :param value: Desired final output value in V or A
        :param slope: Desired slope in V/s or A/s
        '''
        value = float(value)
        if value==self.value : return
        npoints = int(np.ceil(abs(value-self.value)/slope * self.points_per_second)) + 1
        ramp = np.linspace(self.value, value, npoints )[1:]
        for v in ramp:
            self.write( 'S%.10f;' % (v) )
            self.trigger()
        self.value = value

    def ready(self):
        """Blocks until the output is stabilized."""
        notready = int(self.query('OC;').strip('STS1=')) & 8
        while notready:
            notready = int(self.query('OC;').strip('STS1=')) & 8
            time.sleep(1./self.points_per_second)

    def write(self, str):
        self.instrument.write(str)

    def clear(self):
        self.instrument.clear()

    def query(self, str):
        return self.instrument.query(str)

    def close(self):
        self.instrument.close()
