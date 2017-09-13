from PyQt4 import  Qwt5, Qt, QtGui, QtCore
import numpy as np
import os

class Hcursor(Qwt5.QwtPlotMarker):
        def __init__(self, plot, pos, color=Qt.Qt.black, width=2, invTransform=True):
                Qwt5.QwtPlotMarker.__init__(self)
                if invTransform : pos = plot.invTransform(Qwt5.QwtPlot.yLeft, pos)
                self.setYValue(pos)
                self.setLineStyle(Qwt5.QwtPlotMarker.HLine)
                self.setLinePen(Qt.QPen(color, width, Qt.Qt.SolidLine))
                self.attach(plot)

class Hcursor_pair:
        def __init__(self, plot, pos1, pos2, color=Qt.Qt.black, width=2, invTransform=True):
                self.plot = plot
                self.cursor1 = Hcursor(plot, pos1, color, width, invTransform)
                self.cursor2 = Hcursor(plot, pos2, color, width, invTransform)
                plot.replot()
        def move_cursor1(self, pos, invTransform=True):
                if invTransform : pos = self.plot.invTransform(Qwt5.QwtPlot.yLeft, pos)
                self.cursor1.setYValue(pos)
                self.plot.replot()
        def move_cursor2(self, pos, invTransform=True):
                if invTransform : pos = self.plot.invTransform(Qwt5.QwtPlot.yLeft, pos)
                self.cursor2.setYValue(pos)
                self.plot.replot()
        def getpositions(self):
                pos =  [self.cursor1.yValue(), self.cursor2.yValue()]
                pos.sort()
                return tuple(pos)
        def clear(self):
                self.cursor1.detach()
                self.cursor2.detach()
                self.plot.replot()


class Vcursor(Qwt5.QwtPlotMarker):
        def __init__(self, plot, pos, color=Qt.Qt.black, width=2, invTransform=True):
                Qwt5.QwtPlotMarker.__init__(self)
                if invTransform : pos = plot.invTransform(Qwt5.QwtPlot.xBottom, pos)
                self.setXValue(pos)
                self.setLineStyle(Qwt5.QwtPlotMarker.VLine)
                self.setLinePen(Qt.QPen(color, width, Qt.Qt.SolidLine))
                self.attach(plot)

class Vcursor_pair:
        def __init__(self, plot, pos1, pos2, color=Qt.Qt.black, width=2, invTransform=True):
                self.plot = plot
                self.cursor1 = Vcursor(plot, pos1, color, width, invTransform)
                self.cursor2 = Vcursor(plot, pos2, color, width, invTransform)
                plot.replot()
        def move_cursor1(self, pos, invTransform=True):
                if invTransform : pos = self.plot.invTransform(Qwt5.QwtPlot.xBottom, pos)
                self.cursor1.setXValue(pos)
                self.plot.replot()
        def move_cursor2(self, pos, invTransform=True):
                if invTransform : pos = self.plot.invTransform(Qwt5.QwtPlot.xBottom, pos)
                self.cursor2.setXValue(pos)
                self.plot.replot()
        def getpositions(self):
                pos =  [self.cursor1.xValue(), self.cursor2.xValue()]
                pos.sort()
                return tuple(pos)
        def clear(self):
                self.cursor1.detach()
                self.cursor2.detach()
                self.plot.replot()

