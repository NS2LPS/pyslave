import numpy as np
import zmq
import time
import pickle


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.setsockopt(zmq.REQ_CORRELATE, 1)
socket.setsockopt(zmq.REQ_RELAXED, 1)
socket.setsockopt(zmq.SNDTIMEO, 5000)
socket.setsockopt(zmq.RCVTIMEO, 10000)
socket.connect ("tcp://192.168.0.200:5556")


def request(*msg):    
    socket.send(pickle.dumps(msg,protocol=2))
    ret = socket.recv()
    return pickle.loads(ret,encoding='bytes')

def setup(channel0=True, channel1=True, decimation=1, packetsize=0x10000, nsamples=0x1000000):
    request('setup',channel0, channel1, decimation, packetsize, nsamples)

def IQmoments(nframes,b,nskip):
    request('IQmoments',nframes,b,nskip)

def IQmoments_phase_lock(nframes,b,nskip):
    request('IQmoments_phase_lock',nframes,b,nskip)
    
def IQmoments_both_shifted(nframes,b,nskip):
    request('IQmoments_both_shifted',nframes,b,nskip)

def IQmoments_task(task,nframes,b,nskip):
    request('IQmoments_task',task,nframes,b,nskip)
    
def trace(nframes):
    request('trace',nframes)

def IQtrace(nframes,b):
    request('IQtrace',nframes,b)

def IQtrace_phase_lock(nframes,b):
    request('IQtrace_phase_lock',nframes,b)

    
def wait():
    request('wait')

def get_result():
    ret = request('get_result')
    return(ret)


