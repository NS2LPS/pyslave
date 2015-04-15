# Parse rszvb.py file to generate DLL doc

fout = open("rszvb.rst",'w')
import re, cStringIO

def parse_rst(func, argin):
    with open('./rszvb_vxi/rszvb_{0}.rst'.format(func),'r') as fdoc:
        docin = fdoc.read()
    docin = docin.replace('\nVi',' Vi')
    docin = docin.replace('generator_PortNumber','generatorPortNumber')
    docin = docin.replace('generator_portNumber','generatorPortNumber')
    docin = docin.replace('single_trainPulsePeriod','singleTrainPulsePeriod')
    docin = docin.replace('delay_phase','delayPhase')
    for a in argin:
        docin = docin.replace('{0}\n'.format(a), '{0} '.format(a))
    fdoc = cStringIO.StringIO(docin)
    while True:
        l = fdoc.readline()
        if l.startswith('Purpose'): break
    fdoc.readline()
    description=''
    while True:
        l = fdoc.readline()
        if l.startswith('Parameters'):break
        description += '        '+l
    fdoc.readline()
    argin_dict = dict()
    for a in argin:
        a=a.split('=')[0]
        print a
        while True:
            l=fdoc.readline()
            if re.search('{0} Vi'.format(a), l, re.IGNORECASE) : break
            if not l : break
        argin_description = re.findall(r'Vi[^\s]+.*',l)[0]
        try :
            argin_description = argin_description.split(' ',1)[1]
        except IndexError:
            argin_description=fdoc.readline()
        while True:
            l=fdoc.readline().strip()
            if not l: break
            argin_description+=l
        argin_dict[a]=argin_description
    return description, argin_dict

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
            if func!='init':
                print "Processing",func
                description, argin_dict = parse_rst(func, argin)
                print >>fout, ".. method:: {0}(self, {1})".format(func, ', '.join(argin))
                print >>fout, "   {0}".format(description)
                for k,v in argin_dict.iteritems():
                    print >>fout, "   :param {0}: {1}".format(k, v)
                for a in argout:
                    print >>fout, "   :return: {0}".format(a)
                print >>fout


fout.close()
