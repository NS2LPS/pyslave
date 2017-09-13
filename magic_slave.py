"""This module defines magic IPython functions to run pyslave from the IPython shell."""

from matplotlib.pyplot import figure
from IPython.core.magic import register_line_magic, needs_local_scope
import time, os, re, logging, inspect, logging.handlers
from collections import OrderedDict
import configparser
import traceback

from pyslave import instruments
from pyslave import data_directory
from pyslave.slave import SlaveWindow

# Logger
logger = logging.getLogger('pyslave.magic')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

# List of ressources that are handled
__resources__ = ['VISA', 'NIDAQ']

# Keep trace of instruments
__instruments__ = { k:{} for k in __ressources__}

# Register opening functions
__open_functions__ = {'VISA' : instruments.openVISA,
                      'NIDAQ': instruments.openNIDAQ,
                      }

# Look for prefix (for remote access)
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
__prefix__ = { r:config.get(r,'prefix',fallback='') for r in __resources__}

# Read the ini file
def __config__(main_resource):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '{0}.ini'.format(main_resource)))
    return config

# Argument parsing functions
def __arg_split__(line):
    """Split line on whitespace but do not split string parameters."""
    res = ['']
    line = str(line)
    s = line.replace("\"\"\"", chr(240))
    single_quote = False
    double_quote = False
    triple_quote = False
    for c in s:
        if single_quote or double_quote or triple_quote:
            res[-1] += c
            single_quote ^= c is chr(39)
            double_quote ^= c is chr(34)
            triple_quote ^= c is chr(240)
        else:
            if c is ' ':
                res.append('')
            else:
                res[-1] += c
                single_quote = c is chr(39)
                double_quote = c is chr(34)
                triple_quote = c is chr(240)
    return [x.replace(chr(240), "\"\"\"" ) for x in res if x]

########################################################
# Instruments loading and listing magic
########################################################
def __find_config__(name):
    for main_resource in __resources__:
        config_resource = __config__(main_resource)
        for resource in config_ressource.sections():
            value = config_ressource[resource]
            # Look-up by name
            if value['name']==name:
                id = value.get('id', None)
                return main_ressource, ressource, id, name
            # Look-up by ressource name
            if resource==name:
                id = value.get('id', None)
                name = value['name']
                return main_ressource, ressource, id, name
    return None, None, None, None


def __open__(main_ressource, ressource, name, id, local_ns):
    if not name:
        print ("Invalid instrument name")
        return
    func = __open_functions__[main_ressource]
    instr_dict = __instruments__[main_ressource]
    if name in instr_dict:
        print("{0} already loaded".format(name))
        return
    try:
        app = func(__prefix__[main_ressource], ressource, id)
    except:
        error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
        for e in error_msgs: print(e)
        print("Error while loading {0}".format(name))
    local_ns[name] = app
    instr_dict[name] = app
    logger.info('Opening {0} ({1}) as {2}'.format(name, ressource, app.driver_name))
    print('{0} ({1}) loaded as {2}'.format(name, ressource, app.driver_name))


@register_line_magic
@needs_local_scope
def openinstr(line, local_ns):
    """Opens an instrument through a name or address (or alias).
    The name (or the address) is looked up in the config.ini file
    to get information about the instrument.

    If no information is found, the function assumes that one wants
    to open a new VISA device. The function asks for an instrument
    name and id and try to load the instrument.

    The user can also provide name='...' and id='...' as parameters.

    Examples :
        # Open by name
        openinstr vna1
        # Open by address
        openinstr GPIB0::22
        openinstr GPIB0::22 name='dcpwr1' id='Yokogawa 7651'
    """
    args = __arg_split__(line)
    a0 = str(args[0])
    # Look up in the config.ini file
    main_ressource, ressource, id, name = __find_config__(a0)
    # Otherwise assumes it is a VISA device
    if main_ressource is None:
        main_ressource = 'VISA'
        ressource = a0
        exec('args=dict({0})'.format(','.join(args[1:])) )
        if 'name' not in args:
            inp = raw_input('Instrument name : ')
            name = inp.strip()
        else:
            name = args['name']
        if 'id' not in args:
            inp = raw_input('Instrument id [auto] : ')
            id = inp.strip() or None
        else:
            id = args['id']
    # Open the instrument
    __open__(main_ressource, ressource, name, id, local_ns)


@register_line_magic
@needs_local_scope
def closeinstr(line, local_ns):
    """Close the specified instrument."""
    name = line.strip()
    if not name:
        return
    logger.info('Closing {0}.'.format(name))
    for main_ressource in __resources__:
        d = __instruments__[main_ressource]
        if name in d:
            app = d.pop(name)
            break
    if name in local_ns:
        app = local_ns.pop(name)
    try:
        app.close()
    except:
        pass

@register_line_magic
@needs_local_scope
def openall(line, local_ns):
    """Load all ressources listed in the config.ini file."""
    for main_resource in __resources__:
        config_resource = __config__(main_resource)
        for resource in config_resource.sections():
            name = config_resource.get(resource, 'name')
            id = config_resource.get(resource, 'id', fallback=None)
            __open__(main_ressource, ressource, name, id, local_ns)


@register_line_magic
def listall(line):
    """List all loaded instruments."""
    for main_resource in __resources__:
        d = __instruments__[main_resource]
        if d:
            print("{0} :".format(main_resource))
            for k,v in d.items():
                print('{0:10s} -> {1}'.format(k, v.resource))


@register_line_magic
def listVISA(line):
    """List all available VISA instruments."""
    for app in instruments.__visa__rm__.list_resources():
        print(app)

