"""This module defines magic IPython functions to run pyslave from the IPython shell."""

from IPython.core.magic import register_line_magic, needs_local_scope
import time, os, re, logging, inspect
from collections import OrderedDict

from pyslave import script
from pyslave import instruments
from pyslave.slave import SlaveWindow

# Data directory
data_directory = 'Z:\\Data\\'

# Logger
logger = logging.getLogger('pyslave')
logger.setLevel(logging.DEBUG)
# create file handler
fh = logging.TimedRotatingFileHandler(os.path.join(os.path.dirname(inspect.getfile(script)), '/log/pyslave.log'), when='midnight', delay=True)
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.info('Magic functions loaded')

########################################################
# Instruments loading and listing magic
########################################################

@register_line_magic
@needs_local_scope
def openinst(line, local_ns):
    """Load the VISA instrument at the specified resource."""
    res = instruments.openinst(line)
    local_ns[app.shortname] = app
    print '{0} loaded as {1}'.format(app.fullname, app.shortname)

@register_line_magic
@needs_local_scope
def closeinst(line, local_ns):
    """Close the specified instrument."""
    res = instruments.closeinst(line)
    del local_ns[line]

@register_line_magic
@needs_local_scope
def openall(line, local_ns):
    """Load all GPIB instruments."""
    res = instruments.openall('GPIB')
    for app in res:
        local_ns[app.shortname] = app
    print "Loaded instruments :"
    for app in instruments.__loaded__.itervalues():
        print '{0:10s} -> {1}'.format(app.shortname, app.fullname)

@register_line_magic
def listall(line):
    """List all loaded instruments."""
    print "Loaded instruments :"
    for app in instruments.__loaded__.itervalues():
        print '{0:10s} -> {1}'.format(app.shortname, app.fullname)

del listall, openall, openinst, closeinst

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

# Argument parsing functions
cool_pattern = re.compile("[^\\s\"']+|\"[^\"]*\"|'[^']*'")
def __arg_split__(line):
    """Split line on whitespace but do not split string parameters. Glue back jey=keyword arguments."""
    split = re.findall(cool_pattern, line)
    out=[]
    while split:
        val=split.pop(0)
        if val.endswith('=') : val+=split.pop(0)
        out.append(val)
    return out

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
fig, ax = subplots()
monitor_out = dict(values=[], times=[])
t0 = time.time()
def script_monitor(thread):
    while True:
        val = {0}
        thread.display('Monitored value '+str(val))
        monitor_out['values'].append(val)
        monitor_out['times'].append(time.time()-t0)
        ax.cla()
        ax.plot(monitor_out['times'], monitor_out['values'])
        thread.draw()
        time.sleep({1})
        thread.pause()
        if thread.stopflag : break""".format(args[0], args[1] if len(args)>1 else 1)
    exec script in local_ns
    if slave is None : __start_slave__()
    slave.thread_start(local_ns['script_monitor'])

measure_parameters = OrderedDict([
                      ('iterable' , ''),
                      ('set_function' , ''),
                      ('set_sleep' , '0'),
                      ('read_function' , 'dmm1.measurement.read(1)'),
                      ('read_sleep' , '0'),
                      ('plot','y'),
                      ('filename',''),
                      ])

text_input = OrderedDict([
              ('iterable' , 'Parameter values to iterate over'),
              ('set_function' , 'Set parameter (parameter variable is x)'),
              ('set_sleep' , 'Sleep (in s)'),
              ('read_function' , 'Read value'),
              ('read_sleep' , 'Sleep (in s)'),
              ('plot' , 'Plot (y/n)'),
              ('filename' , 'Save to (filename.txt)'),
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
        for k,v in text_input.iteritems():
            inp = raw_input('{0} [{1}] : '.format(v, measure_parameters[k]))
            if inp : measure_parameters[k] = inp
    script = """
import time
from pyslave.script import increment
if '{plot}'=='y': fig, ax = subplots()
measure_out = dict(values=[], parameters=[])
filename = increment('{filename}') if '{filename}' else ''
def script_measure(thread):
    for x in {iterable}:
        {set_function}
        time.sleep({set_sleep})
        val = {read_function}
        thread.display('Measured value '+str(val))
        measure_out['values'].append(val)
        measure_out['parameters'].append(x)
        ax.cla()
        if '{plot}'=='y':
            ax.plot(measure_out['parameters'], measure_out['values'])
            thread.draw()
        if filename:
            with open(filename, 'a') as f:
                f.write("{{0}}    {{1}}\\n".format(x, val))
        time.sleep({read_sleep})
        thread.pause()
        if thread.stopflag : break
    if filename : print "Data saved to", filename """.format(**measure_parameters)
    exec script in local_ns
    if slave is None : __start_slave__()
    if not line:
        print 'To quickly start the same measurement, copy paste this line : '
        print 'measure {0}'.format(' '.join(["{0}='{1}'".format(k,v) for k,v in measure_parameters.iteritems()]))
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
def fetch_txt(line, local_ns):
    """Fetch data from an instrument and save them as text file."""
    args = __arg_split__(line)
    func = args[0] if '(' in args[0] else '{0}.fetch()'.format(args[0])
    exec func in local_ns
    instr = local_ns[func.split('.',1)[0]]
    param = dict(increment=True)
    if len(args)>2 : param.update(eval('dict({0})'.format(','.join(args[2:]))))
    filename = script.increment(args[1]) if param['increment'] else args[1]
    script.save_txt(instr, filename)
    print "Data saved to",filename

@register_line_magic
@needs_local_scope
def fetch_h5(line, local_ns):
    """Fetch data from an instrument and save them as HDF5 file."""
    args = __arg_split__(line)
    func = args[0] if '(' in args[0] else '{0}.fetch()'.format(args[0])
    exec func in local_ns
    instr = local_ns[func.split('.',1)[0]]
    param = dict(increment=True)
    if len(args)>2 : param.update(eval('dict({0})'.format(','.join(args[2:]))))
    filename = script.increment(args[1]) if param['increment'] else args[1]
    if 'increment' in param : del param['increment']
    script.save_h5(instr, str(filename), **param)
    print "Data saved to",filename


del today, lastday, fetch_txt, fetch_h5
