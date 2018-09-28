from IPython.core.magic import register_line_magic, needs_local_scope
from numpy import *

@register_line_magic
@needs_local_scope
def testexec(line, local_ns):
    exec("a=ones(10)",globals(),local_ns)
    print(line)

del testexec
