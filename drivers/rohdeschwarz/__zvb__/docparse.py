# Parse rszvb.py file to generate DLL doc

fout = open("rszvb.rst",'w')


with open("rszvb.py",'r') as fin:
    while True:
        l = fin.readline()
        if not l: break
        if l.startswith("paramflags"):
            exec l
            argin =  [ '{0}={1}'.format(p[1],p[2]) if len(p)>2 else p[1] for p in paramflags[1:] if p[0]==1 ]
            argout = [ p[1] for p in paramflags[1:] if p[0]==2 ]
            l = fin.readline()
            func = l.split('=')[0].strip()
            func = func[6:]
            print >>fout, "    .. method:: {0}(self, {1})".format(func, ', '.join(argin))
            if argout:
                print >>fout, "        Returns : ",', '.join(argout)
            print >>fout


fin.close()

fout.close()
