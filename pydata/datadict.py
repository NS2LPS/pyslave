import sys
import numpy as np
import h5py
from pydata.h5pydata import Group_autoiter, h5file
from pydata.increment import increment_file, __increment__

if 'pyslave' in sys.modules :   
    from pyslave import __slave_disp__ as disp
else:
    disp = print


# Error class
class DataException(Exception):
    pass


class Data(dict):
    """Base class to represent experimental data. Inherits from dict.

    Values stored in the object can be accessed via attributes or keys.
    Data attributes will be saved as an array by the save methods.
    Normal attributes will be discarded when saving in text format and saved
    as attributes in the HDF5 format.

    Data object can be created by the createdata function."""
    def __init__(self, *args, **kwargs):
        """Creates a Data instance from key,value pairs.
        Any valid syntax to create a Python dict is allowed.
        Keys corresponding to numpy arrays are added to the data attributes."""
        super().__init__()
        self.__data_attributes__ = []
        if args:
            if len(args)>1:
                raise DataException('Expected at most 1 arguments, got {0}'.format(len(args)))
            if isinstance(args[0],dict):
                for k,v in args[0].items():
                    if k in self :  raise DataException('Duplicate key {0}'.format(k))
                    self[k] = v
            elif hasattr(args[0],'__iter__'):
                for k,v in args[0]:
                    if k in self :  raise DataException('Duplicate key {0}'.format(k))
                    self[k] = v
            else:
                raise DataException('Argument should be a mapping or an iterable')
        if kwargs:
            for k,v in kwargs.items():
                if k in self :  raise DataException('Duplicate key {0}'.format(k))
                self[k] = v
        self.set_data_attributes()
        self.set_hidden_attributes()
    def set_data_attributes(self):
        pass
    def set_hidden_attributes(self):
        self.__hidden_attributes__ = ['__hidden_attributes__','__data_attributes__']
    def __getattr__(self, name):
        return self[name]
    def __setattr__(self, name, value):
        self[name] = value
    def __delitem__(self, key):
        super().__delitem__(key)
        if key in self.__data_attributes__ : self.__data_attributes__.remove(key)
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if key in self.__data_attributes__ : self.__data_attributes__.remove(key)
        if type(value)==np.ndarray : self.__data_attributes__.append(key)
    def __delattr__(self, name):
        self.__delitem__(name) 
    def update(self,*args,**kwargs):
        for a in args:
            if type(a)==dict:
                for k,v in a.items():
                    self.__setitem__(k,v)
            elif type(a)==list or type(a)==tuple:
                for k,v in a:
                    self.__setitem__(k,v)
        for k,v in kwargs.items():
            self.__setitem__(k,v)
    def plot(self, fig, subplots=True, **kwargs):
        """Plot data to a figure.
        If subplots is True each data is plotted in a different subplot."""
        __data_attributes__ = self.__data_attributes__
        l = len(__data_attributes__)
        fig.clf()
        if subplots:
            ax = [ fig.add_subplot(l-1,1,i) for i in range(1, l) ]
        else:
            ax = fig.add_subplot(1,1,1)
            ax = [ax for i in range(1, l) ]
        for i,a in enumerate(ax):
            x = self[__data_attributes__[0]]
            y = self[__data_attributes__[i+1]]
            a.plot(x, y, **kwargs)
            a.set_xlabel(__data_attributes__[0])
            a.set_ylabel(__data_attributes__[i+1])
            a.get_xaxis().get_major_formatter().set_powerlimits((-1, 2))
            a.get_yaxis().get_major_formatter().set_powerlimits((-1, 2))
    def append(self, *args):
        if len(args)!=len(self.__data_attributes__):
            raise DataException('Number of arguments does not match number of data fields : ' + ' '.join(self.__data_attributes__))
        data_attributes = self.__data_attributes__.copy()
        for i,v in enumerate(args):
            k = data_attributes[i] 
            self[k] = np.append(self[k], v)
    @property
    def __data__(self):
        return np.core.rec.fromarrays( [self[k] for k in self.__data_attributes__] , names = self.__data_attributes__)
    @property
    def __attributes__(self):
        return dict([ (k,v) for k,v in self.items() if k not in self.__data_attributes__ and k not in self.__hidden_attributes__])
    def __repr__(self):
        out = "Data:\n"
        out += '\n'.join( [ '{0} : {1}'.format(k, self[k].__repr__()) for k in self.__data_attributes__])
        if self.__attributes__:
            out += "\nAttributes:\n"
            out += '\n'.join( [ '{0} : {1}'.format(k, self[k].__repr__()) for k in self.__attributes__])
        return out
    def save(self, file, **kwargs):
        """Save the data to a file in text or HDF5 format.

        * Text format : used if file is a string ending in txt.
          The optional keywords are increment=True and ndigits=4 to control
          the behaviour of the filename autoincrement (see the save_txt method
          for more details).

        * HDF5 format : used if file is an HDF5 file object or a string ending in h5.
          The optional keywords are increment=True and ndigits=4 to control the
          behaviour of the dataset autoincrement. The optional attrs will
          be added to the dataset attributes. Extra keywords arguments will be
          passed to the hDF5 create_dataset function (see the save_h5 method for
          more details).

        """
        if type(file)==str:
            if file.endswith('txt'):
                self.save_txt(file, **kwargs)
            elif file.endswith('h5'):
                with h5file(file, 'a', libver='latest') as hdf:
                    self.save_h5(hdf, **kwargs)
            else:
                raise Exception('Unknown file extension : {0}'.format(file))
        elif isinstance(file, h5py.Group) or type(file)==Group_autoiter:
            self.save_h5(file, **kwargs)
        else :
            raise TypeError('File should be a string or an opened HDF file.')

    def __save_txt__(self, filename, data, attrs, increment, ndigits):
        attributes = self.__attributes__.copy()
        if attrs : attributes.update(attrs)
        if increment : filename = increment_file(filename, ndigits)
        np.savetxt(filename, data)
        msg = 'Data saved to {0}.'.format(str(filename))
        disp(msg)
        if attrs:
            with open(filename[:-4]+'_attrs.txt', 'w') as f:
                for k,v in attrs.items():
                    print >>f,k,v

    def save_txt(self, filename, attrs=None, increment=True, ndigits=4):
        """Save the data to a text file.
        If increment is True, the filename is automatically incremented and will contain a ndigits integer.
        The non data attributes are saved in a companion text file together with the extra attributes passed in attrs.
        """
        self.__save_txt__(filename, self.__data__, attrs, increment, ndigits)

    def __save_h5__(self, hdf, data, dataset, attrs, increment, ndigits, **kwargs):
        attributes = self.__attributes__.copy()
        if attrs : attributes.update(attrs)
        if increment:
            if type(hdf)==Group_autoiter:
                # fast
                counter, dataset_name = hdf.__next_dataset__(dataset, ndigits)
            else:
                # slow
                dataset_name = __increment__(dataset, '', hdf.keys(), ndigits)
        else:
            dataset_name = dataset
        #if dataset_name in hdf:
        #    print('WARNING : Deleting {0} in {1}'.format(dataset_name, str(hdf.file.filename+hdf.name)))
        #    del hdf['{0}'.format(dataset_name)]
        opts = {'track_order' : True}
        kwargs.update(opts)
        if type(hdf)==Group_autoiter:
            hdf.create_dataset(dataset_name, data=data, attrs=attributes, **opts)
        else:
            ds = hdf.create_dataset(dataset_name, data=data, **opts)
            ds.attrs.update(attributes)
        if increment and type(hdf)==Group_autoiter:
            hdf.__data_counter__[dataset] = counter
        msg = 'Data saved to {0} in dataset {1}.'.format(str(hdf.file.filename + hdf.name), dataset_name)
        disp(msg)

    def save_h5(self, hdf, dataset='data', attrs=None, increment=True, ndigits=4, **kwargs):
        """Save the data to a HDF5 dataset. The first parameter hdf must a HDF5 file opened for writing.
        If increment is True, the name of the dataset is automatically incremented and will contain a ndigits integer.
        The non data attributes are saved as HDF5 attributes together with the extra attributes passed in attrs.
        The file is flushed after the dataset is inserted.
        Optional arguments are passed to the create_dataset function (e.g. compression='gzip').
        """
        self.__save_h5__(hdf, self.__data__, dataset, attrs, increment, ndigits, **kwargs)


