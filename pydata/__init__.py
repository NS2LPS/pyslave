"""The *pydata* module provides function to o quickly create and access experimental data.

It contains :
* "Magic" functions to be used in the IPython shell. These functions help to keep data organized on a one folder per day basis..
* Helper functions and classes to create datasets and store them in text or H5 format
"""

from pydata.datadict import Data, xy, Sij, Spec, Lecroy_trace, createdata, h5todata
from pydata.increment import increment_file
from pydata.h5pydata import loadh5, createh5
