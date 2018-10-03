import h5py
import numpy as np

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
