"""This module defines magic IPython functions to run pyslave from the IPython shell."""

import time, os, logging, inspect, logging.handlers, sys, io
from collections import OrderedDict
import configparser
import traceback
from matplotlib.pyplot import figure
from IPython.core.magic import register_line_magic, needs_local_scope
from pyslave import instruments
from pyslave.slave import SlaveWindow

# Logger
logger = logging.getLogger('pyslave.magic')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

# List of resources that are handled
__resources__ = ['VISA', 'NIDAQ', 'COM', 'Other']

# Keep trace of all instruments
__instruments__ = OrderedDict()

# Keep track of opened COM ports and VISA devices
__opened_COM__ = []
__opened_VISA__ = []
__opened_NIDAQ__ = []


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
def __read_config_instruments__():
    __config__ = configparser.ConfigParser()
    __config__.read(os.path.join(os.path.dirname(__file__), 'pyslave.ini'))
    config_instruments = dict()
    for resource in __resources__:
        if __config__.has_section(resource):
            section = __config__[resource]
            for k,v in section.items():
                if not k.startswith('__'):
                    vsplit = v.split(' ')
                    if len(vsplit)==1:
                        config_instruments[k] = {'resource':resource,'address':vsplit[0],'driver':None}
                    elif len(vsplit)==2:
                        config_instruments[k] = {'resource':resource,'address':vsplit[0],'driver':vsplit[1]}
                    else:
                        print('Badly formatted line in pyslave.ini:')
                        print('{0} = {1}'.format(k,v))
    return config_instruments

# Not used for the moment
def __read_config_special__(section):
    __config__ = configparser.ConfigParser()
    __config__.read(os.path.join(os.path.dirname(__file__), 'pyslave.ini'))
    config_special = {}
    if __config__.has_section(section):
        section = __config__[section]
        for k,v in section.items():
            if k.startswith('__'):
                config_special[k] = v
    return config_special


def __open__(resource, address, name, driver, local_ns, verbose=False):
    if resource=='VISA':
        info = instruments.__visa_rm__.resource_info(address)
        res_name = info.resource_name
        if res_name in __opened_VISA__:
            print('{0} is already opened'.format(address))
            return None
        inst = instruments.openVISA(address, driver, verbose)
        name = __get_name__(inst,verbose) if name is None else name
        __opened_VISA__.append(res_name)
    elif resource=='NIDAQ':
        if address in __opened_NIDAQ__:
            print('{0} is already opened'.format(address))
        inst = instruments.openNIDAQ(address, driver, verbose)
        name = __get_name__(inst,verbose) if name is None else name
        __opened_NIDAQ__.append(address)
    elif resource=='COM':
        if address in __opened_COM__:
            print('{0} is already opened'.format(address))
            return None
        inst = instruments.openCOM(address, driver, verbose)
        name = __get_name__(inst,verbose) if name is None else name
        __opened_COM__.append(address)
    elif resource=='Other':
        inst = instruments.openOther(address, driver, verbose)
        name = __get_name__(inst,verbose) if name is None else name
    local_ns[name] = inst
    __instruments__[name] = inst
    logger.info('Opening {0} {1} as {2} with {3} ({4})'.format(resource, address, name, inst.__driver_name__, inst.__driver_module__))
    print('{0:10s} : {1} {2}'.format(name, inst.__inst_id__, inst.__address__))
    return inst

def __get_name__(inst, verbose=False):
    prefix = inst.__inst_type__
    prev = [ int(k[len(prefix):]) for k in __instruments__.keys() if k.startswith(prefix) ]
    i = 1
    while i in prev:
        i += 1
    name = prefix + str(i)
    if verbose:
        inp = input('Instrument name [{0}] : '.format(name))
        inp = inp.strip()
        name = inp or name
    return name

@register_line_magic
@needs_local_scope
def openinstr(line, local_ns):
    """Opens an instrument through a name or address.

    The function first looks into the pyslave.ini file. If an
    entry is found corresponding to the given name, the corresponding
    instrument is opened.

    If no matches is found in pyslva.ini:
    - if the given name contains COM, the function opens the coresponding COM port
    - otherwise, the function assumes the passed name is a VISA alias or address and
    tries to open it

    A driver can be passed as a second argument, it will override the driver
    specified in the pyslave.ini file.

    Examples :
        # Open by name
        openinstr dmm1
        # Open by address or alias
        openinstr TCPIP::192.168.0.81
        openinstr ZND
        openinstr GPIB0::22
        openinstr GPIB0::22 yokogawa.yogogawa7651.yokogawa7651
    """
    args = __arg_split__(line)
    instr_name = args[0]
    driver = args[1] if len(args)>1 else None
    # Look up in the pyslave.ini file
    config_instruments = __read_config_instruments__()
    if instr_name in config_instruments:
        name = instr_name
        if name in __instruments__ :
            print('{0} already exists. Close it before opening it again.'.format(name))
            return
        resource = config_instruments[instr_name]['resource']
        address = config_instruments[instr_name]['address']
        if driver is None:
            driver = config_instruments[instr_name].get('driver',None)
        __open__(resource, address, instr_name, driver, local_ns, True)
    elif 'COM' in instr_name:
        __open__('COM', instr_name, None, driver, local_ns, True)
    else:
        rm = instruments.__visa_rm__
        if rm is None:
            return
        try:
            info = rm.resource_info(instr_name)
            res = info.resource_name
        except:
            print('{0} is not a known instrument, COM port or VISA resource.'.format(instr_name))
            return
        __open__('VISA', instr_name, None, driver, local_ns, True)



