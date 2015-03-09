# Parse header file to generate Python wrapper around the rszvb DLL for the Rohde&Scwarz ZVA 40 Network Anlyzer

fout = open("rszvb_v2.py",'w')

# First load the DLL
print >>fout , """import numpy as numpy
from ctypes import *

# Prerequisition: installed rszvb driver 32-bit

# Reference to rszvb dll
rszvbDLL = windll.rszvb_32

class ZVBDLLERROR(Exception):
	pass
        
iStringBufferLen = 1024
sStringBuffer = create_string_buffer(iStringBufferLen)

def __errorcheck__(iCode, func, args):
    if iCode<0:
        iHandle = args[0]
        rszvbDLL.rszvb_error_message(iHandle, iCode, sStringBuffer)
        msg = " {} : {}".format(func.name, sStringBuffer.value)
        eqcode = c_int(0)
        rszvbDLL.rszvb_error_query (iHandle, byref(eqcode), sStringBuffer)
        if eqcode.value != 0:
            msg += " - ZVB Instrument Error : {}".format(sStringBuffer.value)
        raise ZVBDLLERROR(msg)
    else:
        return args

"""

# Load all constants 
print >>fout,"\n#DLL constants\n"

fin  = open("rszvb_header_file.h",'r')
for l in fin:
    if l.startswith("#define RSZVB") and "0x" not in l :
        vals = l[8:].split(' ',1)
        print >>fout, vals[0],"=",vals[1].strip()
fin.close()

# Protoype dll functions
print >>fout,"\n#DLL functions\n"

type_convert = {'ViSession'     : 'c_int',
                'ViSession*'    : 'POINTER(c_int)',
                'ViStatus'      : 'c_int',
                'ViInt16'       : 'c_int16',
                'ViInt16*'      : 'POINTER(c_int16)',                
                'ViInt32'       : 'c_int32',
                'ViInt32*'      : 'POINTER(c_int32)',                
                'ViBoolean'     : 'c_bool',
                'ViBoolean*'    : 'POINTER(c_bool)',
                'ViString'      : 'c_char_p',
                'ViRsrc'        : 'c_char_p',
                'ViReal64'      : 'c_double',
                'ViReal64*'     : 'POINTER(c_double)',
                'ViReal64 _VI_FAR'  : 'numpy.ctypeslib.ndpointer(dtype=numpy.float64)',
                'ViInt32 _VI_FAR'   : 'numpy.ctypeslib.ndpointer(dtype=numpy.int32)',
                'ViChar _VI_FAR'    : 'c_char_p',
                }

with open("rszvb_header_file.h",'r') as fin:
    while True:
        l = fin.readline()
        if not l: break    
        if l.startswith("ViStatus _VI_FUNC"):
            func_block = l[17:]
            if ';' not in func_block:
                l = ''
                while ';' not in l:
                    l = fin.readline()
                    func_block += l
            func_name,func_args = [s.strip('\n );') for s in func_block.split('(')]
            func_args = [s.strip() for s in func_args.split(',')]
            print >>fout, "#",func_name,func_args
            arg_types = []
            arg_names = []
            for s in func_args:
                s = s.split(' ')
                arg_types.append(s[0]+' '+s[1] if len(s)>2 else s[0])
                arg_names.append(s[-1])
            print >>fout, "prototype = WINFUNCTYPE(c_int, {0})".format( ','.join([type_convert.get(typ, 'Unknown') for typ in arg_types]) )
            print >>fout, "paramflags = ({0},)".format(','.join(["({0}, '{1}')".format(2 if '*' in typ else 1 ,nam) for (typ,nam) in zip(arg_types,arg_names)]))
            print >>fout, func_name," = prototype(('{0}', rszvbDLL), paramflags)".format(func_name)
            print >>fout, "{0}.name = '{0}'".format(func_name)
            print >>fout, "{0}.errcheck = __errorcheck__".format(func_name)
            print >>fout, "{0}.output = {1}".format(func_name, any(['*' in typ for typ in arg_types]))
            

fin.close()

fout.close()