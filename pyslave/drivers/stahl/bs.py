import serial
import time
import numpy as np

class BSException(BaseException):
    pass

class BS(serial.Serial):
    __inst_type__ ='dcpwr'
    __inst_id__ = 'Stahl BS'
    def __init__(self, comport):
        super(BS, self).__init__(comport, baudrate=115200, timeout=1.0)
        self.write(b'IDN\r')
        ans = self.read_until(b'\r')
        self.__id__ = ans[:5]
        self.__class__.__call__ = self.__class__.ramp
        self.points_per_second = 60
            
    def __send__(self, val):
        val = self.__id__ + b' ' + val.encode() + b'\r'
        #print(val)
        self.write(val)
        ans = self.read_until(b'\r')
        return ans.strip()
        
    def setvoltage(self, ch, voltage):
        """Set the voltage between -10 V to +10 V on the specified channel"""
        assert type(ch)==int and ch>=1 and ch<=16
        val = (voltage+10.)/20.
        val = min(val,1.)
        val = max(val,0.)
        val = 'CH{0:02d} {1:1.5f}'.format(ch, val)
        try:
            ans = self.__send__(val)
            assert ans==b'\x06'
        except:
            self.flush()
            self.reset_input_buffer()
            ans = self.__send__(val)
            if ans!=b'\x06':
                raise BSException('Error while setting voltage')
    
    def getvoltage(self, ch):
        """Get the voltage of the specified channel"""
        assert type(ch)==int and ch>=1 and ch<=16
        val = 'U{0:02d}'.format(ch)
        try:
            out = self.__send__(val)
            res = float(out.replace(b',',b'.').replace(b'V',b'').strip())
        except:
            self.flush()
            self.reset_input_buffer()
            out = self.__send__(val)
            res = float(out.replace(b',',b'.').replace(b'V',b'').strip())            
        return res    
        
    def getcurrent(self, ch):
        """Get the voltage of the specified channel"""
        assert type(ch)==int and ch>=1 and ch<=16
        val = 'I{0:02d}'.format(ch)
        try:
            out = self.__send__(val)
            res = float(out.replace(b',',b'.').replace(b'mA',b'').strip())
        except:
            self.flush()
            self.reset_input_buffer()
            out = self.__send__(val)
            res = float(out.replace(b',',b'.').replace(b'mA',b'').strip())
        return res    
        
    # Ramp output
    def ramp(self, ch, value, slope=0.1):
        '''
        Ramp the output value of the given channel at the given slope.

        :param value: Desired final output value in V
        :param slope: Desired slope in V/s 
        '''
        assert type(ch)==int and ch>=1 and ch<=16
        current_value = self.getvoltage(ch)
        if value==current_value : return
        npoints = int(np.ceil(abs(value-current_value)/slope * self.points_per_second)) + 1
        ramp = np.linspace(current_value, value, npoints )[1:]
        for v in ramp:
            self.setvoltage(ch, v)
        
    def __repr__(self):
        res = 'Stahl BS '+self.__id__.decode()+'\n'
        for j in range(1,17):
            v = self.getvoltage(j)
            i = self.getcurrent(j)
            res += 'CH{0:02d} {1:+1.3f} V {2:+1.3f} mA\n'.format(j,v,i)
        return res
        
 