"""Create the GUI to handle script execution.
The module also defines the way scripts are converted before being run."""

from PyQt5 import QtCore, QtGui, Qt, QtWidgets
from PyQt5.uic import loadUiType
from IPython.core.magic import register_line_magic
import sys, traceback, time, imp, os, logging
#from .ui.SlaveWindow import Ui_MainWindow
from matplotlib.pyplot import draw


dirpath = os.path.dirname(__file__)
Ui_MainWindow, QMainWindow = loadUiType(os.path.join(dirpath,'SlaveWindow.ui'))

# Logger
logger = logging.getLogger('pyslave.slave')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())


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
            traceback.print_exc(file=sys.stdout)
    def pause(self):
        disp = True
        while self.pauseflag :
            if disp :
                self.display('Script paused.')
                disp = False
            time.sleep(0.1)
        if not disp:
            self.display('Script is running...')

class SlaveWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # Graphical User Interface
        super(SlaveWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.draw_semaphore = QtCore.QSemaphore(1)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        self.thread = None

    def thread_start(self, func):
        # Setup the thread and starts it
        if self.thread is not None and self.thread.isRunning():
            print('A script is already running.')
            return
        self.thread = ScriptThread(self, func)
        self.thread.finished.connect(self.thread_finished)
        self.thread.display_signal.connect(self.thread_display)
        self.thread.draw_signal.connect(self.draw)
        self.thread.start()
        self.ui.textEdit.clear()
        self.display('Script is running...', echo=True, log=True)

    @QtCore.pyqtSlot()
    def on_pushButton_Abort_clicked(self, echo=False):
        if self.thread is None : return
        self.thread.stopflag = True
        self.thread.pauseflag = False
        self.display('Aborting script...', echo=echo, log=True)
        self.display('Use %kill if script does not finish.', echo=echo, log=True)

    @QtCore.pyqtSlot()
    def on_pushButton_Kill_clicked(self, echo=False):
        if self.thread is None : return
        self.thread.terminate()
        self.display('Killing script...', echo=echo, log=True)

    @QtCore.pyqtSlot()
    def on_pushButton_Pause_clicked(self, echo=False):
        if self.thread is None : return
        self.thread.pauseflag = True
        self.display('Pausing script...', echo=echo, log=False)

    @QtCore.pyqtSlot()
    def on_pushButton_Resume_clicked(self, echo=False):
        if self.thread is None : return
        self.thread.pauseflag = False
        self.display('Resuming script...', echo=echo, log=False)

    def display(self, text, echo=False, log=False):
        self.ui.textEdit.append(text)
        if echo : print(text)
        sys.stdout.flush()
        if log : logger.info(text)

    def thread_display(self):
        while self.thread.message:
            self.display(*self.thread.message.pop(0))

    def thread_finished(self):
        if not self.thread.error:
            self.display('Script finished.', echo=True, log=True)
        else:
            self.display('Script finished with an error.', echo=True, log=True)

    def thread_terminated(self):
        self.display('Script forced to terminate.', echo=True, log=True)

    def draw(self):
        draw()
        self.draw_semaphore.release()
