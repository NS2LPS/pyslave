"""This module defines magic IPython functions to run pyslave from the IPython shell.
The slave window is created when the module is loaded."""

from IPython.core.magic import register_line_magic, needs_local_scope
from pyslave import instruments

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
    if res : print 'Loaded instruments :'
    for app in res:
        local_ns[app.shortname] = app
        print '{0:10s} -> {1}'.format(app.shortname, app.fullname)

@register_line_magic
def listall(line):
    """List all loaded instruments."""
    print "Loaded instruments :"
    for app in instruments.__loaded__:
        print '{0:10s} -> {1}'.format(app.shortname, app.fullname)

del listall, openall, openinst, closeinst

# Scripts launching, pausing

from pyslave import __slave__
slave = __slave__.SlaveWindow()
slave.show()

@register_line_magic
@needs_local_scope
def start(filename, local_ns):
    """Convert and launch a script in slave."""
    if not filename.endswith('.py'):
        filename += '.py'
    slave.call(filename, local_ns)

@register_line_magic
@needs_local_scope
def call(filename, local_ns):
    """Convert and launch a script in slave."""
    if not filename.endswith('.py'):
        filename += '.py'
    slave.call(filename, local_ns)

@register_line_magic
def pause(line):
    """Pause the running script."""
    slave.on_pushButton_Pause_clicked()

@register_line_magic
def resume(line):
    """Resume the paused script."""
    slave.on_pushButton_Resume_clicked()

@register_line_magic
def abort(line):
    """Abort the running script. If the script does not finish within 10 s,
    a dialog appears to eventually force the script to terminate."""
    slave.on_pushButton_Abort_clicked()

@register_line_magic
def window(line):
    """Show the slave window."""
    slave.show()

del call, window, pause, resume, abort

# Miscellaneous
import time, os

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

del today, lastday
