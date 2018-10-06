from pydata import Data, h5todata
import numpy as np
import os
import h5py

def test_Data(tmpdir):
    o = Data(x=np.ones(3), y=np.ones(3), a=5, b='hh')
    assert o.b=='hh'
    assert o['a']==5
    o.append(np.ones(5),np.ones(5))
    o.save(os.path.join(tmpdir, 'test.txt'))
    o.save(os.path.join(tmpdir, 'test.h5'))


def test_h5todata(tmpdir):
    o = Data(x=np.ones(3), y=np.ones(3), a=5, b='hh')
    o.save(os.path.join(tmpdir, 'test.h5'))
    f = h5py.File(os.path.join(tmpdir, 'test.h5'),'r')
    d = h5todata(f['data0000'])
    assert d.a==5
    assert d.x[0]==1

