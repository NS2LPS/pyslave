"""Create the GUI to handle script execution.
The module also defines the way scripts are converted before being run."""

from PyQt5 import QtCore, QtGui, Qt
from IPython.core.magic import register_line_magic
import sys, traceback, time, imp, os, logging
from ui.SlaveWindow import Ui_MainWindow
from matplotlib.pyplot import draw

# Logger
logger = logging.getLogger('pyslave.slave')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

class SlaveError(Exception):
    pass

class ScriptThread(QtCore.QThread):
    display_signal = QtCore.pyqtSignal()
    draw_signal = QtCore.pyqtSignal()
    def __init__(self, parent, script_function):
        QtCore.QThread.__init__(self, parent)
        self.script_function = script_function
        self.stopflag = False
        self.pauseflag = False
        self.parent = parent
        self.message = []
    def display(self, msg, echo=False, log=False):
        self.message.append( (msg, echo, log) )
        self.display_signal.emit()
    def draw(self):
        if not self.stopflag:
            self.parent.draw_semaphore.acquire()
            self.draw_signal.emit()
            self.parent.draw_semaphore.acquire()
            self.parent.draw_semaphore.release()
    def looptime(self):
        newtime  = time.time()
        self.display('Loop time : {0:.1f} s'.format(newtime-self.lasttime))
        self.lasttime = newtime
    def run(self):
        self.error = False
        self.lasttime = time.time()
        try:
            self.script_function(self)
        except:
            self.error = True
            error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
            for e in error_msgs : print(e)
    def pause(self):
        disp = True
        while self.pauseflag :
            if disp :
                self.display('Script paused.',True)
                disp = False
            time.sleep(0.1)
        if not disp:
            self.display('Script is running...',True)

class SlaveWindow(QtGui.QMainWindow):
    def __init__(self):
        # Graphical User Interface
        super(SlaveWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.draw_semaphore = QtCore.QSemaphore(1)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        self.thread = None

    def call(self, filename, local_ns):
        if self.thread is not None and self.thread.isRunning():
            self.display('A script is already running.')
            return
        if not filename.endswith('_converted.py'):
            try:
                convert(filename)
            except :
                error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
                for e in error_msgs : print(e)
                self.display('Error while converting {0}.'.format(filename))
                return
        filename = filename[:-3] + '_converted.py'
        try:
            execfile(filename, local_ns)
        except :
            error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
            for e in error_msgs : print(e)
            self.display('Error while loading {0}.'.format(filename))
            return
        with open(filename,'r')as f:
            logger.info('Creating converted script {0} :\n'.format(filename)+f.read())
        self.thread_start(local_ns['script_main'])

    def thread_start(self, func):
        # Setup the thread and starts it
        self.thread = ScriptThread(self, func)
        self.thread.finished.connect(self.thread_finished)
        self.thread.terminated.connect(self.thread_terminated)
        self.thread.display_signal.connect(self.thread_display)
        self.thread.draw_signal.connect(self.draw)
        self.thread.start()
        self.ui.textEdit.clear()
        self.display('Script is running...', log=True)

    @QtCore.pyqtSignature("")
    def on_pushButton_Abort_clicked(self):
        if self.thread is None : return
        self.thread.stopflag = True
        self.thread.pauseflag = False
        self.display('Aborting...', log=True)
        self.display('Try Killing if script does not finish.', log=True)

    @QtCore.pyqtSignature("")
    def on_pushButton_Kill_clicked(self):
        if self.thread is None : return
        self.thread.terminate()
        self.display('Killing...', log=True)

    @QtCore.pyqtSignature("")
    def on_pushButton_Pause_clicked(self):
        if self.thread is None : return
        self.thread.pauseflag = True

    @QtCore.pyqtSignature("")
    def on_pushButton_Resume_clicked(self):
        if self.thread is None : return
        self.thread.pauseflag = False

    def display(self, text, echo=True, log=False):
        self.ui.textEdit.append(text)
        if echo : print(text)
        sys.stdout.flush()
        if log : logger.info(text)

    def thread_display(self):
        while self.thread.message:
            self.display(*self.thread.message.pop(0))

    def thread_finished(self):
        if not self.thread.error:
            self.display('Script finished.', log=True)
        else:
            self.display('Script finished with an error.', log=True)

    def thread_terminated(self):
        self.display('Script forced to terminate.', log=True)

    def draw(self):
        draw()
        self.draw_semaphore.release()

def __replace__(line):
    line = line.replace('#draw','thread.draw()')
    line = line.replace('#pause','thread.pause()')
    line = line.replace('#abort','if thread.stopflag : break')
    line = line.replace('#looptime','thread.looptime()')
    line = line.replace('#disp', 'thread.disp')
    return line

def convert(filename):
    """Convert a python script so that it can be called by slave.
    The converted file is named by appending '_converted' to the filename."""
    with open(filename,'r') as f:
        script = f.read()
    if '#main' not in script:
        raise SlaveError('Could not find #main section in {0}.'.format(filename))
    header, main = [s.strip() for s in script.split('#main')]
    converted_script = filename[:-3] + '_converted.py'
    with open(converted_script,'w') as f:
        print('# Auto generated script file',file=f)
        print('',file=f)
        for l in header.split('\n'):
            print(__replace__(l), file=f)
        print('', file=f)
        print('# Main script function', file=f)
        print('def script_main(thread):', file=f)
        abortflag = True
        for l in main.split('\n'):
            if '#abort' in l : abortflag=False
            print("   ",__replace__(l), file=f)
        if abortflag:
            print("   ","if thread.stopflag : break", file=f)

