from PyQt4 import QtGui, QtCore
from PyQt4.uic import loadUiType
import os, sys
import h5py
import numpy as np
from scipy.signal import butter, lfilter

# Dynamically convert ui file to python
Ui_MainWindow, QMainWindow = loadUiType('main_window.ui')

# IQ demodulator function factory
def make_iq(**kwargs):
    params ={ 'fsampling' : 1e9,
              'fcut' : 20e6,
              'decimate' : 100,
            }
    params.update(kwargs)
    q1 = np.array([1,0,-1,0],dtype=np.int8)
    q1 = np.array([0,1,0,-1],dtype=np.int8)
    b, a = butter(4, 0.8/params['fsampling']*params['fcut'])
    decimate = params['decimate']
    def iq(y):
        y = np.reshape(y, (len(y)/4,4))
        iq1 = y*q1
        iq2 = y*q2
        iq1 = lfilter(b, a, iq1.flatten())[::decimate]
        iq2 = lfilter(b, a, iq2.flatten())[::decimate]
        return iq1, iq2
    return iq


class AcquisitionThread(QtCore.QThread):
    def __init__(self, fun):
        super(AcquisitionThread, self).__init__()
        self.fun = fun
    def run(self):
        self.fun()


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        # Create the main window
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.update_iq()
        self.curve = Qwt5.QwtPlotCurve()
        self.curve.attach(self.ui.qwtPlot)
        # Acquisition thread
        self.acquisition_thread = AcquisitionThread(self.acquire)
        self.acquiring = False

    @QtCore.pyqtSignature("")
    def on_pushButton_Start_clicked(self):
        if not self.acquiring:
            # Start acquisition
            self.acquisition_thread.finished.connect(self.callback)
            self.acquisition_thread.start()
            self.acquiring = True

    @QtCore.pyqtSignature("")
    def on_pushButton_Stop_clicked(self):
        if self.acquiring:
            # Stop acquisition
            self.acquisition_thread.finished.disconnect(self.callback)
            self.acquiring = False

    def acquire(self):
        data = scope1.fetch('C3')
        iq1, iq2 = self.iq(data['wave'])
        self.last_trace = sqrt(iq1**2 + iq2**2)

    def callback(self):
        self.plot()
        self.acquisition_thread.start()

    def plot(self):
        y = self.last_trace
        x = np.arange(len(y))
        self.curve.setData(x, y)
        self.ui.qwtPlot.replot()

    def update_iq(self):
        self.iq = make_iq()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
