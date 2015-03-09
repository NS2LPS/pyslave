import traceback
import visa
from pyslave import drivers
import ivi

# VISA resource manager
rm = visa.ResourceManager()

# Known devices with their Python drivers and naming convention
known_devices   = {'HEWLETT-PACKARD 34401A': (ivi.agilent.agilent34401A, lambda s : 'dmm' + str(int(s.split('::')[1])%10)),
                   'HEWLETT-PACKARD E3631A': (ivi.agilent.agilentE3641A, lambda s : 'dcpwr' + str(int(s.split('::')[1])%10)),
                   'Rohde&Schwarz ZVA40-2Port' : (drivers.zvb, lambda s : 'zva'),
                   }

# Keep track of loaded instruments
__loaded__ = dict()


class InstrumentError(Exception):
    pass

def openinst(address):
    try :
        app = rm.open_resource(address)
        id = app.query('*IDN?')
        app.close()
    except :
        raise InstrumentError('Could not id intrument at {0}.'.format(address))
    id = id.split(',')[:2]
    id = ' '.join(id)
    if id in known_apparatus:
        driver, name_func = known_apparatus[id]
        try :
            app = driver(address)
            shortname = name_func(address)
        except :
            raise InstrumentError('Error while loading the instrument driver {0}.'.format(str(driver)))
    else:
        try:
            app = rm.open_resource(address)
            shortname = 'app{0:02d}'.format(int(s.split('::')[1]))
        except:
            raise InstrumentError('Error while loading the generic instrument at {0}.'.format(address))
    app.shortname = shortname
    app.fullname = id + ' ' + address
    __loaded__[shortname] = app
    return app


def openall(match):
    res = []
    for address in instruments.rm.list_resources() :
        if match in address:
            try:
                app = openinst(address)
                res.append(app)
            except:
                error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
                print error_msgs
                print 'Error while opening instrument at {0}.'.format(address)
    return res


def closeinst(shortname):
    __loaded__[shortname].close()
    del __loaded__[shortname]
