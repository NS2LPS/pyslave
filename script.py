# Script helping functions

import os, glob

def increment(filename, ndigits=3):
    basename = filename.rsplit('.',1)[0] if '.' in filename else filename
    ext = '.'+filename.rsplit('.',1)[1] if '.' in filename else ''
    path = os.getcwd()
    files = sorted(glob.glob( os.path.join(path, basename+'*'+ext) ))
    if files :
        lastfile = files[-1]
        counter = int(lastfile[len(basename):len(basename)+ndigits])
    else :
        counter = 0
    return basename + str(counter).zfill(ndigits) + ext
