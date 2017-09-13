"""The instruments module contains functions to open and close VISA or NI-DAQ instruments.
The Python ressource to be loaded when opening an instrument is obtained from the drivers.ini file.
"""

import traceback, sys, importlib, configparser

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

# Load known devices with their driver and type
def __drivers__():
    drivers = configparser.ConfigParser()
    drivers.read(os.path.join(os.path.dirname(__file__), 'drivers.ini'))
    return drivers

def openVISA(address, id=None):
    """Open the instrument at the specified VISA address.
    The address must be a valid VISA resource or alias.

    If id is None, the instrument id is queried. If the instrument does not answer (e.g. Yoko),
    an error is raised. If the id is listed in the drivers.ini file, the corresponding
    driver class is loaded and one instance is created, otherwise a generic instrument is instanciated.

    The function returns the instance of the instrument.
    """
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
            raise InstrumentError("""Identification of {0} failed. The instrument did not respound.
                                  If the instrument is a Yoko, set the id to 'Yokogawa 7651'.""".format(address))
        except:
            raise InstrumentError('Unknown error while identifying {0}.'.format(address))
        finally:
            app.close()
    known_devices = __drivers__()
    if id in known_devices:
        pkg_name    = known_devices[id]['package']
        driver_name = known_devices[id]['model']
        typ         = known_devices[id]['type']
        try :
            m = importlib.import_module( '.{0}'.format(pkg_name), 'pyslave.drivers')
            driver = getattr(m, driver_name)
            app = driver(address)
        except:
            error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
            for e in error_msgs: print(e)
            print('Error while loading instrument driver {0}, using generic instrument instead.'.format(driver_name))
            app = __visa__rm__.open_resource(address)
            typ = 'instr'
            driver_name = ''
            pkg_name = 'generic'
    else:
        app = __visa__rm__.open_resource(address)
        typ = 'instr'
        driver_name = ''
        pkg_name = 'generic'
    app.id = id
    app.resource = address
    app.driver_name = '{0}.{1}'.format(pkg_name,driver_name)
    return app

def openNIDAQ(devname, id=None):
    """Open the NI-DAQ device with the specified name.

    If id is None, the device id is queried. If no driver is found for the corresponding id,
    an error is raised otherwise an instance of the found driver class is returned.
    """
    if __ni__ is None:
        raise InstrumentError('NI-DAQ library not loaded.')

    if id is None:
        buffer = ctypes.create_string_buffer('',1024)
        __ni__.DAQmxGetDeviceAttribute(devname, __ni__.DAQmx_Dev_ProductType, buffer, 1024)
        id = buffer.value.strip()
    known_devices = __drivers__()
    if id in known_devices:
        pkg_name    = known_devices[id]['package']
        driver_name = known_devices[id]['model']
        typ         = known_devices[id]['type']
        m = importlib.import_module( '.{0}'.format(pkg_name), 'pyslave.drivers')
        driver = getattr(m, driver_name)
        app = driver(devname)
    else:
        raise InstrumentError('No driver for NI-DAQ device {0}.'.format(id))
    app.id = id
    app.ressource = devname
    app.driver_name = '{0}.{1}'.format(pkg_name,driver_name)
    return app

