import requests
from numpy import nan
import time

class rcdat:
    __inst_id__ = 'RCDAT variable attenuator'
    def __init__(self, url="http://192.168.0.85/"):
        self.url = url
        r1 = requests.get(url+'MN?\n')
        r2 = requests.get(url+'SN?\n')   
        print (r1.text.split('=')[1],'loaded with SN',r2.text.split('=')[1])
    def getatt(self):
        """Return tha current attenuation in dB."""
        err = True
        retry = 0
        while err and retry<2:
            try:
                r = requests.get(self.url+'ATT?\n')
                res = float(r.text)
                err = False
            except:
                err = True
                time.sleep(1)
                retry += 1
                res = nan
        return res
    def setatt(self, att):
        """Set the attenuation in dB.
        The argument should be a multiple of 0.25 ranging between 0 and 31.25."""
        if (att*4) % 1 :
            print ('RDCAT : WARNING {0} is not a multiple of 0.25 dB'.format(att))
        r=requests.get(self.url+'SETATT={0}\n'.format(att))
        if r.text!='1':
            raise Exception('RDCAT : Error while setting attenuation.')
    def __repr__(self):
        att = self.getatt()
        s1 = 'Attenuation : {0} dB\n'.format(att)
        return s1