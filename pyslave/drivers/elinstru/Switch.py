# VISA resource manager
try:
    from pyslave.instruments import __visa_rm__
except:
    __visa_rm__ = None

if __visa_rm__ is None:
    try:
        import pyvisa as visa
        __visa_rm__ = visa.ResourceManager()
    except:
        __visa_rm__ = None


class Switch:
    """Elinstru microwave switch driver.
    """
    __inst_id__ = 'PilotSwitch Rev. NUCLEO_F756ZG May 22 2024 14:40:22 MbedOS 61700'

    def __init__(self, resource, *args, **kwargs):
        self.instrument = __visa_rm__.open_resource(resource, *args, **kwargs)
        self.instrument.write_termination = '\n'
        self.instrument.read_termination = '\n'
        self.instrument.send_end = True
        self.query = self.instrument.query
        self.write = self.instrument.write
        self.close = self.instrument.close
    def getIDN(self):       
        return self.query("*IDN?")
    def getMAC(self):       
        return self.query("MAC?")
    def getCLIENT(self):    
        return self.query("CLIENT?")
    def getETH(self):       
        return self.query("ETH?")
    def getIP(self):        
        return self.query("IP?")
    def getIPALL(self):     
        return self.query("IP=ALL?")
    def getSWITCHS(self):   
        return self.query("SWITCHS?")
    def openSwitchs(self):  
        self.write('1O;2O')
    def closeSwitchs(self): 
        self.write('1C;2C')
    def openSwitch1(self):  
        self.write('1O')
    def closeSwitch1(self): 
        self.write('1C')
    def openSwitch2(self):  
        self.write('2O')
    def closeSwitch2(self): 
        self.write('2C')