class Curve(Qwt5.QwtPlotCurve):
        def __init__(self, x, y, title=Qwt5.QwtText(), color=None, width=1, symbol=None):
                Qwt5.QwtPlotCurve.__init__(self, title if isinstance(title, Qwt5.QwtText) else Qwt5.QwtText(str(title)))
                self.setData(x, y)
                self.color = color
                self.width = width
                self.symbol = symbol
                self.__pen__()
                self.__symbol__()
        def setstyle(self, color=None, width=1, symbol=None):
                self.color = color
                self.width = width
                self.symbol = symbol
                self.__pen__()
                self.__symbol__()
        def setcolor(self, color):
                self.color = color
                self.__pen__()
                self.__symbol__()
        def setsymbol(self, symbol):
                self.symbol = symbol
                self.__symbol__()
        def __symbol__(self):
                s = Qwt5.QwtSymbol()
                if self.symbol is not None :
                        q = Qwt5.QwtSymbol
                        d = {'o':q.Ellipse, '+':q.Cross, 'x':q.XCross, 't':q.Triangle, '*':q.Star1, 's':q.Rect, 'd':q.Diamond }
                        s.setStyle(d[self.symbol])
                        s.setSize(10)
                        color = Qt.Qt.blue if self.color is None else self.color
                        s.setBrush( Qt.QBrush(color) )
                        s.setPen( Qt.QPen(color) )
                self.setSymbol(s)
        def __pen__(self):
                if self.width==0:
                        self.setStyle(Qwt5.QwtPlotCurve.NoCurve)
                        return
                color = Qt.Qt.blue if self.color is None else self.color
                pen = Qt.QPen(color)
                pen.setWidth(self.width)
                self.setPen(pen)


class Image(Qwt5.QwtPlotItem):
    def __init__(self, title = Qwt5.QwtText()):
        Qwt5.QwtPlotItem.__init__(self)
        self.title = title if isinstance(title, Qwt5.QwtText) else Qwt5.QwtText(str(title))
        self.setItemAttribute(Qwt5.QwtPlotItem.Legend);
        self.image = None

    def bytescale(self, data, cmin=None, cmax=None):
        if cmin is None: cmin = data.min()
        if cmax is None: cmax = data.max()
        scale = 255. / (cmax-cmin or 1)
        data -= cmin
        data *= scale
        np.clip(data,0,255,out=data)

    def setData(self, data, cmin=None, cmax=None):
        shape = data.shape
        # Possible shortcut code
        if data.dtype is np.uint8 and cmin==0 and cmax==255:
                if shape[1]%4==0:
                        xyzs = data
                else:
                        xyzs = np.empty( (shape[0], shape[1] + 4 - shape[1]%4), dtype=np.uint8)
                        xyzs[:,:shape[1]] = data
                return
        # Rescale data
        self.bytescale(data, cmin, cmax)
        if shape[1]%4==0:
                xyzs = data.astype(np.uint8)
        else:
                xyzs = np.empty( (shape[0], shape[1] + 4 - shape[1]%4), dtype=np.uint8)
                xyzs[:,:shape[1]] = data
        # Create image
        self.image = Qt.QImage( xyzs, shape[1], shape[0], Qt.QImage.Format_Indexed8 ).mirrored(False, True)
        self.image.setColorTable(jet)

    def setAxes(self, shape, xRange=None, yRange=None):
        if not xRange:
            xRange = (0, shape[1])
        if not yRange:
            yRange = (0, shape[0])
        self.xMap = Qwt5.QwtScaleMap(0, shape[1], *xRange)
        self.plot().setAxisScale(Qwt5.QwtPlot.xBottom, *xRange)
        self.yMap = Qwt5.QwtScaleMap(0, shape[0], *yRange)
        self.plot().setAxisScale(Qwt5.QwtPlot.yLeft, *yRange)

    def updateLegend(self, legend):
        Qwt5.QwtPlotItem.updateLegend(self, legend)
        legend.find(self).setText(self.title)

    def draw(self, painter, xMap, yMap, rect):
        """Paint image zoomed to xMap, yMap

        Calculate (x1, y1, x2, y2) so that it contains at least 1 pixel,
        and copy the visible region to scale it to the canvas.
        """
        if self.image is None : return
        # calculate y1, y2
        # the scanline order (index y) is inverted with respect to the y-axis
        y1 = y2 = self.image.height()
        y1 *= (self.yMap.s2() - yMap.s2())
        y1 /= (self.yMap.s2() - self.yMap.s1()) or 1
        y1 = max(0, int(y1-0.5))
        y2 *= (self.yMap.s2() - yMap.s1())
        y2 /= (self.yMap.s2() - self.yMap.s1()) or 1
        y2 = min(self.image.height(), int(y2+0.5))
        # calculate x1, x2 -- the pixel order (index x) is normal
        x1 = x2 = self.image.width()
        x1 *= (xMap.s1() - self.xMap.s1())
        x1 /= (self.xMap.s2() - self.xMap.s1())
        x1 = max(0, int(x1-0.5))
        x2 *= (xMap.s2() - self.xMap.s1())
        x2 /= (self.xMap.s2() - self.xMap.s1())
        x2 = min(self.image.width(), int(x2+0.5))
        # copy
        image = self.image.copy(x1, y1, x2-x1 or 1, y2-y1 or 1)
        # zoom
        image = image.scaled(xMap.p2()-xMap.p1()+1, yMap.p1()-yMap.p2()+1)
        # draw
        painter.drawImage(xMap.p1(), yMap.p2(), image)

    def reset(self):
        self.image = None

