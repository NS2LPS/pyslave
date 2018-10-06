from pydata.h5pydata import createh5, loadh5
from pydata import Data
import os
import numpy as np



def test_createh5(tmpdir):
    o = createh5(os.path.join(tmpdir,'test.h5'))
    data = Data(test=np.ones(5))
    o.append_data(data)
    o.append_data(data,attrs={'test':2})
    assert o['data0001'].attrs['test']==2
    assert o.__next_dataset__('data',4)[1]=='data0002'
    assert o.__next_dataset__('test',4)[1]=='test0000'
    o.close()
    o = createh5(os.path.join(tmpdir,'test.h5'))
    assert o.__next_dataset__('data',4)[1]=='data0002'
    o.close()


def test_loadh5(tmpdir):
    o = createh5(os.path.join(tmpdir,'test.h5'))
    data = Data(test=np.ones(5))
    o.append_data(data,attrs={'test_':2})
    o.append_data(data,attrs={'test_':1})
    o.close()
    r = loadh5(os.path.join(tmpdir,'test.h5'))
    assert r.test_[1]==1
    assert r.test[1,1]==1


