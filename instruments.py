"""The instruments module contains functions to open and close VISA instruments.
It keeps track of all the instruments that are loaded and attributes them unique shortnames."""

import traceback, sys, logging
import visa
from pyslave.drivers import *

# Logger
logger = logging.getLogger('pyslave.instruments')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

# VISA resource manager
rm = visa.ResourceManager()

# Known devices with their driver and category
known_devices   = {'HEWLETT-PACKARD 34401A': (agilent.agilent34401A, 'dmm'),
                   'HEWLETT-PACKARD E3631A': (agilent.agilentE3641A,  'dcpwr'),
                   'Rohde&Schwarz ZVA40-2Port' : (rohdeschwarz.zvb, 'vna'),
                   'Rohde&Schwarz ZVB8-2Port' : (rohdeschwarz.zvb, 'vna'),
                   'Stanford_Research_Systems SR830': (standfordresearch.SR830, 'lockin'),
                   '*IDN LECROY LT322': (lecroy.LecroyScope, 'scope'),
                   }

# Keep track of loaded instruments
__loaded__ = dict()

# Naming scheme
def __shortname__(prefix):
    prev = [ int(k.shortname[len(prefix):]) for k in __loaded__.itervalues() if k.shortname.startswith(prefix) ]
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
    id = str(' '.join(id)).strip()
    if id in known_devices:
        driver, typ = known_devices[id]
        app = driver(address)
    else:
        app = rm.open_resource(address)
        typ = 'instr'
    fullname = id + ' ' + address
    app.shortname =  __loaded__[fullname].shortname if fullname in __loaded__ else __shortname__(typ)
    app.fullname = fullname
    __loaded__[fullname] = app
    logger.info('Opening {0} as {1}.'.format(app.fullname, app.shortname))
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
    """Close the instrument specified by its shortname and remove it from the instrument list."""
    d = dict( [ (v.shortname, k) for k,v in __loaded__.iteritems() ] )
    fullname = d[shortname]
    __loaded__[fullname].close()
    logger.info('Closing {0}.'.format(shortname))
    del __loaded__[fullname]
