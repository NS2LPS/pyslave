from pydata.increment import __next_index__, increment_file

def test__next_index__():
    r = __next_index__('test','.txt',['data01.txt','test02.txt','test003.txt','test004'])
    assert r==4
    r = __next_index__('test','',['data01.txt','test02.txt','test003.txt','test004'])
    assert r==5
    r = __next_index__('ff','',['data01.txt','test02.txt','test003.txt','test004','ff'])
    assert r==0

def test_increment_file():
    r = increment_file('test.txt')
    assert r=='test0000.txt'
    r = increment_file('test')
    assert r=='test0000'
