#
import subprocess, sys, os, os.path, shutil, ntpath, re, time
'''
	20180207
	The settings used to be stored in each script.
	This script calls a file 'settings.txt' and sets variables for your
	reuse.


'''

import subprocess, sys, os, os.path, shutil, collections, fnmatch, re, xmlrpclib
from collections import defaultdict

N=[]
S=open('Settings.txt','r').readlines()

def BS(l):
        global cleanedL
        if '\\' in l:
                print 'Be careful with paths ending with a backslash'
                print 'Changing '+str(l)
                cleanedL=os.path.dirname(l)
                print 'To... '+str(cleanedL)
                return cleanedL
        else:
                return cleanedL


print ' Current Settings are:'
for l in S:
        exec(l)
        N.append(l)
        print l.strip()
EDIT=raw_input('Edit Settings? ')

if EDIT == 'y':
        var=raw_input('Which Setting? ')
        nS=open('Settings.txt','w')
else:
        var=''
        pass

if var == 'FireCaptureRoot':
        NEWa=raw_input('What do you wish to use for a? ')
        BS(NEWa)
        N=['FireCaptureRoot=\''+cleanedL+'\'\n' if 'FireCaptureRoot=' in x else x for x in N]
        for n in N:
                nS.write(n)
elif var == 'b':
        NEWb=os.path.join(raw_input('What do you wish to use for b? '))
        BS(NEWb)
        N=['b=\''+cleanedL+'\'\n' if 'b=' in x else x for x in N]
        for n in N:
                nS.write(n)
elif var == 'c':
        NEWc=os.path.join(raw_input('What do you wish to use for c? '))
        BS(NEWc)
        N=['c=\''+cleanedL+'\'\n' if 'c=' in x else x for x in N]
        for n in N:
                nS.write(n)
else:
        pass

try:
        nS.close()
except:
        pass
