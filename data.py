import os, re, logging
import numpy as np
import h5py

# Logger
logger = logging.getLogger('pyslave.data')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

def __increment__(base, ext, previous, ndigits):
    rec = re.compile(base+'[0-9]*'+ext)
    previous = [p for p in previous if rec.match(p)]
    if previous :
        previous.sort()
        last = previous[-1]
        counter = last[len(base):]
        if ext : counter = counter[:-len(ext)]
        counter = int(counter)+1 if counter else 0
    else :
        counter = 0
    return base + str(counter).zfill(ndigits) + ext

def increment_file(filename, ndigits=3):
    """Return a filename with an automatically incremented number at the end.
    The number is zero padded to have ndigits."""
    basename = filename.rsplit('.',1)[0] if '.' in filename else filename
    ext = '.'+filename.rsplit('.',1)[1] if '.' in filename else ''
    files = os.listdir('.')
    return __increment__(basename, ext, files, ndigits)

class data(dict):
    """Base class to represent data acquired with instruments. Specific values stored in the data can be accessed via attributes or keys.
    Special data values will be concatenated and saved as an array by the save methods.
    Normal values will be discarded when saving in text format and saved as attributes in the HDF5 format."""
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute : " + name)
    def __setattr__(self, name, value):
        self[name] = value
    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute : " + name)
    def plot(self, ax, **kwargs):
        pass
    @property
    def __data__(self):
        pass
    @property
    def __attributes__(self):
        pass
    def save(self, file, **kwargs):
        """Save the data to a file in text or HDF5 format.

        - Text format : used if file is a string ending in 'txt'.
        The optional keywords are increment=True and ndigits=3 to control the behaviour of the filename autoincrement (see the save_txt method for more details).

        - HDF5 format : used if file is an opened HDF5 file or a string ending in 'h5'.
        The optional keywords are increment=True and ndigits=3 to control the behaviour of the dataset autoincrement.
        The optional attrs=dict() will be added to the dataset attributes. Extra keywords arguments will be passed to the hDF5 create_dataset function.
        (see the save_h5 method for more details)."""
        if type(file) is str:
            if file.endswith('txt'):
                msg = self.save_txt(file, **kwargs)
            elif file.endswith('h5'):
                with h5py.File(file, 'a') as hdf:
                    msg = self.save_h5(hdf, **kwargs)
            else:
                raise Exception('Unknown file extension : {0}'.format(file))
        elif type(file) is h5py._hl.files.File:
            msg = self.save_h5(file, **kwargs)
        else :
            raise TypeError('File should be a string or an opened HDF file.')
        return msg
    def save_txt(self, filename, increment=True, ndigits=3):
        """Save the data to a text file. If increment is True, the filename is automatically incremented and will contain a ndigits integer."""
        if increment : filename = increment_file(filename, ndigits)
        nparray = self.__data__
        np.savetxt(filename, nparray)
        msg = 'Data saved to {0}.'.format(str(filename))
        logger.info(msg)
        return msg
    def save_h5(self, hdf, dataset='data', attrs=dict(), increment=True, ndigits=3, **kwargs):
        """Save the data to a HDF5 dataset. The first parameter hdf must a HDF5 file opened for writing.
        If increment is True, the name of the dataset is automatically incremented and will contain a ndigits integer.
        The non data attributes are saved as HDF5 attributes together with the extra attributes passed in attrs.
        The file is flushed after the dataset is inserted.
        Optional arguments are passed to the create_dataset function (e.g. compression='gzip').
        """
        nparray = self.__data__
        attrs.update(self.__attributes__)
        if increment : dataset = __increment__(dataset, '', hdf.keys(), ndigits)
        if dataset not in hdf:
            ds = hdf.create_dataset(dataset, data=nparray, **kwargs)
        else:
            ds = hdf[dataset]
            ds[:] = source
        for k,v in attrs.iteritems() :
            ds.attrs[k] = v
        hdf.flush()
        msg = 'Data saved to {0} in dataset {1}.'.format(str(file.filename), dataset)
        logger.info(msg)
        return msg

class Sij(data):
    """Vector network analyzer data.
    Attributes : freq, real, imag, mag, phase, start_frequency, stop_frequency, number_of_points, power
    Data format : c_[freq, real, imag]"""
    @property
    def freq(self):
        return np.linspace(self.start_frequency, self.stop_frequency, self.number_of_points)
    @property
    def real(self):
        return self.Sij[:,0]
    @property
    def imag(self):
        return self.Sij[:,1]
    @property
    def mag(self):
        return np.sqrt(self.Sij[:,0]**2 + self.Sij[:,1]**2)
    @property
    def phase(self):
        return np.arctan2(self.Sij[:,1] , self.Sij[:,0])
    def __data__(self):
        return np.c_[ self.freq, self.Sij]
    def plot(self, ax, scale='log', **kwargs):
        y = 20*np.log10(self.mag) if scale is 'log' else self.mag
        ax.plot(self.freq/1e9, y, **kwargs)
        ax.set_xlabel('Frequency (GHz)')
        ax.set_ylabel('$|S_{ij}|^2$ (dB)' if scale is 'log' else '$|S_{ij}|$')
    def __attributes__(self):
        attrs = self.copy()
        del attrs['Sij']
        return attrs

class lecroy_trace(data):
    """Lecroy oscilloscope waveform.
    Attributes : horiz, vert, horiz_interval, horiz_offset, sweeps_per_acq, bandwidth_limit, vertical_gain, vertical_offset, vert_coupling, acq_vert_offset, probe_att, wave
    Data format : c_[horiz, vert]"""
    @property
    def __data__(self):
        return np.c_[ self.horiz, self.vert]
    def plot(self, ax, **kwargs):
        ax.plot(self.horiz, self.vert, **kwargs)
    @property
    def __attributes__(self):
        attrs = self.copy()
        del attrs['wave']
        return attrs
    @property
    def horiz(self):
        """Horizontal axis vector."""
        x = np.arange( len(self.wave) ) * self.horiz_interval
        x += self.horiz_offset
        return x
    @property
    def vert(self):
        y = self.wave.astype(np.float)
        y *= param['vertical_gain']
        y -= param['vertical_offset']


class xy(data):
    """Generic x,y data.
    Attributes : x, y
    Data format : c_[x,y]"""
    @property
    def __data__(self):
        return np.c_[ self.x, self.y]
    def plot(self, ax, **kwargs):
        ax.plot(self.x, self.y, **kwargs)
    @property
    def __attributes__(self):
        attrs = self.copy()
        del attrs['x']
        del attrs['y']
        return attrs
