"""The instruments module contains functions to open and close VISA, NI-DAQ or COM instruments.
"""

import traceback, sys, importlib, pkgutil, os

class InstrumentError(Exception):
    pass

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

# Get serial (COM) module
try:
    import serial as __com__
except:
    __com__ = None

# Parse drivers directory to build driver list
def __drivers__():
    drivers = {}
    loader = pkgutil.get_loader('pyslave.drivers')
    for sub_module in pkgutil.iter_modules([os.path.dirname(loader.get_filename())]):
        try:
            m = importlib.import_module( '.{0}'.format(sub_module.name), 'pyslave.drivers')
            drivers.update(m.__drivers__)
        except:
            pass
    return drivers

# Open the instrument and set missing attributes
def __open__(address, driver, resource):
    app = driver(address)
    app.__ressource__ = resource
    app.__driver_name__ = driver.__name__
    app.__driver_module__ = driver.__module__
    if not hasattr(app, '__inst_id__'):
        app.__inst_id__ = 'Unknown instrument'
    if not hasattr(app, '__instr_type__'):
        app.__instr_type__ = 'instr'
    if not hasattr(app,'__address__'):
        if resource in ('VISA','NIDAQ','COM'):
            app.__address__ = address
        else:
            app.__address__ = ''
    return app

def openVISA(address, driver=None):
    """Open the instrument with the specified VISA address and python driver.
    The address must be a valid VISA resource or alias.

    If driver is None, the instrument id is queried and a corresponding driver
    is searched. If the instrument does not answer (e.g. Yoko) or a matching
    driver is not found, the generic VISA instrument driver is selected.

    The function returns an instance of the driver class.
    """
    if __visa__rm__ is None:
        raise InstrumentError('PyVISA module not loaded')
    # Check if valid VISA identifier
    info = __visa__rm__.resource_info(address)
    address = info.resource_name
    # Automatic driver selection
    if driver is None:
        app = __visa__rm__.open_resource(address)
        try:
            app.clear()
            id = app.query('*IDN?')
            id = id.split(',')[:2]
            id = str(' '.join(id)).strip()
        except:
            error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
            for e in error_msgs: print(e)
            print("""Identification of {0} failed, using generic VISA instrument.
                  If the instrument is a Yoko, set the driver to 'yokogawa.yokogawa7651'.""".format(address))
            id = None
        finally:
            app.close()
        if id is not None:
            known_devices = __drivers__()
            if id in known_devices:
                driver = known_devices[id]
            else:
                print('No driver found for instrument {0}, using generic VISA instrument.'.format(id))
    # Import driver
    if driver is not None:
        try:
            pkg_name, driver_name = driver.rsplit('.',1)
            m = importlib.import_module( '.{0}'.format(pkg_name), 'pyslave.drivers')
            driver = getattr(m, driver_name)
        except:
            error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
            for e in error_msgs: print(e)
            print('Error while importing instrument driver {0}, using generic VISA instrument.'.format(driver))
            driver = __visa__rm__.open_resource
    else:
        driver = __visa__rm__.open_resource
    return __open__(address, driver, 'VISA')

def openNIDAQ(devname, driver=None):
    """Open the NI-DAQ device with the specified name and python driver.

    If driver is None, the device id is queried and a matching driver
    is looked for. If no driver is found for the corresponding id,
    an error is raised.

    The function returns an instance of the driver class.
    """
    if __ni__ is None:
        raise InstrumentError('PyDAQmx module not loaded.')

    if driver is None:
        buffer = ctypes.create_string_buffer('',1024)
        __ni__.DAQmxGetDeviceAttribute(devname, __ni__.DAQmx_Dev_ProductType, buffer, 1024)
        id = buffer.value.strip()
    known_devices = __drivers__()
    if id in known_devices:
        pkg_name, driver_name = known_devices[id].rsplit('.',1)
        m = importlib.import_module( '.{0}'.format(pkg_name), 'pyslave.drivers')
        driver = getattr(m, driver_name)
    else:
        raise InstrumentError('No driver for NI-DAQ device {0}.'.format(id))
    return __open__(devname, driver,'NIDAQ')

def openCOM(com, driver=None):
    """Open the COM device with the specified COM port and python driver.

    If driver is None, the generic com interface driver is used.

    The function returns an instance of the driver class.
    """
    if __com__ is None:
        raise InstrumentError('PySerial module not loaded.')

    if driver is not None:
        try:
            pkg_name, driver_name = driver.rsplit('.',1)
            m = importlib.import_module( '.{0}'.format(pkg_name), 'pyslave.drivers')
            driver = getattr(m, driver_name)
        except:
            error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
            for e in error_msgs: print(e)
            print('Error while importing instrument driver {0}, using generic COM driver.'.format(driver))
            driver = __com__.Serial
    else:
        driver = __com__.Serial
    return __open__(com, driver,'COM')

def openOther(arg, driver):
    """Open specific types of instruments.

    The function returns an instance of the driver. The first
    argument is passed to the driver."""
    return __open__(arg, driver, 'Other')
