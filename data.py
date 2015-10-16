import os, re, logging
import numpy as np
import h5py

# Logger
logger = logging.getLogger('pyslave.data')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

def __increment__(base, ext, previous, ndigits):
    rec = re.compile(base+'[0-9]*'+ext)
    index = [p[len(base):] for p in previous if rec.match(p)]
    if ext : index = [ p[:-len(ext)] for p in index]
    index = [ int(p) for p in index]
    if index :
        index.sort()
        counter = index[-1]+1
    else :
        counter = 0
    return base + str(counter).zfill(ndigits) + ext

def increment_file(filename, ndigits=4):
    """Return a filename with an automatically incremented number at the end.
    The number is zero padded to have ndigits."""
    basename = filename.rsplit('.',1)[0] if '.' in filename else filename
    ext = '.'+filename.rsplit('.',1)[1] if '.' in filename else ''
    files = os.listdir('.')
    return __increment__(basename, ext, files, ndigits)

class data(dict):
    """Base class to represent experimental data. Values stored in the object can be accessed via attributes or keys.
    Data attributes will be saved as an array by the save methods.
    Normal attributes will be discarded when saving in text format and saved as attributes in the HDF5 format."""
    __data_attributes__ = []
    __hidden_attributes__ = []
    def __getattr__(self, name):
        return self[name]
    def __setattr__(self, name, value):
        self[name] = value
    def __delattr__(self, name):
        del self[name]
    def plot(self, ax, **kwargs):
        x = self[__data_attributes__[0]]
        y = self[__data_attributes__[1]]        
        ax.plot(x, y, **kwargs)
        ax.set_xlabel(__data_attributes__[0])
        ax.set_ylabel(__data_attributes__[1])
    @property
    def __data__(self):
        return np.core.rec.fromarrays( [self[k] for k in self.__data_attributes__] , names = self.__data_attributes__)
    @property
    def __attributes__(self):
        return dict([ (k,v) for k,v in self.iteritems() if k not in self.__data_attributes__ and k not in self.__hidden_attributes__])
    def save(self, file, **kwargs):
        """Save the data to a file in text or HDF5 format.

        - Text format : used if file is a string ending in txt.
            The optional keywords are increment=True and ndigits=4 to control the behaviour of the filename autoincrement (see the save_txt method for more details).

        - HDF5 format : used if file is an opened HDF5 file or a string ending in h5.
            The optional keywords are increment=True and ndigits=4 to control the behaviour of the dataset autoincrement.
            The optional attrs=dict() will be added to the dataset attributes. Extra keywords arguments will be passed to the hDF5 create_dataset function
            (see the save_h5 method for more details).

        """
        if type(file) is str:
            if file.endswith('txt'):
                self.save_txt(file, **kwargs)
            elif file.endswith('h5'):
                with h5py.File(file, 'a') as hdf:
                    self.save_h5(hdf, **kwargs)
            else:
                raise Exception('Unknown file extension : {0}'.format(file))
        elif type(file) is h5py._hl.files.File:
            self.save_h5(file, **kwargs)
        else :
            raise TypeError('File should be a string or an opened HDF file.')
    def save_txt(self, filename, increment=True, ndigits=4):
        """Save the data to a text file. If increment is True, the filename is automatically incremented and will contain a ndigits integer."""
        if increment : filename = increment_file(filename, ndigits)
        np.savetxt(filename, self.__data__)
        msg = 'Data saved to {0}.'.format(str(filename))
        logger.info(msg)
        print msg
    def save_h5(self, hdf, dataset='data', attrs=dict(), increment=True, ndigits=4, **kwargs):
        """Save the data to a HDF5 dataset. The first parameter hdf must a HDF5 file opened for writing.
        If increment is True, the name of the dataset is automatically incremented and will contain a ndigits integer.
        The non data attributes are saved as HDF5 attributes together with the extra attributes passed in attrs.
        The file is flushed after the dataset is inserted.
        Optional arguments are passed to the create_dataset function (e.g. compression='gzip').
        """
        attrs.update(self.__attributes__)
        if increment : dataset = __increment__(dataset, '', hdf.keys(), ndigits)
        if dataset in hdf: del hdf['{0}'.format(dataset)]
        ds = hdf.create_dataset(dataset, data=self.__data__, **kwargs)
        for k,v in attrs.iteritems() :
            ds.attrs[k] = v
        hdf.flush()
        msg = 'Data saved to {0} in dataset {1}.'.format(str(hdf.filename), dataset)
        logger.info(msg)
        print msg

class Sij(data):
    """Vector network analyzer Sij data class.

    * Data attributes : freq, S12 (complex)
    * Attributes : start_frequency, stop_frequency, number_of_points, power
    """
    __data_attributes__ = ['freq','Sij']
    def __getitem__(self, key):
        if key is 'freq':
            return np.linspace(self.start_frequency, self.stop_frequency, self.number_of_points)
        else:
            return self.get(key)
    def plot(self, ax, scale='log', **kwargs):
        y = 10*np.log10( np.abs(self.Sij)**2 ) if scale is 'log' else np.abs(self.Sij)**2
        ax.plot(self.freq/1e9, y, **kwargs)
        ax.set_xlabel('Frequency (GHz)')
        ax.set_ylabel('$|S_{ij}|^2$ (dB)' if scale is 'log' else '$|S_{ij}|^2$')
    def save_txt(self, filename, increment=True, ndigits=4):
        """Save the data to a text file with three columns : freq, Sij.real, Sij.imag."""
        if increment : filename = increment_file(filename, ndigits)
        data = self.__data__
        data = np.c_[data['freq'], data['Sij'].real, data['Sij'].imag]
        np.savetxt(filename, data)
        msg = 'Data saved to {0}.'.format(str(filename))
        logger.info(msg)
        print msg

class lecroy_trace(data):
    """Lecroy oscilloscope waveform data class.

    * Data attributes : horiz, vert
    * Attributes : horiz_interval, horiz_offset, sweeps_per_acq, bandwidth_limit, vertical_gain, vertical_offset, vert_coupling, acq_vert_offset, probe_att
    """
    __data_attributes__ = ['horiz','vert']
    __hidden_attributes__ = ['wave']
    def plot(self, ax, **kwargs):
        ax.plot(self.horiz, self.vert, **kwargs)
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Voltage (V)')
    def __getitem__(self, key):
        if key is 'horiz':
            x = np.arange( len(self.wave) ) * self.horiz_interval
            x += self.horiz_offset
            return x
        elif key is 'vert':
            y = self.wave.astype(np.float)
            y *= self.vertical_gain
            y -= self.vertical_offset
            return y
        else:
            return self.get(key)