class Spy(Qt.QObject):
    def __init__(self, parent):
        Qt.QObject.__init__(self, parent)
        parent.setMouseTracking(True)
        parent.installEventFilter(self)

    def eventFilter(self, _, event):
        if event.type() == Qt.QEvent.MouseMove:
            self.emit(Qt.SIGNAL("MouseMove"), event.pos())
        return False

class PlotImage(Qwt5.QwtPlot):
        def __init__(self, parent=None, zoom=True, track=True):
                super(PlotImage, self).__init__(parent)
                self.__init_modified__(parent, zoom, track)

        def __init_modified__(self, parent=None, zoom=True, track=True):
                # Set some default values
                self.image = Image()
                self.image.attach(self)
                self.shape = (0,0)
                self.parent = parent
                if zoom  : self.__init_zoomer__()
                if track and parent is not None : self.__init_tracking__()

        def __init_tracking__(self):
                self.spy = Spy(self.canvas())
                self.connect(self.spy, Qt.SIGNAL("MouseMove"), self.showCoordinates)

        def showCoordinates(self, position):
                x = self.invTransform(Qwt5.QwtPlot.xBottom, position.x())
                y = self.invTransform(Qwt5.QwtPlot.yLeft, position.y())
                self.parent.statusBar().showMessage('x = {0:+.6g}, y = {1:+.6g}'.format(x,y))

        def __init_zoomer__(self):
                self.zoomer = Qwt5.QwtPlotZoomer(Qwt5.QwtPlot.xBottom,
                                                Qwt5.QwtPlot.yLeft,
                                                Qwt5.QwtPicker.DragSelection,
                                                Qwt5.QwtPicker.AlwaysOff,
                                                self.canvas())
                self.zoomer.setRubberBandPen(Qt.QPen(Qt.Qt.white))

        def imshow(self, data, xrange = None, yrange = None, cmin=None, cmax=None, xlabel=Qwt5.QwtText(), ylabel=Qwt5.QwtText(), copy=True, reset_axes=False ):
                __data__ = data.astype(float) if copy else data
                self.image.setData(__data__, cmin, cmax)
                if reset_axes or __data__.shape != self.shape:
                        self.image.setAxes(__data__.shape, xrange, yrange)
                        if hasattr(self,'zoomer') : self.zoomer.setZoomBase()
                        self.shape = __data__.shape
                if xlabel is not None : self.setAxisTitle(Qwt5.QwtPlot.xBottom, xlabel)
                if ylabel is not None : self.setAxisTitle(Qwt5.QwtPlot.yLeft, ylabel)
                self.replot()

        def reset(self, replot=True, xlabel=Qwt5.QwtText(), ylabel=Qwt5.QwtText()):
            self.image.detach()
            self.setAxisTitle(Qwt5.QwtPlot.xBottom, xlabel)
            self.setAxisTitle(Qwt5.QwtPlot.yLeft, ylabel)
            self.setTitle('')
            if replot : self.replot()
            self.image.reset()
            self.shape = (0,0)
            self.image.attach(self)

