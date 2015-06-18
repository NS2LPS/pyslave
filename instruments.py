"""The instruments module contains functions to open and close VISA or NI-DAQ instruments.
It keeps track of all the instruments that are loaded and attributes them unique shortnames.
Loaded instruments are stored in the ``__loaded__`` dictionary."""

import time, traceback, sys, logging, importlib
from collections import OrderedDict

# Logger
logger = logging.getLogger('pyslave.instruments')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

# Get VISA resource manager
try:
    import visa
    from pyvisa import VisaIOError
    # VISA resource manager
    __visa__rm__ = visa.ResourceManager()
except:
    __visa__rm__ = None

# Get NIDAQ module
try:
    import PyDAQmx as __ni__
    import ctypes
except:
    __ni__ = None

# Known devices with their driver and type
known_devices   = {'HEWLETT-PACKARD 34401A': ('agilent' , 'agilent34401A', 'dmm'),
                   'HEWLETT-PACKARD E3631A': ('agilent', 'agilentE3641A',  'dcpwr'),
                   'Rohde&Schwarz ZVA40-2Port' : ('rohdeschwarz', 'zvb', 'vna'),
                   'Rohde&Schwarz ZVB8-2Port' : ('rohdeschwarz', 'zvb', 'vna'),
                   'Stanford_Research_Systems SR830': ('standfordresearch', 'SR830', 'lockin'),
                   '*IDN LECROY LT322': ('lecroy','LecroyScope', 'scope'),
                   'Yokogawa 7651':('yokogawa', 'yokogawa7651','dcpwr'),
                   'NI 9269': ('nidaq','ni9269','nidaqao'),
                   'NI 9239 (BNC)': ('nidaq','ni9239','nidaqai'),
                   }

# Keep track of loaded instruments
__loaded__ = OrderedDict()

# Naming scheme
def __shortname__(prefix):
    prev = [ int(k.shortname[len(prefix):]) for k in __loaded__.itervalues() if k.shortname.startswith(prefix) ]
    next = max(prev)+1 if prev else 1
    return prefix + str( next )

class InstrumentError(Exception):
    pass

def openinstr(address, id=None, shortname=None):
    """Open the instrument at the specified VISA address.
    The address must be a valid VISA resource.
    If id is None, the instrument id is queried. If no driver is found for the corresponding id, a generic instrument is returned
    otherwise an instance of the found driver class is returned.
    The function also sets the fullname and shortname attributes automatically (unless shortname is specified)."""
    if __visa__rm__ is None:
        raise InstrumentError('VISA library not loaded')
    if id is None:
        app = __visa__rm__.open_resource(address)
        try:
            app.clear()
            id = app.query('*IDN?')
            id = id.split(',')[:2]
            id = str(' '.join(id)).strip()
        except VisaIOError:
            # Assume it is a yoko
            id = 'Yokogawa 7651'
            time.sleep(0.5)
            app.clear()
        except:
            raise InstrumentError('Could not id intrument at {0}.'.format(address))
        finally:
            app.close()
    if id in known_devices:
        pkg, driver, typ = known_devices[id]
        try :
            m = importlib.import_module( '.{0}'.format(pkg), 'pyslave.drivers')
            driver = getattr(m, driver)
            app = driver(address)
        except:
            error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
            for e in error_msgs: print e
            print 'Error while loading instrument driver {0}, using generic instrument instead.'.format(driver)
            app = __visa__rm__.open_resource(address)
            typ = 'instr'
    else:
        app = __visa__rm__.open_resource(address)
        typ = 'instr'
    fullname = id + ' ' + address
    if shortname is None:
        app.shortname =  __loaded__[fullname].shortname if fullname in __loaded__ else __shortname__(typ)
    else:
        app.shortname = shortname
    app.fullname = fullname
    __loaded__[fullname] = app
    logger.info('Opening {0} as {1}.'.format(app.fullname, app.shortname))
    return app

def opennidaq(devname, id=None, shortname=None):
    """Open the NI-DAQ device with the specified name.
    If id is None, the device id is queried. If no driver is found for the corresponding id,
    an error is raised otherwise an instance of the found driver class is returned.
    The function also sets the fullname and shortname attributes automatically (unless shortname is specified)."""
    if __ni__ is None:
        raise InstrumentError('NI-DAQ library not loaded.')
    if id is None:
        buffer = ctypes.create_string_buffer('',1024)
        __ni__.DAQmxGetDeviceAttribute(devname, __ni__.DAQmx_Dev_ProductType, buffer, 1024)
        id = buffer.value.strip()
    if id in known_devices:
        pkg, driver, typ = known_devices[id]
        m = importlib.import_module( '.{0}'.format(pkg), 'pyslave.drivers')
        driver = getattr(m, driver)
        app = driver(devname)
    else:
        raise InstrumentError('No driver for NI-DAQ device {0}.'.format(id))
    fullname = id + ' ' + devname
    if shortname is None:
        app.shortname =  __loaded__[fullname].shortname if fullname in __loaded__ else __shortname__(typ)
    else:
        app.shortname = shortname
    app.fullname = fullname
    __loaded__[fullname] = app
    logger.info('Opening {0} as {1}.'.format(app.fullname, app.shortname))
    return app


def openall(match, resource='visa'):
    """Open all instruments whose address contains match in the given resource.
    For example, openall('GPIB', resource='visa') loads all GPIB devices and return them in a list.
    Or openall('Mod',resource='nidaq') loads all NI-DAQ modules in a rack."""
    if resource is 'visa':
        return __openall_visa__(match)
    elif resource is 'nidaq':
        return __openall_nidaq__(match)
    else:
        print 'Unknown resource :',resource
        return []

def __openall_visa__(match):
    res = []
    if __visa__rm__ is None : return res
    for address in __visa__rm__.list_resources() :
        if match in address:
            try:
                app = openinstr(str(address.strip()))
                res.append(app)
            except:
                error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
                for e in error_msgs: print e
                print 'Error while opening instrument at {0}.'.format(address)
    return res

def __openall_nidaq__(match):
    res = []
    if __ni__ is None : return res
    devicenames = ctypes.create_string_buffer('',1024)
    __ni__.DAQmxGetSystemInfoAttribute(__ni__.DAQmx_Sys_DevNames, devicenames, 1024);
    devices = devicenames.value.split(',')
    for dev in devices :
        if match in dev:
            try:
                app = opennidaq(str(dev.strip()))
                res.append(app)
            except:
                error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
                for e in error_msgs: print e
                print 'Error while opening device {0}.'.format(dev)
    return res



def closeinstr(shortname):
    """Close the instrument specified by its shortname and remove it from the instrument list."""
    d = dict( [ (v.shortname, k) for k,v in __loaded__.iteritems() ] )
    fullname = d[shortname]
    __loaded__[fullname].close()
    logger.info('Closing {0}.'.format(shortname))
    del __loaded__[fullname]
