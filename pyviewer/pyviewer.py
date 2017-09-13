from PyQt4 import QtGui, QtCore
from PyQt4.uic import loadUiType
import os, sys
import h5py
import numpy as np
from pyslave.data import h5todata

# Custom Qwt5 plotting
import plotting

# Dynamically convert ui file to python
Ui_MainWindow, QMainWindow = loadUiType('main_window.ui')
Ui_TextWindow, QMainWindow = loadUiType('text_window.ui')

# Data Model
class H5_manager:
    def __init__(self, filename):
        self.filename = filename
        self.h5file = h5py.File(filename, 'r')
        self.keys = self.h5file.keys()
        self.cursor = 0
        self.range = (None, None)

    def currentpath(self):
        dirname, filename = os.path.split(self.filename)
        return dirname

    def setmin(self):
        self.range = (self.cursor, self.range[1])

    def setmax(self):
        self.range = (self.range[0], self.cursor)

    def select_all(self):
        self.range = (0, len(self.keys)-1)

    def disp(self):
        dataset = self.keys[self.cursor]
        filename = self.filename
        fmin, fmax = self.range
        fmin = '?' if fmin is None else self.keys[fmin]
        fmax = '?' if fmax is None else self.keys[fmax]
        return dataset, filename, fmin, fmax

    def currentdata(self):
        return self.__getitem__(self.cursor)

    def currentfile(self):
        return self.filelist[self.cursor]

    def move(self, direction):
        if direction=='first':
            self.cursor=0
            return
        if direction=='last':
            self.cursor=len(self.keys)-1
            return
        self.cursor = self.cursor + direction
        self.cursor = min(self.cursor, len(self.keys)-1)
        self.cursor = max(self.cursor, 0)

    def __len__(self):
        return len(self.keys)

    def __iter__(self):
        self.iter_cursor = 0
        return self

    def next(self):
        if self.iter_cursor == len(self): raise StopIteration
        d = self.__getitem__(self.iter_cursor)
        self.iter_cursor = self.iter_cursor + 1
        return d

    def __getitem__(self, pos):
        h5ds = self.h5file[self.keys[pos]]
        return h5todata(h5ds)

    def close(self):
        self.h5file.close()