class PlotCurve(Qwt5.QwtPlot):
        def __init__(self, parent=None, zoom=True, track=True):
                super(PlotCurve, self).__init__(parent)
                self.__init_modified__(parent, zoom, track)

        def __init_modified__(self, parent=None, zoom=True, track=True):
                self.parent = parent
                self.setCanvasBackground(Qt.Qt.white)
                # Set some default values
                self.curve = []
                self.isloaded = False
                if zoom :
                        self.leftclic_dragging = False
                        self.rightclic_dragging = False
                        self.canvas().installEventFilter(self)
                if track and parent is not None : self.__init_tracking__()

        def __init_tracking__(self):
                self.spy = Spy(self.canvas())
                self.connect(self.spy, Qt.SIGNAL("MouseMove"), self.showCoordinates)

        def showCoordinates(self, position):
                x = self.invTransform(Qwt5.QwtPlot.xBottom, position.x())
                y = self.invTransform(Qwt5.QwtPlot.yLeft, position.y())
                self.parent.statusBar().showMessage('x = {0:+.6g}, y = {1:+.6g}'.format(x,y))

        def eventFilter(self, object, event):
                # Right button dragging : zoom between horizontal or vertical cursors depending if shift key is pressed
                if event.type() == Qt.QEvent.MouseButtonPress and event.button()==Qt.Qt.RightButton:
                    self.rightclic_dragging = True
                    self.shiftkey = event.modifiers()==Qt.Qt.ShiftModifier
                    self.axis_dragging = Qwt5.QwtPlot.yLeft if self.shiftkey else Qwt5.QwtPlot.xBottom
                    self.cursors = Hcursor_pair(self, event.pos().y(), event.pos().y()) if self.shiftkey else Vcursor_pair(self, event.pos().x(), event.pos().x())
                elif event.type() == Qt.QEvent.MouseMove and self.rightclic_dragging:
                    self.cursors.move_cursor2(event.pos().y() if self.shiftkey else event.pos().x())
                elif event.type() == Qt.QEvent.MouseButtonRelease and event.button()==Qt.Qt.RightButton:
                    self.rightclic_dragging = False
                    min, max =  self.cursors.getpositions()
                    self.cursors.clear()
                    del self.cursors
                    if self.shiftkey:
                        self.rescaleY(min, max)
                    else:
                        self.rescaleX(min, max)
                # Left button dragging : move curve left-right or up-down depending if shift key is pressed
                elif event.type() == Qt.QEvent.MouseButtonPress and event.button()==Qt.Qt.LeftButton:
                     self.leftclic_dragging = True
                     self.shiftkey = event.modifiers()==Qt.Qt.ShiftModifier
                     self.axis_dragging = Qwt5.QwtPlot.yLeft if self.shiftkey else Qwt5.QwtPlot.xBottom
                     self.initialpos = event.pos().y() if self.shiftkey else event.pos().x()
                     self.scaling = self.invTransform(self.axis_dragging, 1)-self.invTransform(self.axis_dragging, 0)
                elif event.type() == Qt.QEvent.MouseMove and self.leftclic_dragging:
                     newpos = event.pos().y() if self.shiftkey else event.pos().x()
                     shift = (self.initialpos-newpos)*self.scaling
                     self.initialpos = newpos
                     min = self.axisScaleDiv(self.axis_dragging).lowerBound()
                     max = self.axisScaleDiv(self.axis_dragging).upperBound()
                     min += shift
                     max += shift
                     if self.shiftkey:
                        self.rescaleY(min, max)
                     else:
                        self.rescaleX(min, max)
                elif event.type() == Qt.QEvent.MouseButtonRelease and event.button()==Qt.Qt.LeftButton:
                     self.leftclic_dragging = False
                # Mouse wheel to zoom in and out
                elif event.type()==Qt.QEvent.Wheel:
                     factor = -event.delta()/10.
                     if event.modifiers()==Qt.Qt.ShiftModifier:
                        ymin = self.axisScaleDiv(Qwt5.QwtPlot.yLeft).lowerBound()
                        ymax = self.axisScaleDiv(Qwt5.QwtPlot.yLeft).upperBound()
                        height =  ymax-ymin
                        height = height*(1.01**factor)
                        ymax = ymin+height
                        self.rescaleY(ymin, ymax)
                     else:
                        xmin = self.axisScaleDiv(Qwt5.QwtPlot.xBottom).lowerBound()
                        xmax = self.axisScaleDiv(Qwt5.QwtPlot.xBottom).upperBound()
                        width =  xmax-xmin
                        center = (xmax+xmin)/2.
                        width = width*(1.01**factor)
                        xmin = center-width/2.
                        xmax = center+width/2.
                        self.rescaleX(xmin, xmax)
                return False

        def rescaleX(self, xmin, xmax, replot=True):
                self.setAxisScale(Qwt5.QwtPlot.xBottom, xmin, xmax)
                if replot : self.replot()

        def rescaleY(self, ymin, ymax, replot=True):
                self.setAxisScale(Qwt5.QwtPlot.yLeft, ymin, ymax)
                if replot : self.replot()

        def getscaleX(self):
                axdiv = self.axisScaleDiv(Qwt5.QwtPlot.xBottom)
                return axdiv.lowerBound(), axdiv.upperBound()

        def getscaleY(self):
                axdiv = self.axisScaleDiv(Qwt5.QwtPlot.yLeft)
                return axdiv.lowerBound(), axdiv.upperBound()

        def setautoscaleX(self, val):
                if val:
                        self.setAxisAutoScale(Qwt5.QwtPlot.xBottom)
                else:
                        self.rescaleX(*self.getscaleX())

        def setautoscaleY(self, val):
                if val:
                        self.setAxisAutoScale(Qwt5.QwtPlot.yLeft)
                else:
                        self.rescaleY(*self.getscaleY())

        def autoscale(self, X=True, Y=True):
            oldX = self.axisAutoScale(Qwt5.QwtPlot.xBottom)
            oldY = self.axisAutoScale(Qwt5.QwtPlot.yLeft)
            self.setautoscaleX(X)
            self.setautoscaleY(Y)
            self.replot()
            self.setautoscaleX(oldX)
            self.setautoscaleY(oldY)

        def __autocenter__(self):
            if hasattr(self.parent, '__autocenter__'):
                self.parent.__autocenter__()

        def autocenter(self):
            self.__autocenter__()
            self.replot()

        def reset(self, replot=True, xlabel=Qwt5.QwtText(), ylabel=Qwt5.QwtText(), title=Qwt5.QwtText()):
            # Erase old data and restore default value
            for c in self.curve:
                    c.detach()
            self.curve = []
            self.isloaded = False
            self.setAxisTitle(Qwt5.QwtPlot.xBottom, xlabel)
            self.setAxisTitle(Qwt5.QwtPlot.yLeft, ylabel)
            self.setTitle(title)
            if replot : self.replot()

        def plot(self, curve_list, xlabel=Qwt5.QwtText(), ylabel=Qwt5.QwtText(), autoscaleX=True, autoscaleY=True, autocenter=False, title=Qwt5.QwtText()):
            # Set Axis
            self.setautoscaleX(autoscaleX)
            self.setautoscaleY(autoscaleY)
            self.reset(xlabel=xlabel, ylabel=ylabel, title=title)
            # Create curves
            self.addcurve(*curve_list)
            # Autocenter
            if autocenter : self.__autocenter__()
            # Plot
            self.isloaded = True
            self.replot()

        def addcurve(self, *curve_list):
            # Create curves
            for c in curve_list :
                newcurve = c if type(c)==Curve else Curve(*c)
                self.curve.append(newcurve)
                if newcurve.color is None : newcurve.setcolor(colors[ len(self.curve)-1 ])
                newcurve.attach(self)

