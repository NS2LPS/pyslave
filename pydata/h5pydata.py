import sys
import h5py
import numpy as np
from pydata.increment import __next_index__
import types

class DataException(Exception):
    pass    

class __autoiter__:
    def __next_dataset__(self, dataset, ndigits):
        if not dataset in self.__data_counter__ :
            counter = __next_index__(dataset,'',self.keys())
        else:
            counter = self.__data_counter__[dataset] + 1
        return counter, dataset + str(counter).zfill(ndigits)
    def append(self, data, **kwargs):
        """Create a new dataset with automatic increment of the name and save data to it.
        The data object must be an instance of pyslave.Data. Attributes can be added.
        See pyslave.Data.save for more details."""
        data.save_h5(self,**kwargs)

class Group_autoiter(h5py.Group, __autoiter__):
    pass

class createh5(h5py.File, __autoiter__):
    """Create a new H5 file to save data.
    Use append to add data to the file."""
    def __init__(self, *args, **kwargs):
        if not args:
            args = ('a',)
        params = {'libver':'latest'}
        params.update(kwargs)
        super().__init__(*args, **params)
        self.__data_counter__ = dict()
    def create_group(self, *args, **kwargs):
        """Create a group in the file"""
        g = super().create_group(*args,**kwargs)
        g.__data_counter__ = dict()
        g.__class__ = Group_autoiter
        return g

class loadh5:
    """Load all datasets of a H5 file or group into numpy arrays.

    Example :
      d = loadh5('Sij_vs_Temperature.h5')
      print(d)

      Loaded from Sij_vs_Temperature.h5 with 70 datasets
      Data fields : freq,Sij
      Attributes  : T

      plot(T, abs(Sij).max(1))
    """

    def __init__(self, filename, print_file = True):
        self.__groups__ = []
        self.attr_keys = []
        self.data_keys = []
        if type(filename) is str:
            with h5py.File(filename,'r', libver='latest', swmr=True) as hdf:
                self.__load__(hdf)
                self.name = hdf.file.filename + hdf.name 
        elif isinstance(filename, h5py.Group):
                self.__load__(filename)
                self.name = filename.file.filename + filename.name 
        else:
            raise DataException('Argument should be a filename or an HDF group')
        if print_file:
            print(self)

    def __load__(self,f):
        keys = []
        values = []
        for k,v in f.items():
            if isinstance(v, h5py.Group):
                setattr(self, k, loadh5(v, print_file=False))
                self.__groups__.append(k)
            elif isinstance(v, h5py.Dataset):
                keys.append(k)
                values.append(v)
        self.length = len(keys)
        if self.length:
            dataset = values[0]
            attr_keys = list(dataset.attrs.keys())
            data_keys = dataset.dtype.names
            # Build attribute array
            all_attrs = { k:np.empty(self.length, dtype=type(dataset.attrs[k]) ) for k in attr_keys}
            all_data  = { k:np.empty((self.length, len(dataset[k])), dtype=dataset[k].dtype) for k in data_keys}
            for i,d in enumerate(values):
                for k in attr_keys : all_attrs[k][i] = d.attrs[k]
                for k in data_keys :  all_data[k][i] = d[k]
            for k in attr_keys:
                setattr(self, k, all_attrs[k])
            for k in data_keys:
                setattr(self, k, all_data[k])
            self.attr_keys = attr_keys
            self.data_keys = data_keys

    def __repr__(self):
        s = ""
        if self.length:
            s += "Loaded from {0} with {1} datasets\n".format(self.name, self.length)
            s += "Data fields : " + ', '.join(self.data_keys) + '\n'
            if self.attr_keys : s += "Attributes  : " + ', '.join(self.attr_keys) + '\n'
        if self.__groups__:
            s += "Other groups : " + ', '.join(self.__groups__) + '\n'
        return s
