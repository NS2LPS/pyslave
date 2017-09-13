"""This module defines magic IPython functions to rapidly access data."""

from IPython.core.magic import register_line_magic, needs_local_scope

from pyslave import data_directory

########################################################
# Miscellaneous magic functions for data handling
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
    print('Directory set to',path)

@register_line_magic
def lastday(line):
    """Change directory to the last day of data."""
    lastyear = sorted(os.listdir(data_directory))[-1]
    lastday = sorted(os.listdir(os.path.join(data_directory,lastyear)))[-1]
    path = os.path.join(data_directory, lastyear, lastday)
    os.chdir(path)
    print('Directory set to',path)

@register_line_magic
def rmlast(line):
    """Remove last file created in the directory."""
    l = [ (os.stat(name).st_mtime, name) for name in os.listdir('.')]
    l.sort()
    last = l[-1][1]
    ans = raw_input('Remove {0} ? [y] '.format(last))
    if ans=='' or ans=='y' or ans=='Y':
        os.remove(last)
        print('{0} removed.'.format(last))

del today, lastday, rmlast
