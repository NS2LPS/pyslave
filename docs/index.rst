.. pyslave documentation master file, created by
   sphinx-quickstart on Sun Mar 29 15:46:05 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyslave's documentation!
===================================

.. automodule:: pyslave


Pyslave contains two modules *pyslave* and *pydata*. The *pyslave* module allows
to control an experiment through Python scripts. The *pydata* module defines helper
functions and classes to manipulate experimental data:

::

    from pyslave import *

Contents
========

.. toctree::
   :maxdepth: 2

    pyslave.rst::
    magic_pyslave.rst
    scripting_language.rst
    instruments.rst
    drivers.rst

    pydata.rst::
    magic_pydata.rst
    datadict.rst
    increment.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