class TextWindow(QtGui.QMainWindow):
    def __init__(self):
        # Create the main window
        super(TextWindow, self).__init__()
        self.ui = Ui_TextWindow()
        self.ui.setupUi(self)
    def settext(self, text):
        self.ui.textBrowser.setText(text)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, filename=None):
        # Create the main window
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Upgrade plot to be a zoomplot and set default values
        self.ui.plot.__class__ = plotting.PlotCurve
        self.ui.plot.__init_modified__(self)
        # Update text display
        self.display()
        self.textwindow = TextWindow()
        # Load a file if given on the command line
        if filename : self.loadfile(filename)

    @QtCore.pyqtSignature("")
    def on_pushButton_Browse_clicked(self):
        dirname = self.filemanager.currentpath() if hasattr(self, 'filemanager') else ''
        filename = QtGui.QFileDialog.getOpenFileName(self, "Pyviewer", dirname, "*.h5")
        if filename : self.loadfile( str(filename) )

    def loadfile(self, filename):
        fm = H5_manager(filename)
        self.reset()
        self.filemanager = fm
        self.movefile(0)

    def reset(self):
        pass

    def loaddata(self, newdata):
        # Print attributes to text window
        self.textwindow.settext("{0} content:\n" + newdata.__repr__() )
        # Get data
        x = newdata[newdata.__data_attributes__[0]]
        y = newdata[newdata.__data_attributes__[1]]
        if any(np.iscomplex(y)) : y = np.abs(y)
        curve = [ (x, y, 'data', None) ]
        self.center = x[y.argmax()]
        self.plotdata(curve, newdata.__data_attributes__[0], newdata.__data_attributes__[1])

    def __autocenter__(self):
        center = self.center
        xmin, xmax = self.ui.plot.getscaleX()
        width = xmax-xmin
        xmin = center-width/2.
        xmax = center+width/2.
        self.ui.plot.rescaleX(xmin,xmax)

    def plotdata(self, curve, xlabel, ylabel):
        self.ui.plot.plot( curve,
                          autoscaleX = not self.ui.plot.isloaded,
                          autoscaleY = self.ui.checkBox_Autoscale.isChecked(),
                          autocenter = self.ui.checkBox_Autocenter.isChecked(),
                          xlabel = xlabel,
                          ylabel = ylabel)


    @QtCore.pyqtSignature("int")
    def on_checkBox_Autoscale_stateChanged(self, val):
        self.ui.plot.autoscale(X=False, Y=val)

    @QtCore.pyqtSignature("int")
    def on_checkBox_Autocenter_stateChanged(self, val):
        if val : self.ui.plot.autocenter()

    @QtCore.pyqtSignature("")
    def on_pushButton_SeeAll_clicked(self):
        self.ui.plot.autoscale()

    def display(self):
        if hasattr(self,'filemanager'):
            dataset, filename, fmin, fmax = self.filemanager.disp()
            self.ui.label_Filename.setText('{0} ({2}/{3}) in {1}'.format(dataset,filename,self.filemanager.cursor+1,len(self.filemanager)))
            self.ui.label_Archive.setText( 'Export {0} to {1}'.format(fmin, fmax) )
        else:
            self.ui.label_Filename.setText('No file')
            self.ui.label_Archive.setText( 'Export ? to ?')

    @QtCore.pyqtSignature("")
    def on_pushButton_Setmin_clicked(self):
        if not hasattr(self,'filemanager'): return
        self.filemanager.setmin()
        self.display()

    @QtCore.pyqtSignature("")
    def on_pushButton_Setmax_clicked(self):
        if not hasattr(self,'filemanager'): return
        self.filemanager.setmax()
        self.display()

    def movefile(self, direction):
        if not hasattr(self,'filemanager'): return
        self.filemanager.move(direction)
        data = self.filemanager.currentdata()
        self.loaddata( data )
        self.display()
        self.textwindow.settext(str(data))

    @QtCore.pyqtSignature("")
    def on_pushButton_fwd_clicked(self):
        self.movefile(+1)
    @QtCore.pyqtSignature("")
    def on_pushButton_ffwd_clicked(self):
        self.movefile(+10)
    @QtCore.pyqtSignature("")
    def on_pushButton_fffwd_clicked(self):
        self.movefile(+100)
    @QtCore.pyqtSignature("")
    def on_pushButton_last_clicked(self):
        self.movefile('last')
    @QtCore.pyqtSignature("")
    def on_pushButton_rwd_clicked(self):
        self.movefile(-1)
    @QtCore.pyqtSignature("")
    def on_pushButton_frwd_clicked(self):
        self.movefile(-10)
    @QtCore.pyqtSignature("")
    def on_pushButton_ffrwd_clicked(self):
        self.movefile(-100)
    @QtCore.pyqtSignature("")
    def on_pushButton_first_clicked(self):
        self.movefile('first')

    @QtCore.pyqtSignature("")
    def on_pushButton_Go_clicked(self):
        if not hasattr(self,'filemanager'): return
        if None in self.filemanager.range : return
        filename = QtGui.QFileDialog.getSaveFileName(self, "Pyviewer", os.path.splitext(self.filemanager.filename)[0], "*.dat")
        filename = str(filename)
        if filename:
            i = 0
            fmin, fmax = self.filemanager.range
            for k in range(fmin,fmax+1) :
                data = self.filemanager[k]
                x = data[data.__data_attributes__[0]]
                y = data[data.__data_attributes__[1]]
                if any(np.iscomplex(y)) :
                    data_txt = np.c_[x, y.real, y.imag]
                else:
                    data_txt = np.c_[x, y]
                np.savetxt('{0}_{1:04d}.dat'.format(filename,k), data_txt)
                if data.__attributes__:
                    with open('{0}_{1:04d}_attrs.txt'.format(filename,k), 'w') as fout:
                        for k2,v2 in data.__attributes__.iteritems():
                            print >> fout,k2,v2
                i+=1
            QtGui.QMessageBox.information(self, "Pyviewer", "{0} files created.".format(i) )



    @QtCore.pyqtSignature("")
    def on_pushButton_ViewText_clicked(self):
        self.textwindow.show()

    def closeEvent(self, event):
        self.textwindow.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    filename = QtCore.QCoreApplication.argv()[1] if QtCore.QCoreApplication.argc()>1 else None
    mainWin = MainWindow(filename)
    mainWin.show()
    sys.exit(app.exec_())
