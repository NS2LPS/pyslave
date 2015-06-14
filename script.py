"""This module contains helper functions to write slave scripts."""

import os, re, logging
import numpy as np
import h5py

# Logger
logger = logging.getLogger('pyslave.script')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

def __increment_logic__(base, ext, previous, ndigits):
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
    

def increment(filename, ndigits=3):
    """Automatically generate filenames with an incremented number

    Return a filename with an auto incremented number at the end of the name.
    The number is zero padded to have n digits."""
    basename = filename.rsplit('.',1)[0] if '.' in filename else filename
    ext = '.'+filename.rsplit('.',1)[1] if '.' in filename else ''
    files = os.listdir('.') 
    return __increment_logic__(basename, ext, files, ndigits)

def save_txt(source, file, increment=True, ndigits=3):
    """Save the data from source to a text file.

    File can be a string or a valid file handle opened for writing.

    Source can be a numpy array or an instrument.
    If source is an instrument the __save_txt__ method is called and the returned data are saved."""
    if type(source) is not np.ndarray:
        source = source.__save_txt__()
    if increment and type(filename) is str : filename = increment(filename, ndigits)
    np.savetxt(filename, source)
    msg = 'Data saved to {0}.'.format(str(filename))
    logger.info(msg)
    return msg

def save_h5(source, file, dataset='data', attrs=dict(), increment=True, ndigits=3, **kwargs):
    """Save the data from source to a HDF5 dataset.

    Source can be a numpy array or an instrument.
    If source is an instrument the __save_h5__ method is called and the returned data are used to create the dataset.
    Attributes passed in attrs are added to the dataset attributes.

    File can be a string or a valid HDF5 file or group opened for writing. The file is flushed after the dataset is inserted.

    Optional arguments are passed to the create_dataset function (e.g. compression='gzip').
    """
    if type(source) is not np.ndarray:
        source, args = source.__save_h5__()
        attrs.update(args)
    hdf = h5py.File(file,'a') if type(file) is str else file
    if increment : dataset = __increment_logic__(dataset, '', hdf.keys(), ndigits)
    if dataset not in hdf:
        ds = hdf.create_dataset(dataset, data=source, **kwargs)
    else:
        ds = hdf[dataset]
        ds[:] = source
    for k,v in attrs.iteritems() :
        ds.attrs[k] = v
    hdf.flush()
    if type(file) is str : hdf.close()
    msg = 'Data saved to {0} in dataset {1}.'.format(str(file), dataset)
    logger.info()
    return msg

def fetch_txt(instrument, filename, fetch_args=dict()):
    """ Fetch and save data from an instrument to a text file.

    The fetch method of the instrument is called with the fetch_args. Then the data are saved as described in save_txt."""
    instrument.fetch(**fetch_args)
    save_txt(instrument, filename)


def fetch_h5(instrument, filename, fetch_args=dict(), dataset='data', attrs=dict(), **kwargs):
    """ Fetch and save data from an instrument to a HDF5 file.

    The fetch method of the instrument is called with the fetch_args. Then the data are saved as described in save_h5."""
    instrument.fetch(**fetch_args)
    save_h5(instrument, filename, dataset=dataset, attrs=dict(), **kwargs)