class Sij(Data):
    """Vector network analyzer Sij data class.

    * Data attributes : freq, S12 (complex)
    * Attributes : start_frequency, stop_frequency, number_of_points, power

    """
    def set_data_attributes(self):
        self.__data_attributes__ = ['freq','Sij']
    def __getitem__(self, key):
        if key=='freq':
            return np.linspace(self.start_frequency, self.stop_frequency, self.number_of_points)
        else:
            return self.get(key)
    def plot(self, fig, scale='log', **kwargs):
        """Plot data to a figure.
        """
        fig.clf()
        ax = fig.add_subplot(1,1,1)
        y = 10*np.log10( np.abs(self.Sij)**2 ) if scale=='log' else np.abs(self.Sij)**2
        ax.plot(self.freq/1e9, y, **kwargs)
        ax.set_xlabel('Frequency (GHz)')
        ax.set_ylabel('$|S_{ij}|^2$ (dB)' if scale=='log' else '$|S_{ij}|^2$')
        ax.get_xaxis().get_major_formatter().set_powerlimits((-1, 2))
        ax.get_yaxis().get_major_formatter().set_powerlimits((-1, 2))
    def save_txt(self, filename, attrs=None, increment=True, ndigits=4):
        """Save the data to a text file with three columns : freq, Sij.real, Sij.imag."""
        data = self.__data__
        data = np.c_[data['freq'], data['Sij'].real, data['Sij'].imag]
        self.__save_txt__(filename, data, attrs, increment, ndigits)

