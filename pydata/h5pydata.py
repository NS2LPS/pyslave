import h5py
import numpy as np
from .increment import __next_index__

class createh5(h5py.File):
    """Create a new H5 file to save data.
    Use the append_dataset to add data to the file."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__data_counter__ = dict()
    def __next_dataset__(self, dataset, ndigits):
        if not dataset in self.__data_counter__ :
            self.__data_counter__[dataset] = __next_index__(dataset,'',self.keys())
        return dataset + str(self.__data_counter__[dataset]).zfill(ndigits)
    def append_dataset(self, data, attrs={}, dataset='data', ndigits=4, **kwargs):
        """Create a new dataset with autmatic increment of the name and save data to it.
        Attributes can be added."""
        dataset_name = self.__next_dataset__(dataset, ndigits)
        ds = super().create_dataset(dataset_name, data=data, **kwargs)
        for k,v in attrs.items() :
            ds.attrs[k] = v
        self.__data_counter__[dataset] += 1
        self.flush()


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
