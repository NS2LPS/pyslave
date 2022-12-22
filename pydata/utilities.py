from IPython.display import display, Markdown
import glob
import h5py

def dispattrs(files,*args):
    """Display attributes of a group of H5 files::
    
        dispattrs('scan*.h5','power','rbw')"""
    allf = glob.glob(files)
    allf.sort()
    s = f"|File|{'|'.join(args)}|\n"
    s = s + f"| ---- | {'|'.join(['----' for a in args])} |\n"
    for f in allf:
        with h5py.File(f,'r') as h5f:
            find_data = lambda name, obj : name if 'data' in name  else None
            d0 = h5f.visititems(find_data)
            d0 = h5f[d0].attrs
            s = s + f"| {f} | {'|'.join([ str(d0[a]) for a in args])} |\n"
    return display(Markdown(s))
    
def fixattr(file,attr,value):
    """Fix or add the value of an attribute for all items in the file::
    
        fixattr('scan0000.h5','rbw',10)"""
    with h5py.File(file,'a') as h5f:
        for d in h5f.values():
            d.attrs[attr]=value
    
def copyh5(fin,fout,range):
    """Copy datasets from one file to another. Datasets are supposed to be named data????::
    
        copyh5('scan0000.h5','scan0001.h5',range(100,200))"""
    with h5py.File(fout,'a') as h5fout:
        with h5py.File(fin,'r') as h5fin:
            for i in range:
                h5fin.copy(h5fin[f'data{i:04d}'],h5fout)

def delh5(file,range):
    """Delete datasets from one. Datasets are supposed to be named data????::
    
        delh5('scan0000.h5',range(100,200))"""
    with h5py.File(file,'a') as h5f:
        for i in range:
            del h5f[f'data{i:04d}']