def __paint__(device, title, text, plot, width, height):
        page = QtGui.QPainter()
        page.begin(device)
        # Title, graph and bottom text areas
        titleRect = QtCore.QRect(0,0,width,height/10)
        graphRect = QtCore.QRect(0,height/10,width,height/2)
        bottomRect = QtCore.QRect()
        bottomRect.setTopLeft(graphRect.bottomLeft())
        bottomRect.setBottomRight( QtCore.QPoint(width, height) )
        # Title
        font = QtGui.QFont()
        font.setPointSize(24)
        page.setFont(font)
        page.drawText(titleRect, Qt.Qt.AlignCenter, title)
        # Graph
        plot.print_(page, graphRect)
        # Bottom text
        font.setPointSize(10)
        page.setFont(font)
        page.drawText(bottomRect, Qt.Qt.AlignLeft, text)
        page.end()

def __export_pdf__(plot, filename, title, text):
        # Printer initialization
        printer = QtGui.QPrinter()
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setPageSize(QtGui.QPrinter.A4)
        if os.path.isfile(filename) : os.remove(filename)
        printer.setOutputFileName(filename)
        printer.setOrientation(QtGui.QPrinter.Portrait)
        printer.setResolution(600)
        __paint__(printer, title, text, plot, printer.pageRect().width(), printer.pageRect().height())

