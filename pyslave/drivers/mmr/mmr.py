import traceback, sys
import socket
import zmq
import numpy as np
context = zmq.Context()

class mmr3:
    __inst_id__ = 'MMR3 thermometer'
    def __init__(self, address):
        self.address = address    
    def get(self, key):
        """Get the last readout from the MMR3.
        The mmr3.pyw progam has to run.
        Valid keys are : 'MC Cernox', 'MC RuO2', 'Still', '4K stage', '50K stage'"""   
        try:
            socket=context.socket(zmq.REQ)
            socket.connect("tcp://{0}:5556".format(self.address))
            socket.setsockopt(zmq.RCVTIMEO,100)
            socket.setsockopt(zmq.SNDTIMEO,100)
            socket.send(key.encode())     
            msg = socket.recv()
            res = float(msg)
        except ValueError:
            print("Could not convert received string to float")
            print(msg.decode())
            res = np.nan
        except:
            traceback.print_exc(limit=1,file=sys.stdout)
            print("Error wile reading temperature")
            print("Make sure that the mmr3 server is running.")
            res = np.nan
        return res
        

class mgc3:
    __inst_id__ = 'MGC3 heater'
    def __init__(self, address):
        port = int(address.split('.')[-1])+12000
        self.address = (address, port)
    def send(self, msg):
        sock = socket.socket(socket.AF_INET,    # Internet
                             socket.SOCK_DGRAM) # UDP
        sock.sendto(msg.encode(), self.address)

    def set(self, n,v):
        if type(v) is str: v = "\"{0}\"".format(v)
        if type(v) is float : v = "{0:0.3e}".format(v)
        self.send("MGC3SET {0} {1}".format(n,v))

    def setpoint_MC(self, TmK):
        self.set(2, TmK*1e-3)

    def setpoint_Still(self, TmK):
        self.set(14, TmK*1e-3)
    
        