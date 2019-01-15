import h5py
import numpy as np
from pydata.increment import __next_index__


try:
    from pyslave import __slave_disp__ as disp
except:
    disp = print

    
class createh5(h5py.File):
    """Create a new H5 file to save data.
    Use the append_dataset to add data to the file."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__data_counter__ = dict()
        self.fname = args[0]
    def __next_dataset__(self, dataset, ndigits):
        if not dataset in self.__data_counter__ :
            counter = __next_index__(dataset,'',self.keys())
        else:
            counter = self.__data_counter__[dataset] + 1
        return counter, dataset + str(counter).zfill(ndigits)
    def append_data(self, data, attrs=None, dataset='data', ndigits=4, **kwargs):
        """Create a new dataset with automatic increment of the name and save data to it.
        N.B. : data is an instance of the pyslave.datadict.Data class
        Attributes can be added."""
        counter, dataset_name = self.__next_dataset__(dataset, ndigits)
        ds = super().create_dataset(dataset_name, data=data.__data__, **kwargs)
        attributes = data.__attributes__.copy()
        if attrs : attributes.update(attrs)
        self.__data_counter__[dataset] = counter
        for k,v in attributes.items() :
            ds.attrs[k] = v
        self.flush()
        msg = 'Data saved to {0} in dataset {1}.'.format(self.fname, dataset_name)
        disp(msg)

class loadh5:
    """Load all datasets of a H5 file into numpy arrays.

    Example :
      d = loadh5('Sij_vs_Temperature.h5')
      print(d)

      Loaded from Sij_vs_Temperature.h5 with 70 datasets
      Data fields : freq,Sij
      Attributes  : T

      plot(T, abs(Sij).max(1))
    """

    def __init__(self, filename):
        with h5py.File(filename,'r') as f:
            keys = list(f.keys())
            length = len(keys)
            dataset = f[keys[0]]
            attr_keys = list(dataset.attrs.keys())
            data_keys = dataset.dtype.names
            # Build attribute array
            all_attrs = { k:np.empty(length, dtype=type(dataset.attrs[k]) ) for k in attr_keys}
            all_data  = { k:np.empty((length, len(dataset[k])), dtype=dataset[k].dtype) for k in data_keys}
            for i,d in enumerate(f.values()):
                for k in attr_keys : all_attrs[k][i] = d.attrs[k]
                for k in data_keys :  all_data[k][i] = d[k]
        for k in attr_keys:
            setattr(self, k, all_attrs[k])
        for k in data_keys:
            setattr(self, k, all_data[k])
        self.attr_keys = attr_keys
        self.data_keys = data_keys
        self.length = length
        self.filename = filename
        print(self)
    def __repr__(self):
        s = "Loaded from {0} with {1} datasets\n".format(self.filename, self.length)
        s += "Data fields : " + ', '.join(self.data_keys) + '\n'
        s += "Attributes  : " + ', '.join(self.attr_keys)
        return s
