from PyQt4 import QtCore, QtGui, Qt, Qwt5
from IPython.core.magic import register_line_magic
import sys, traceback, time, imp, os
from ui.SlaveWindow import Ui_MainWindow
from matplotlib.pyplot import draw

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
    def display(self, msg):
        self.message.append(msg)
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
            self.display(''.join(error_msgs))
    def pause(self):
        disp = True
        while self.pauseflag :
            if disp :
                self.display('Script paused.')
                disp = False
            time.sleep(0.1)
        if not disp:
            self.display('Script is running...')

class SlaveWindow(QtGui.QMainWindow):
    def __init__(self):
        # Graphical User Interface
        super(SlaveWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timeout = 10 # timeout in seconds
        self.draw_semaphore = QtCore.QSemaphore(1)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        self.thread = None

    #@QtCore.pyqtSignature("")
    #def on_pushButton_Call_clicked(self):
    #    filename = QtGui.QFileDialog.getOpenFileName(self, "Choose a script file", filter="Python (*.py)")
    #    if filename:
    #        self.call(filename)

    def call(self, filename, local_ns):
        if not filename.endswith('_converted.py'):
            try:
                convert(filename)
            except :
                error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
                print error_msgs
                print 'Error while converting {0}.'.format(filename)
                return
        filename = filename[:-3] + '_converted.py'
        try:
            #current_script = imp.load_source('current_script', filename)
            execfile(filename, local_ns)
        except :
            error_msgs = traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)
            for e in error_msgs : print e
            print 'Error while loading {0}.'.format(filename)
            return
        # Setup the thread and starts it
        self.thread = ScriptThread(self, local_ns['script_main'])
        self.thread.finished.connect(self.thread_finished)
        self.thread.terminated.connect(self.thread_terminated)
        self.thread.display_signal.connect(self.thread_display)
        self.thread.draw_signal.connect(self.draw)
        self.thread.start()
        self.ui.textEdit.clear()
        self.display('Script is running...')
        print 'Script is running...'

    @QtCore.pyqtSignature("")
    def on_pushButton_Abort_clicked(self):
        if self.thread is None : return
        self.thread.stopflag = True
        self.thread.pauseflag = False
        ret = self.thread.wait(self.timeout*1000)
        if not ret:
            ret = QtGui.QMessageBox.warning(self, "Script", "Script is not answering. Abort Anyway ?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No )
            if ret==QtGui.QMessageBox.Yes:
                self.thread.terminate()

    @QtCore.pyqtSignature("")
    def on_pushButton_Pause_clicked(self):
        if self.thread is None : return
        self.thread.pauseflag = True

    @QtCore.pyqtSignature("")
    def on_pushButton_Resume_clicked(self):
        if self.thread is None : return
        self.thread.pauseflag = False

    def display(self, text):
        self.ui.textEdit.append(text)

    def thread_display(self):
        while self.thread.message:
            self.display(self.thread.message.pop(0))

    def thread_finished(self):
        if not self.thread.error:
            self.display('Script finished.')
        else:
            self.display('Script finished with an error.')
        draw()

    def thread_terminated(self):
        self.display('Script aborted.')

    def draw(self):
        draw()
        self.draw_semaphore.release()

slave_window = SlaveWindow()
slave_window.show()

def __replace__(line):
    line = line.replace('#draw','thread.draw()')
    line = line.replace('#pause?','thread.pause()')
    line = line.replace('#break?','if thread.stopflag : break')
    line = line.replace('#abort?','if thread.stopflag : return')
    line = line.replace('#looptime?','thread.looptime()')
    line = line.replace('#disp','thread.display')
    return line

def convert(filename):
    with open(filename,'r') as f:
        script = f.read()
    if '#main' not in script:
        raise SlaveError('Could not find #main section in {0}.'.format(filename))
    header, main = [s.strip() for s in script.split('#main')]
    converted_script = filename[:-3] + '_converted.py'
    with open(converted_script,'w') as f:
        print >>f, '# Auto generated script file'
        print >>f
        for l in header.split('\n'):
            print >>f,__replace__(l)
        print >>f
        print >>f, '# Main script function'
        print >>f, "def script_main(thread):"
        for l in main.split('\n'):
            print >>f,"   ",__replace__(l)
