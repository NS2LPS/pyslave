"""This module defines magic IPython functions to run pyslave from the IPython shell."""

from IPython.core.magic import register_line_magic, needs_local_scope
from pyslave import instruments
from pyslave import __slave__

slave = None

data_directory = 'Z:\\Data\\'

# Instruments loading and listing
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

# Scripts launching, pausing
def __start_slave__():
    global slave
    slave = __slave__.SlaveWindow()
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
    args = line.split(' ')
    script = """
    import time
    ax, fig = subplots(111)
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
            if thread.stopflag : break
    """.format(args[0], args[1] if len(args)>1 else 1)
    exec script in local_ns
    if slave is None : __start_slave__()
    slave.thread_start(local_ns['script_monitor'])

measure_parameters = {'iterable' : '',
                      'set_function' : '',
                      'set_sleep' : '',
                      'read_function' : '',
                      'read_sleep' : '',
                      'plot':'y',
                      'filename':'',
                      }

def __update_measure_parameter__():
    text_input = {'iterable' : 'Variable to iterate over',
                  'set_function' : 'Set instrument value (looping variable is x)',
                  'set_sleep' : 'Sleep',
                  'read_function' : 'Read instrument',
                  'read_sleep' : 'Sleep',
                  'plot':'Plot',
                  'filename':'Save to',
                  }

@register_line_magic
@needs_local_scope
def measure(line, local_ns):
    """Measure the output of an instrument and plot it while scanning a parameter."""
    if line :
        exec 'args=dict({0})'.format(','.join(args))
        measure_parameters.update(args)
    else :
        for k,v in text_input.iteritems():
            inp = input('{0} [{1}] '.format(v, measure_parameters[k]))
            if inp : measure_parameters[k] = inp
    script = """
    import time
    from pyslave.script import increment
    if {plot}=='y': ax, fig = subplots(111)
    measure_out = dict(values=[], parameters=[])
    filename = increment({filename})
    def script_measure(thread):
        for x in {iterable}:
            {set_function}
            time.sleep({set_sleep})
            val = {read_function}
            thread.display('Measured value '+str(val))
            measure_out['values'].append(val)
            measure_out['parameters'].append(x)
            ax.cla()
            if {plot}=='y':
                ax.plot(measure_out['parameters'], measure_out['values'])
                thread.draw()
            with open(filename, 'a') as f:
                f.write('{0}    {1}\n'.format(x, val))
            time.sleep({read_sleep})
            thread.pause()
            if thread.stopflag : break
    """.format(measure_parameters)
    exec script in local_ns
    if slave is None : __start_slave__()
    print 'To quickly start the same measurement, copy paste this line : '
    print 'measure {0}'.format(' '.join(["{0}='{1}'" for k,v in measure_parameters]))
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

del call, window, pause, resume, abort

# Miscellaneous
import time, os
from pyslave import script

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
    args = line.split(' ')
    func = args[0] if '(' in args[0] else '{0}.fetch()'.format(args[0])
    exec func in local_ns
    filename = script.increment(args[1])
    instr = local_ns[func.split('.',1)[0]]
    script.save_txt(instr, filename)
    print "Data saved to",filename

@register_line_magic
@needs_local_scope
def fetch_h5(line, local_ns):
    """Fetch data from an instrument and save them as HDF5 file."""
    args = line.split(' ')
    func = args[0] if '(' in args[0] else '{0}.fetch()'.format(args[0])
    exec func in local_ns
    filename = script.increment(args[1])
    instr = local_ns[func.split('.',1)[0]]
    exec 'save_param = dict( {0} )'.format(','.join(args[2:]))
    script.save_h5(instr, str(filename), **save_param)
    print "Data saved to",filename


del today, lastday, fetch_txt, fetch_h5
