"""This module defines magic IPython functions to rapidly access data."""
import os, time
import configparser
from IPython.core.magic import register_line_magic, needs_local_scope

__config__ = configparser.ConfigParser()
__config__.read(os.path.join(os.path.dirname(__file__), 'pydata.ini'))
data_directory = __config__['pydata']['data_directory']

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
    """Remove last file created in the directory.
    Enter 'y' to delete the proposed file, 'n' to skip the file, 'q' to quit."""
    l = [ (os.stat(name).st_mtime, name) for name in os.listdir('.')]
    l.sort()
    last = l[-1][1]
    ans = ''
    i = 1
    while ans.upper()!='Y' and ans.upper()!='Q' and i<=len(l):
        last = l[-i][1]
        i += 1
        ans = input('Remove {0} (y/n/q) ? [n] '.format(last))
        if ans.upper()=='Y':
            os.remove(last)
            print('{0} removed.'.format(last))

del today, lastday, rmlast
