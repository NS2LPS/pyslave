# Script helping functions

import os, glob

def increment(filename, ndigits=3):
    basename = filename.rsplit('.',1)[0] if '.' in filename else filename
    ext = '.'+filename.rsplit('.',1)[1] if '.' in filename else ''
    files = sorted(glob.glob( basename+'*'+ext ))
    if files :
        lastfile = files[-1]
        counter = lastfile[len(basename):-len(ext)]
        counter = int(counter) if counter else 0
    else :
        counter = 0
    return basename + str(counter).zfill(ndigits) + ext
