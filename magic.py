# Register IPython magic functions
from IPython.core.magic import register_line_magic, needs_local_scope
from pyslave import instruments

data_directory = 'Z:\\Data\\'

# Instruments loading and listing
@register_line_magic
@needs_local_scope
def openall(line, local_ns):
    res = instruments.openall('GPIB')
    for app in res:
        local_ns[app.shortname] = app
        print '{0} loaded as {1}'.format(app.fullname, app.shortname)

@register_line_magic
def listall(line):
    print "Loaded instruments :",' '.join(instruments.__loaded__.iterkeys())

del listall, openall


# Scripts launching, pausing
from pyslave import slave

@register_line_magic
@needs_local_scope
def call(filename, local_ns):
    if not filename.endswith('.py'):
        filename += '.py'
    slave.slave_window.call(filename, local_ns)

@register_line_magic
def pause(line):
    slave.slave_window.on_pushButton_Pause_clicked()

@register_line_magic
def resume(line):
    slave.slave_window.on_pushButton_Resume_clicked()

@register_line_magic
def abort(line):
    slave.slave_window.on_pushButton_Abort_clicked()

@register_line_magic
def window(line):
    slave.slave_window.show()

del call, window, pause, resume, abort

# Miscellaneous
import time, os

@register_line_magic
def today(line):
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
    lastyear = sorted(os.listdir(data_directory))[-1]
    lastday = sorted(os.listdir(os.path.join(data_directory,lastyear)))[-1]
    path = os.path.join(data_directory, lastyear, lastday)
    os.chdir(path)
    print 'Directory set to',path

del today, lastday