del listall, openall, openinstr, closeinstr, listVISA

########################################################
# Scripts launching, pausing, resuming, aborting magic
########################################################

# Slave window variable
slave = None

# Open slave window
def __start_slave__():
    global slave
    slave = SlaveWindow()
    slave.show()

@register_line_magic
@needs_local_scope
def call(filename, local_ns):
    """Convert and launch a script in slave."""
    if not filename.endswith('.py'):
        filename += '.py'
    if slave is None : __start_slave__()
    slave.call(filename, local_ns)

@register_line_magic
@needs_local_scope
def monitor(line, local_ns):
    """Monitor the output of an instrument and plot it."""
    args = __arg_split__(line)
    script = """
import time
from pyslave.data import xy
fig = figure()
monitor_out = xy(x=np.empty(0), y=np.empty(0))
t0 = time.time()
def script_monitor(thread):
    while True:
        val = {0}
        thread.display('Monitored value '+str(val))
        monitor_out.append(time.time()-t0, val)
        monitor_out.plot(fig)
        thread.draw()
        time.sleep({1})
        thread.pause()
        if thread.stopflag : break""".format(args[0] if '(' in args[0] else args[0] + '()',
                                             args[1] if len(args)>1 else 1)
    exec(script, local_ns)
    if slave is None : __start_slave__()
    logger.info('Creating monitor script :\n'+script)
    slave.thread_start(local_ns['script_monitor'])

measure_parameters = OrderedDict([
                      ('iterable' , ''),
                      ('set_function' , 'dcpwr1(x)'),
                      ('set_sleep' , '0'),
                      ('read_function' , 'dmm1()'),
                      ('read_sleep' , '0'),
                      ('plot','y'),
                      ('filename','iv.txt'),
                      ])

text_input = OrderedDict([
              ('iterable' , 'Parameter values to iterate over'),
              ('set_function' , 'Set parameter (parameter variable is x)'),
              ('set_sleep' , 'Sleep (in s)'),
              ('read_function' , 'Read value'),
              ('read_sleep' , 'Sleep (in s)'),
              ('plot' , 'Plot (y/n)'),
              ('filename' , 'Save to (space for not saving)'),
              ])

@register_line_magic
@needs_local_scope
def measure(line, local_ns):
    """Measure the output of an instrument and plot it while scanning a parameter."""
    if line :
        args = __arg_split__(line)
        exec('args=dict({0})'.format(','.join(args)))
        measure_parameters.update(args)
    else :
        print("Press enter to keep previous value. Abort with many q's (qqqq...).")
        for k,v in text_input.iteritems():
            inp = raw_input('{0} [{1}] : '.format(v, measure_parameters[k]))
            if inp.endswith('qqqq') : return
            if inp : measure_parameters[k] = inp.strip()
    if '(' not in measure_parameters['read_function'] : measure_parameters['read_function']+= '()'
    if '(' not in measure_parameters['set_function'] and '=' not in measure_parameters['set_function'] :
        measure_parameters['set_function']+= '(x)'
    script = """
import time
from pyslave.data import xy
if '{plot}'=='y': fig = figure()
measure_out = xy(x=array({iterable}), y=ones_like(array({iterable}))*nan)

def script_measure(thread):
    for i,x in enumerate(measure_out.x):
        {set_function}
        time.sleep({set_sleep})
        y = {read_function}
        thread.display('Step ' + str(i+1) + '/' + str(len(measure_out.x)))
        thread.looptime()
        measure_out.y[i] = y
        if '{plot}'=='y':
            measure_out.plot(fig)
            thread.draw()
        time.sleep({read_sleep})
        thread.pause()
        if thread.stopflag : break
    if "{filename}" :
        measure_out.save("{filename}")
        """.format(**measure_parameters)
    exec(script, local_ns)
    if slave is None : __start_slave__()
    if not line:
        print('To quickly start the same measurement, copy paste the line below : ')
        print('measure {0}'.format(' '.join(["{0}='{1}'".format(k,v) for k,v in measure_parameters.iteritems()])))
    logger.info('Creating measurement script :\n'+script)
    slave.thread_start(local_ns['script_measure'])

@register_line_magic
def pause(line):
    """Pause the running script."""
    if slave is None : return
    slave.on_pushButton_Pause_clicked()

@register_line_magic
def resume(line):
    """Resume the paused script."""
    if slave is None : return
    slave.on_pushButton_Resume_clicked()

@register_line_magic
def abort(line):
    """Abort the running script."""
    if slave is None : return
    slave.on_pushButton_Abort_clicked()

@register_line_magic
def kill(line):
    """Kill the running script."""
    if slave is None : return
    slave.on_pushButton_Kill_clicked()

@register_line_magic
def window(line):
    """Show the slave window."""
    if slave is None : __start_slave__()
    slave.show()


@register_line_magic
@needs_local_scope
def capture(line, local_ns):
    args = __arg_split__(line)
    # First argument
    func = 'out = ' + args[0] if '(' in args[0] else args[0].strip() + '()'
    # Second argument
    filename = str(args[1]) if len(args)>1 else None
    # Optional extra arguments
    param = eval('dict({0})'.format(','.join(args[2:])))
    # Fetch data
    data = eval(func, globals(), local_ns)
    # Plot data
    exec("fig_capture = figure()", local_ns)
    data.plot(local_ns['fig_capture'])
    exec("fig_capture.show()", local_ns)
    # Save data to file
    if filename :
        msg = data.save(filename, **param)

del call, window, pause, resume, abort, kill, monitor, measure, capture
