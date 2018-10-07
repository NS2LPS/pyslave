import re, os

def __next_index__(base,ext,previous):
    s = r'^{0}[0-9]+{1}$'.format(re.escape(base),re.escape(ext))
    rec = re.compile(s)
    index = [p[len(base):] for p in previous if rec.match(p)]
    if ext : index = [ p[:-len(ext)] for p in index]
    index = [ int(p) for p in index]
    counter = max(index)+1 if index else 0
    return counter

def __increment__(base, ext, previous, ndigits):
    counter = __next_index__(base,ext,previous)
    return base + str(counter).zfill(ndigits) + ext

def increment_file(filename, ndigits=4):
    """Return a filename with an automatically incremented number at the end.
    The number is zero padded to have ndigits."""
    basename = filename.rsplit('.',1)[0] if '.' in filename else filename
    ext = '.'+filename.rsplit('.',1)[1] if '.' in filename else ''
    files = os.listdir('.')
    return __increment__(basename, ext, files, ndigits)