@register_line_magic
@needs_local_scope
def closeinstr(line, local_ns):
    """Close the specified instrument."""
    name = line.strip()
    if not name:
        return
    logger.info('Closing {0}.'.format(name))
    if name not in __instruments__:
        print('Unknown instrument {0}.'.format(name))
        return
    inst = __instruments__[name]
    list_resources = {'VISA':__opened_VISA__,'NIDAQ':__opened_NIDAQ__,'COM':__opened_COM__}
    l = list_resources.get(inst.__resource__,None)
    if l:
        l.remove(inst.__address__)
    try:
        inst.close()
    except:
        pass
    if name in local_ns:
        del local_ns[name]
    del __instruments__[name]

@register_line_magic
@needs_local_scope
def closeall(line, local_ns):
    """Close all instruments."""
    while __instruments__:
        name,inst = __instruments__.popitem()
        logger.info('Closing {0}.'.format(name))
        list_resources = {'VISA':__opened_VISA__,'NIDAQ':__opened_NIDAQ__,'COM':__opened_COM__}
        l = list_resources.get(inst.__resource__,None)
        if l:
            l.remove(inst.__address__)
        try:
            inst.close()
        except:
            pass
        if name in local_ns:
            del local_ns[name]
        del inst


@register_line_magic
@needs_local_scope
def openall(line, local_ns):
    """Load all instruments listed in the pyslave.ini file."""
    config = __read_config_instruments__()
    err = ''
    for k,v in config.items():
        if k in __instruments__:
           print('{0} is already loaded.'.format(k))
        else:
            try:
                __open__(v['resource'],v['address'],k,v['driver'],local_ns)
            except:
                err = err + '{0} cannot be loaded\n'.format(k)
    print(err)

@register_line_magic
@needs_local_scope
def openGPIB(line, local_ns):
    """Load all GPIB instruments."""
    for address in instruments.__visa_rm__.list_resources('GPIB?*::INSTR'):
        try:
            __open__('VISA',address,None,None,local_ns)
        except:
            traceback.print_exc(limit=1,file=sys.stdout)
            print('Error while opening {0}.'.format(address))

@register_line_magic
def listall(line):
    """List all loaded instruments."""
    for k,v in __instruments__.items():
        print('{0:10s} : {1} {2}'.format(k, v.__inst_id__, v.__address__))

@register_line_magic
def listVISA(line):
    """List all available VISA instruments."""
    for address in instruments.__visa_rm__.list_resources():
        print(address)

@register_line_magic
def resetVISA(line):
    """Reset VISA connection.
    Close instruments before running this function"""
    instruments.resetVISA()


del listall, openall, openinstr, openGPIB, closeinstr, closeall, listVISA, resetVISA

########################################################
# Scripts launching, pausing, resuming, aborting magic
########################################################

class SlaveError(Exception):
    pass


# Slave window variable
__slave__ = None

def __slave_disp__(msg):
    logger.info(msg)
    if __slave__ is None:
        print(msg)
    else:
        if __slave__.thread and __slave__.thread.isRunning():
            __slave__.thread.display(msg, echo=False, log=False)
        else:
            print(msg)


def __replace__(line, add_pause):
    line = line.expandtabs(4)
    line = line.replace('#draw','thread.draw()')
    line = line.replace('#pause','thread.pause()')
    if '#abort' in line:
        if add_pause and line.strip().startswith('#abort'):
            line = line.replace('#abort','thread.pause()') + '\n' + line.replace('#abort','if thread.stopflag : break')
        else:
            line = line.replace('#abort','if thread.stopflag : break')
    line = line.replace('#looptime','thread.looptime()')
    line = line.replace('#disp', 'thread.display')
    return line

def __convert__(filename):
    """Convert a python script so that it can be called by slave.
    The converted file is named by appending '_converted' to the filename."""
    with open(filename,'r') as f:
        script = f.read()
    if '#main' not in script:
        raise SlaveError('Could not find #main section in {0}.'.format(filename))
    header, main = [s.strip() for s in script.split('#main')]
    with io.StringIO() as f:
        print('# Auto generated script file',file=f)
        print('',file=f)
        # Put back header
        print(header, file=f)
        print('', file=f)
        # Create script function
        print('# Main script function', file=f)
        print('def __slave_script__(thread):', file=f)
        add_pause = '#pause' not in main
        for l in main.split('\n'):
            print("   ",__replace__(l, add_pause), file=f)
        output = f.getvalue()
    return output

