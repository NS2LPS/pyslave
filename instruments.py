import traceback, sys
import visa
from pyslave import drivers
import ivi

# VISA resource manager
rm = visa.ResourceManager()

# Known devices with their Python drivers and naming convention
known_devices   = {'HEWLETT-PACKARD 34401A': (ivi.agilent.agilent34401A, lambda s : 'dmm' + str(int(s.split('::')[1])%10)),
                   'HEWLETT-PACKARD E3631A': (ivi.agilent.agilentE3641A, lambda s : 'dcpwr' + str(int(s.split('::')[1])%10)),
                   'Rohde&Schwarz ZVA40-2Port' : (drivers.zvb, lambda s : 'zva'),
                   'Rohde&Schwarz ZVB8-2Port' : (drivers.zvb, lambda s : 'zvb'),                
                   }

# Keep track of loaded instruments
__loaded__ = dict()



def openinst(address):
    try :
        app = rm.open_resource(address)
        id = app.query('*IDN?')
        app.close()
    except :
        raise InstrumentError('Could not id intrument at {0}.'.format(address))
    id = id.split(',')[:2]
    id = ' '.join(id)
    if id in known_devices:
        driver, name_func = known_devices[id]
        app = driver(address)
        shortname = name_func(address)
    else:
        app = rm.open_resource(address)
        shortname = 'dev{0:02d}'.format(int(address.split('::')[1]))
    app.shortname = shortname
    app.fullname = id + ' ' + address
    __loaded__[shortname] = app
    return app


def openall(match):
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
    __loaded__[shortname].close()
    del __loaded__[shortname]