def __export_pic__(plot, filename, title, text):
        pic = QtGui.QImage(572, 818, QtGui.QImage.Format_RGB16)
        pic.fill( QtGui.QColor('white') )
        if os.path.isfile(filename) : os.remove(filename)
        __paint__(pic, title, text, plot, 572, 818)
        pic.save(filename)

def export(plot, filename, title='', text=''):
        filename = str(filename)
        if filename.endswith('.pdf'):
                __export_pdf__(plot, filename, title, text)
        elif filename.endswith('.png') or filename.endswith('.jpg'):
                __export_pic__(plot, filename, title, text)
        else:
                print 'Export : unknown export format'


colors = [ Qt.Qt.blue, Qt.Qt.green, Qt.Qt.red, Qt.Qt.darkYellow, Qt.Qt.magenta, Qt.Qt.darkCyan, Qt.Qt.black, Qt.Qt.cyan, Qt.Qt.darkRed, Qt.Qt.darkGreen, Qt.Qt.yellow, Qt.Qt.darkMagenta, Qt.Qt.gray, Qt.Qt.darkBlue, Qt.Qt.lightGray ]

jet = [(0, 0, 128),
(0, 0, 132),
(0, 0, 137),
(0, 0, 141),
(0, 0, 146),
(0, 0, 150),
(0, 0, 155),
(0, 0, 159),
(0, 0, 164),
(0, 0, 168),
(0, 0, 173),
(0, 0, 178),
(0, 0, 182),
(0, 0, 187),
(0, 0, 191),
(0, 0, 196),
(0, 0, 200),
(0, 0, 205),
(0, 0, 209),
(0, 0, 214),
(0, 0, 218),
(0, 0, 223),
(0, 0, 227),
(0, 0, 232),
(0, 0, 237),
(0, 0, 241),
(0, 0, 246),
(0, 0, 250),
(0, 0, 255),
(0, 0, 255),
(0, 0, 255),
(0, 0, 255),
(0, 1, 255),
(0, 4, 255),
(0, 9, 255),
(0, 13, 255),
(0, 17, 255),
(0, 20, 255),
(0, 25, 255),
(0, 29, 255),
(0, 33, 255),
(0, 36, 255),
(0, 41, 255),
(0, 45, 255),
(0, 49, 255),
(0, 52, 255),
(0, 57, 255),
(0, 61, 255),
(0, 65, 255),
(0, 68, 255),
(0, 73, 255),
(0, 77, 255),
(0, 81, 255),
(0, 84, 255),
(0, 89, 255),
(0, 93, 255),
(0, 97, 255),
(0, 100, 255),
(0, 105, 255),
(0, 109, 255),
(0, 113, 255),
(0, 116, 255),
(0, 121, 255),
(0, 125, 255),
(0, 129, 255),
(0, 133, 255),
(0, 136, 255),
(0, 141, 255),
(0, 145, 255),
(0, 149, 255),
(0, 153, 255),
(0, 157, 255),
(0, 161, 255),
(0, 165, 255),
(0, 168, 255),
(0, 173, 255),
(0, 177, 255),
(0, 181, 255),
(0, 185, 255),
(0, 189, 255),
(0, 193, 255),
(0, 197, 255),
(0, 200, 255),
(0, 205, 255),
(0, 209, 255),
(0, 213, 255),
(0, 217, 255),
(0, 221, 254),
(0, 225, 251),
(0, 229, 248),
(2, 232, 244),
(6, 237, 241),
(9, 241, 238),
(12, 245, 235),
(15, 249, 231),
(19, 253, 228),
(22, 255, 225),
(25, 255, 222),
(28, 255, 219),
(31, 255, 215),
(35, 255, 212),
(38, 255, 209),
(41, 255, 206),
(44, 255, 202),
(48, 255, 199),
(51, 255, 196),
(54, 255, 193),
(57, 255, 190),
(60, 255, 186),
(64, 255, 183),
(67, 255, 180),
(70, 255, 177),
(73, 255, 173),
(77, 255, 170),
(80, 255, 167),
(83, 255, 164),
(86, 255, 160),
(90, 255, 157),
(93, 255, 154),
(96, 255, 151),
(99, 255, 148),
(102, 255, 144),
(106, 255, 141),
(109, 255, 138),
(112, 255, 135),
(115, 255, 131),
(119, 255, 128),
(122, 255, 125),
(125, 255, 122),
(128, 255, 119),
(131, 255, 115),
(135, 255, 112),
(138, 255, 109),
(141, 255, 106),
(144, 255, 102),
(148, 255, 99),
(151, 255, 96),
(154, 255, 93),
(157, 255, 90),
(160, 255, 86),
(164, 255, 83),
(167, 255, 80),
(170, 255, 77),
(173, 255, 73),
(177, 255, 70),
(180, 255, 67),
(183, 255, 64),
(186, 255, 60),
(190, 255, 57),
(193, 255, 54),
(196, 255, 51),
(199, 255, 48),
(202, 255, 44),
(206, 255, 41),
(209, 255, 38),
(212, 255, 35),
(215, 255, 31),
(219, 255, 28),
(222, 255, 25),
(225, 255, 22),
(228, 255, 19),
(231, 255, 15),
(235, 255, 12),
(238, 255, 9),
(241, 252, 6),
(244, 248, 2),
(248, 245, 0),
(251, 241, 0),
(254, 237, 0),
(255, 234, 0),
(255, 230, 0),
(255, 226, 0),
(255, 222, 0),
(255, 219, 0),
(255, 215, 0),
(255, 211, 0),
(255, 208, 0),
(255, 204, 0),
(255, 200, 0),
(255, 196, 0),
(255, 193, 0),
(255, 189, 0),
(255, 185, 0),
(255, 182, 0),
(255, 178, 0),
(255, 174, 0),
(255, 171, 0),
(255, 167, 0),
(255, 163, 0),
(255, 159, 0),
(255, 156, 0),
(255, 152, 0),
(255, 148, 0),
(255, 145, 0),
(255, 141, 0),
(255, 137, 0),
(255, 134, 0),
(255, 130, 0),
(255, 126, 0),
(255, 122, 0),
(255, 119, 0),
(255, 115, 0),
(255, 111, 0),
(255, 108, 0),
(255, 104, 0),
(255, 100, 0),
(255, 96, 0),
(255, 93, 0),
(255, 89, 0),
(255, 85, 0),
(255, 82, 0),
(255, 78, 0),
(255, 74, 0),
(255, 71, 0),
(255, 67, 0),
(255, 63, 0),
(255, 59, 0),
(255, 56, 0),
(255, 52, 0),
(255, 48, 0),
(255, 45, 0),
(255, 41, 0),
(255, 37, 0),
(255, 34, 0),
(255, 30, 0),
(255, 26, 0),
(255, 22, 0),
(255, 19, 0),
(250, 15, 0),
(246, 11, 0),
(241, 8, 0),
(237, 4, 0),
(232, 0, 0),
(228, 0, 0),
(223, 0, 0),
(218, 0, 0),
(214, 0, 0),
(209, 0, 0),
(205, 0, 0),
(200, 0, 0),
(196, 0, 0),
(191, 0, 0),
(187, 0, 0),
(182, 0, 0),
(178, 0, 0),
(173, 0, 0),
(168, 0, 0),
(164, 0, 0),
(159, 0, 0),
(155, 0, 0),
(150, 0, 0),
(146, 0, 0),
(141, 0, 0),
(137, 0, 0),
(132, 0, 0),
(128, 0, 0),
]

jet = [QtGui.qRgb(r,g,b) for r,g,b in jet]
