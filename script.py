"""This module contains helper functions to write slave scripts."""

import os, glob, logging
import numpy as np
import h5py

# Logger
logger = logging.getLogger('pyslave.script')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

def increment(filename, ndigits=3):
    """Automatically generate filenames with an incremented number

    Return a filename with an auto incremented number at the end of the name.
    The number is zero padded to have n digits."""
    basename = filename.rsplit('.',1)[0] if '.' in filename else filename
    ext = '.'+filename.rsplit('.',1)[1] if '.' in filename else ''
    files = sorted(glob.glob( basename + '[0-9]'*ndigits + ext ))
    if files :
        lastfile = files[-1]
        counter = lastfile[len(basename):-len(ext)]
        counter = int(counter)+1 if counter else 0
    else :
        counter = 0
    return basename + str(counter).zfill(ndigits) + ext

def save_txt(source, filename):
    """Save the data from source to a text file.

    Filename can be a string or a valid file handle opened for writing.

    Source can be a numpy array or an instrument.
    If source is an instrument the __save_txt__ method is called and the returned data are saved."""
    if type(source) is not np.ndarray:
        source = source.__save_txt__()
    np.savetxt(filename, source)
    logger.info('Data saved to {0}.'.format(filename))

def save_h5(source, filename, dataset='data', attrs=dict(), **kwargs):
    """Save the data from source to a HDF5 dataset.

    Source can be a numpy array or an instrument.
    If source is an instrument the __save_h5__ method is called and the returned data are used to create the dataset.
    Attributes passed in attrs are added to the dataset attributes.

    Filename can be a string or a valid HDF5 file or group opened for writing. The file is flushed after the dataset is inserted.

    Optional arguments are passed to the create_dataset function (e.g. compression='gzip').
    """
    if type(source) is not np.ndarray:
        source, args = source.__save_h5__()
        attrs.update(args)
    if type(filename) is str:
        with h5py.File(filename,'a') as hdf:
            ds = hdf.create_dataset(dataset, data=source, **kwargs)
            for k,v in attrs.iteritems() :
                ds.attrs[k] = v
    else:
        ds = filename.create_dataset(dataset, data=source, **kwargs)
        for k,v in attrs.iteritems() :
            ds.attrs[k] = v
        hdf.flush()
    logger.info('Data saved to {0} in dataset {1}.'.format(filename,dataset))

def fetch_txt(instrument, filename, fetch_args=dict()):
    """ Fetch and save data from an instrument to a text file.

    The fetch method of the instrument is called with the fetch_args. Then the data are saved as described in save_txt."""
    instrument.fetch(**fetch_args)
    save_txt(instrument, filename)


def fetch_h5(instrument, filename, fetch_args=dict(), dataset='data', attrs=dict(), **kwargs):
    """ Fetch and save data from an instrument to a HDF5 file.

    The fetch method of the instrument is called with the fetch_args. Then the data are saved as described in save_h5."""
    instrument.fetch(**fetch_args)
    save_h5(instrument, filename, dataset='data', attrs=dict(), **kwargs)
