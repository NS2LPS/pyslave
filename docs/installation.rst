Installing the pyslave package
================================

The minimal environment required to run ``pyslave`` is a ``IPython`` installation, including ``numpy``, ``h5py``, ``matplotlib`` and ``pyqt5``.
To interact with instruments, more packages are needed such as ``PyVISA``, ``PyDAQMx``, ``pyserial``.

To install the package, use one of the following set of commands in a prompt (e.g. conda prompt).

* Install and forget: ::

    pip install git+https://github.com/NS2LPS/pyslave

* Install and interact with the code
  First clone the github repository to a folder: ::

    git clone https://github.com/NS2LPS/pyslave

  Install the package with pip: ::

    pip install -e ./pyslave



Setting up ``pyslave and ``pydata`` environment
---------------------------------------------------
Create IPython profiles
^^^^^^^^^^^^^^^^^^^^^^^^^^

* If you have used the install and forget option, you have to locate the ``pyslave`` folder. You can do: ::

    import pyslave
    print(pyslave.__file__)

* Locate the ``.ipython`` directory. It should be ``C:\\Users\\your_name\\.ipython`` or ``~/.ipython``
* Copy the ``profile-pyslave`` directory from ``pyslave\misc`` into the ``.ipython`` directory
* Copy the ``profile-pydata`` directory from ``pydata\misc`` into the ``.ipython`` directory


Create Jupyter kernels
^^^^^^^^^^^^^^^^^^^^^^^^^^
* From the prompt, get the Jupyter kernel path

    >>> jupyter kernelspec list
    python3 C:\Users\your_name\AppData\Local\Continuum\anaconda3\share\jupyter\kernels\python3

* Go to the ``kernels`` folder and create a copy of the ``python3`` folder named ``pyslave``.
  In the ``kernels\pyslave`` folder modify the ``kernel.json`` file to: ::

     {
     "argv": [
      "C:\\Users\\your_name\\AppData\\Local\\Continuum\\anaconda3\\python.exe",
      "-m",
      "ipykernel_launcher",
      "--profile=pyslave",   #<-- add this line
      "-f",
      "{connection_file}"
     ],
     "display_name": "Pyslave", #<-- modify display name
     "language": "python"
    }

* Do the same with ``pydata``
* You can now start the Qt console with: ::

    jupyter qtconsole --kernel=pyslave

* If you start a Jupyter notebook server, you should see the two new kernels in the drop list to create a new notebook.

* You can adapt the windows batch files located in the ``pyslave`` and ``pydata`` folder to your installation.
