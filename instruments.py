"""The instruments module contains functions to open and close VISA instruments.
It keeps track of all the instruments that are loaded and attributes them unique shortnames."""

import traceback, sys
import visa
from pyslave import drivers

# VISA resource manager
rm = visa.ResourceManager()

# Known devices with their driver and category
known_devices   = {'HEWLETT-PACKARD 34401A': (drivers.agilent.agilent34401A, 'dmm'),
                   'HEWLETT-PACKARD E3631A': (drivers.agilent.agilentE3641A,  'dcpwr'),
                   'Rohde&Schwarz ZVA40-2Port' : (drivers.rohdeschwarz.zvb, 'vna'),
                   'Rohde&Schwarz ZVB8-2Port' : (drivers.rohdeschwarz.zvb, 'vna'),
                   }

# Keep track of loaded instruments
__loaded__ = dict()

# Naming scheme
def __shortname__(prefix):
    prev = [ int(k[len(prefix):]) for k in __loaded__.iterkeys() if k.startswith(prefix) ]
    next = max(prev)+1 if prev else 1
    return prefix + str( next )

def openinst(address):
    """Open the instrument at the specified address.
    The address must be a valid VISA resource. The instrument ID is queried and
    the function looks for the appropriate class and returns an instance of the found class.
    The function also sets the fullname and shortname attributes."""
    try :
        app = rm.open_resource(address)
        id = app.query('*IDN?')
        app.close()
    except :
        raise InstrumentError('Could not id intrument at {0}.'.format(address))
    id = id.split(',')[:2]
    id = ' '.join(id)
    if id in known_devices:
        driver, typ = known_devices[id]
        app = driver(address)
        shortname = __shortname__(typ)
    else:
        app = rm.open_resource(address)
        shortname = __shortname__('instr')
    app.shortname = shortname
    app.fullname = id + ' ' + address
    __loaded__[shortname] = app
    return app


def openall(match):
    """Open all instruments whose address contains match.
    For example, openall('GPIB') loads all GPIB devices and return them in a list."""
    res = []
    for address in rm.list_resources() :
        if match in address:
            try:
                app = openinst(str(address.strip()))
                res.append(app)
            except:
                error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
                for e in error_msgs: print e
                print 'Error while opening instrument at {0}.'.format(address)
    return res


def closeinst(shortname):
    """Close the instrument specified by its shortname."""
    __loaded__[shortname].close()
    del __loaded__[shortname]
