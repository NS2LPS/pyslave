"""This module defines magic IPython functions to run pyslave from the IPython shell."""

from matplotlib.pyplot import figure
from IPython.core.magic import register_line_magic, needs_local_scope
import time, os, re, logging, inspect, logging.handlers
from collections import OrderedDict

from pyslave import data_directory
from pyslave import instruments
from pyslave.slave import SlaveWindow

# Logger
logger = logging.getLogger('pyslave.magic')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

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

@register_line_magic
@needs_local_scope
def openinstr(line, local_ns):
    """Load the VISA instrument at the specified resource."""
    args = __arg_split__(line)
    addr = str(args[0])
    id = str(args[1]) if len(args)>1 else None
    app = instruments.openinstr(addr, id)
    local_ns[app.shortname] = app
    print '{0} loaded as {1}'.format(app.fullname, app.shortname)

@register_line_magic
@needs_local_scope
def closeinstr(line, local_ns):
    """Close the specified instrument."""
    res = instruments.closeinstr(line)
    del local_ns[line]

@register_line_magic
@needs_local_scope
def openall(line, local_ns):
    """Load all GPIB instruments and NI-DAQ devices."""
    if instruments.__loaded__:
        print 'Previously loaded instruments :'
        for app in instruments.__loaded__.itervalues():
            print '{0:10s} -> {1}'.format(app.shortname, app.fullname)
    print "Loading new devices ..."
    # GPIB
    res = instruments.openall('GPIB', 'visa')
    for app in res:
        local_ns[app.shortname] = app
    for app in res:
        print '{0:10s} -> {1}'.format(app.shortname, app.fullname)
    # NI-DAQ
    res = instruments.openall('Mod', 'nidaq')
    for app in res:
        local_ns[app.shortname] = app
    for app in res:
        print '{0:10s} -> {1}'.format(app.shortname, app.fullname)
    print "Done"


@register_line_magic
def listall(line):
    """List all loaded instruments."""
    for app in instruments.__loaded__.itervalues():
        print '{0:10s} -> {1}'.format(app.shortname, app.fullname)

del listall, openall, openinstr, closeinstr

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
    exec script in local_ns
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
        exec 'args=dict({0})'.format(','.join(args))
        measure_parameters.update(args)
    else :
        print "Press enter to keep previous value. Abort with many q's (qqqq...)."
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
    exec script in local_ns
    if slave is None : __start_slave__()
    if not line:
        print 'To quickly start the same measurement, copy paste this line : '
        print 'measure {0}'.format(' '.join(["{0}='{1}'".format(k,v) for k,v in measure_parameters.iteritems()]))
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
    """Abort the running script. If the script does not finish within 10 s,
    a dialog appears to eventually force the script to terminate."""
    if slave is None : return
    slave.on_pushButton_Abort_clicked()

@register_line_magic
def window(line):
    """Show the slave window."""
    if slave is None : __start_slave__()
    slave.show()

del call, window, pause, resume, abort, monitor, measure


########################################################
# Miscellaneous magic
########################################################

@register_line_magic
def today(line):
    """Change directory to today's data directory, create it if it does not exist."""
    now = time.localtime()
    year = str(now.tm_year)
    month = '{0:02d}'.format(now.tm_mon)
    day = '{0:02d}'.format(now.tm_mday)
    # Create directory if not existing
    path = os.path.join(data_directory, year, year+'_'+month+'_'+day)
    if not os.path.exists(path): os.makedirs(path)
    os.chdir(path)
    print 'Directory set to',path

@register_line_magic
def lastday(line):
    """Change directory to the last day of data."""
    lastyear = sorted(os.listdir(data_directory))[-1]
    lastday = sorted(os.listdir(os.path.join(data_directory,lastyear)))[-1]
    path = os.path.join(data_directory, lastyear, lastday)
    os.chdir(path)
    print 'Directory set to',path


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
    exec "fig = figure()" in local_ns
    data.plot(local_ns['fig'])
    exec "fig.show()" in local_ns
    # Save data to file
    if filename :
        msg = data.save(filename, **param)

del today, lastday, capture