def __start_slave__(script, filename, local_ns):
    """Start Slave thread with the passed code"""
    global __slave__
    code = compile(script, filename, 'exec')
    glob = globals()
    for k,v in local_ns.items():
        if not k.startswith('_'):
            glob[k]=v
    locals = dict()
    exec(code, glob, locals)
    local_ns.update(locals)
    glob.update(locals)
    if __slave__ is None:
        __slave__ = SlaveWindow()
    __slave__.show()
    __slave__.thread_start(__slave_script__)
    logger.info('Starting script {0} :\n{1}'.format(filename, script))


@register_line_magic
@needs_local_scope
def call(filename, local_ns):
    """Convert and launch a script in slave.
    If the filename ends with '_converted.py', the
    file is not converted again."""
    if not filename.endswith('.py'):
        filename = filename + '.py'
    if not filename.endswith('_converted.py'):
        try:
            script = __convert__(filename)
        except :
            traceback.print_exc(file=sys.stdout)
            print('Error while converting {0}.'.format(filename))
            return
    else:
        with open(filename,'r') as f:
            script = f.read()
    __start_slave__(script, filename, local_ns)

@register_line_magic
def convert(filename):
    """Convert a script and show the result in the console."""
    if not filename.endswith('.py'):
        filename = filename + '.py'
    out = __convert__(filename)
    print(out)
    

@register_line_magic
@needs_local_scope
def monitor(line, local_ns):
    """Monitor the output of an instrument and plot it.
    The first argument is the function to monitor.
    The second optional argument is the time period of the monitoring.
    The default value is 1s.

    The results are stored in monitor_out.

    Examples:
    %monitor dmm1
    %monitor dmm1 0.2
    %monitor instr1.read()
    """
    args = __arg_split__(line)
    script = """
import time
from pydata import xy
fig = figure()
monitor_out = xy(x=empty(0), y=empty(0))
t0 = time.time()
def __slave_script__(thread):
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
    __start_slave__(script, 'monitor', local_ns)
    print("Results are stored in monitor_out.")

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
    """Measure the output of an instrument and plot it while scanning a parameter.
    Results are stored in measure_out."""
    if line :
        args = __arg_split__(line)
        args = dict([ (args[i],args[i+1]) for i in range(0 ,len(args),2)])
        measure_parameters.update(args)
    else :
        print("Press enter to keep previous value. Abort with many q's (qqqq...).")
        for k,v in text_input.items():
            inp = input('{0} [{1}] : '.format(v, measure_parameters[k]))
            if inp.endswith('qqqq') : return
            if inp : measure_parameters[k] = inp.strip()
    if '(' not in measure_parameters['read_function'] : measure_parameters['read_function']+= '()'
    if '(' not in measure_parameters['set_function'] and '=' not in measure_parameters['set_function'] :
        measure_parameters['set_function']+= '(x)'
    script = """
import time
from pydata import xy
if '{plot}'=='y': fig = figure()
measure_out = xy(x=array({iterable}), y=ones_like(array({iterable}))*nan)

def __slave_script__(thread):
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
    __start_slave__(script, 'measure', local_ns)
    if not line:
        print('To quickly start the same measurement, copy paste the line below : ')
        print('measure {0}'.format(' '.join(["{0}='{1}'".format(k,v) for k,v in measure_parameters.items()])))
    print("Results are stored in measure_out.")


@register_line_magic
def pause(line):
    """Pause the running script."""
    if __slave__ is None : return
    __slave__.on_pushButton_Pause_clicked(echo=True)

@register_line_magic
def resume(line):
    """Resume the paused script."""
    if __slave__ is None : return
    __slave__.on_pushButton_Resume_clicked(echo=True)

@register_line_magic
def abort(line):
    """Abort the running script."""
    if __slave__ is None : return
    __slave__.on_pushButton_Abort_clicked(echo=True)

@register_line_magic
def kill(line):
    """Kill the running script."""
    if __slave__ is None : return
    __slave__.on_pushButton_Kill_clicked(echo=True)

@register_line_magic
def window(line):
    """Show the slave window."""
    global __slave__
    if __slave__ is None :
        __slave__ = SlaveWindow()
    __slave__.show()

@register_line_magic
@needs_local_scope
def capture(line, local_ns):
    args = __arg_split__(line)
    # First argument
    func = args[0] if '(' in args[0] else args[0].strip() + '()'
    # Second argument
    filename = str(args[1]) if len(args)>1 else None
    # Optional extra arguments
    param = eval('dict({0})'.format(','.join(args[2:])))
    # Fetch data
    data = eval(func, globals(), local_ns)
    # Plot data
    exec("capture_fig = figure()", globals(), local_ns)
    data.plot(local_ns['capture_fig'])
    exec("capture_fig.show()", globals(), local_ns)
    local_ns['capture_out'] = data
    # Save data to file
    if filename :
        msg = data.save(filename, **param)
    else:
        print("Data are stored in capture_out. Figure is capture_fig.")

del call, convert, window, pause, resume, abort, kill, monitor, measure, capture