class Spec(Data):
    """Spectrum Analyzer data class.

    * Data attributes : freq, S
    * Attributes : start_frequency, stop_frequency, number_of_points

    """
    def set_data_attributes(self):
        self.__data_attributes__ = ['freq','S']
    def __getitem__(self, key):
        if key=='freq':
            return np.linspace(self.start_frequency, self.stop_frequency, self.number_of_points)
        else:
            return self.get(key)
    def plot(self, fig, **kwargs):
        """Plot data to a figure.
        """
        fig.clf()
        ax = fig.add_subplot(1,1,1)
        y = self.S
        ax.plot(self.freq/1e9, y, **kwargs)
        ax.set_xlabel('Frequency (GHz)')
        ax.set_ylabel('$S$ (dB)')
        ax.get_xaxis().get_major_formatter().set_powerlimits((-1, 2))
        ax.get_yaxis().get_major_formatter().set_powerlimits((-1, 2))
    def save_txt(self, filename, attrs=None, increment=True, ndigits=4):
        """Save the data to a text file with two columns : freq, S."""
        data = self.__data__
        data = np.c_[data['freq'], data['S']]
        self.__save_txt__(filename, data, attrs, increment, ndigits)

class Lecroy_trace(Data):
    """Lecroy oscilloscope waveform data class.

    * Data attributes : horiz, vert
    * Attributes : horiz_interval, horiz_offset, sweeps_per_acq, bandwidth_limit, vertical_gain, vertical_offset, vert_coupling, acq_vert_offset, probe_att

    """
    def set_data_attributes(self):
        self.__data_attributes__ = ['horiz','vert']
    def set_hidden_attributes(self):
        self.__hidden_attributes__ = ['wave','__hidden_attributes__','__data_attributes__']
    def plot(self, fig, **kwargs):
        """Plot data to a figure.
        """
        fig.clf()
        ax = fig.add_subplot(1,1,1)
        ax.plot(self.horiz, self.vert, **kwargs)
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Voltage (V)')
        ax.get_xaxis().get_major_formatter().set_powerlimits((-1, 2))
        ax.get_yaxis().get_major_formatter().set_powerlimits((-1, 2))

    def __getitem__(self, key):
        if key=='horiz':
            x = np.arange( len(self.wave) ) * self.horiz_interval
            x += self.horiz_offset
            return x
        elif key=='vert':
            y = self.wave.astype(np.float)
            y *= self.vertical_gain
            y -= self.vertical_offset
            return y
        else:
            return self.get(key)

    def save_h5(self, hdf, dataset='data', attrs=None, increment=True, ndigits=4, **kwargs):
        """Save data in 8 bit mode."""
        self.__save_h5__(hdf, self.wave, dataset, attrs, increment, ndigits, **kwargs)


class xy(Data):
    """Generic x,y data class.

    * Data Attributes : x, y
    """
    def set_data_attributes(self):
        self.__data_attributes__ = ['x', 'y']


def h5todata(h5_dataset):
    """Create a data instance from a H5 dataset.

    Example::
        f = h5py.File('myfile.h5')
        mydata = h5todata(f['data0000'])
        print(mydata)

    """
    res = Data( [ (n, np.array(h5_dataset[n])) for n in h5_dataset.dtype.names] )
    res.update(dict(h5_dataset.attrs))
    return res


def createdata(*args):
    """Create an empty data instance (see the data class).

    Expects string arguments that will refer to the name of the data fields. For example::
        mydata = createdata('i', 'v', 'Rc')

    Data points can be added with the append method::
        mydata.append(i_value, v_value, Rc_value)

    Parameters (non-data) fields are appended as dictionary (key,values) or as attributes::
        mydata['lockin frequency'] = 77.0
        madata.lockin_amplitude = 0.1

    Data can be saved with the save method:::
        mydata.save('mydata.txt')

    Data can be plotted with the plot method:::
        fig, ax = subplots()
        mydata.plot(ax)

    """
    res = Data([(k, np.empty(0)) for k in args])
    return res
