import serial
import time

class SynthHD(serial.Serial):
    __inst_type__ ='gen'
    __inst_id__ = 'Windfreak SynthHD'
    def __init__(self, comport):
        super(SynthHD, self).__init__(comport, baudrate=57600, timeout=1.0,
                                      parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                                      bytesize=serial.EIGHTBITS)

    def setfreq(self, channel, freq):
        self.write('C{0}f{1}'.format(channel,freq).encode())

    def setpower(self, channel, power):
        self.write('C{0}W{1}'.format(channel,power).encode())

    def setphase(self, channel, phase):
        self.write('C{0}~{1}'.format(channel,phase).encode())

    def getfreq(self, channel):
        self.flushInput()
        self.write('C{0}f?'.format(channel).encode())
        out = self.readline()
        return float(out.strip())

    def getphase(self, channel):
        self.flushInput()
        self.write('C{0}~?'.format(channel).encode())
        out = self.readline()
        return float(out.strip())

    def setbothfreq(self, freq):
        self.write('C0f{0}'.format(freq).encode())
        time.sleep(0.1)
        self.write('C1f{0}'.format(freq).encode())

    def getpower(self, channel):
        self.flushInput()
        self.write('C{0}W?'.format(channel).encode())
        out = self.readline()
        return float(out.strip())

    def getrfstatus(self, channel):
        self.flushInput()
        self.write('C{0}h?'.format(channel).encode())
        out = self.readline()
        return int(out.strip())

    def mute(self,channel, val):
        val = 0 if val else 1
        self.write('C{0}h{1}\r\n'.format(channel,val).encode())

    def __repr__(self):
        f0 = self.getfreq(0)
        p0 = self.getpower(0)
        m0 = self.getrfstatus(0)
        s0 = 'Channel A : {0:6.1f} MHz  |  {1:+5.1f} dBm  | RF {2}\n'.format(f0,p0, 'ON' if m0 else 'OFF').encode()
        f0 = self.getfreq(1)
        p0 = self.getpower(1)
        m0 = self.getrfstatus(1)
        s1 = 'Channel B : {0:6.1f} MHz  |  {1:+5.1f} dBm  | RF {2}\n'.format(f0,p0, 'ON' if m0 else 'OFF').encode()
        return s0+s1
