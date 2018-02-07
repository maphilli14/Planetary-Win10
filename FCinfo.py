#
import subprocess, sys, os, os.path, shutil, ntpath, re, time
'''
	started writing from scratch on 20131028
	This script gathers important info from all 
'''

import subprocess, sys, os, os.path, shutil, collections, fnmatch, re, xmlrpclib
from collections import defaultdict

N=[]
S=open('Settings.txt','r').readlines()

def BS(l):
        if '\\' in l[-1:]:
                print 'Be careful with paths ending with a backslash'
                L=l[:-l]
                return L
        else:
                return l


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

if var == 'a':
        NEWa=raw_input('What do you wish to use for a? ')
        BS(NEWa)
        N=['a=\''+os.path.join(NEWa)+'\'\n' if 'a=' in x else x for x in N]
        for n in N:
                nS.write("%s\n" % n)
elif var == 'b':
        NEWb=os.path.join(raw_input('What do you wish to use for b? '))
        BS(NEWb)
        N=['b=\''+NEWb+'\'\n' if 'b=' in x else x for x in N]
        for n in N:
                nS.write(n)
elif var == 'c':
        NEWc=os.path.join(raw_input('What do you wish to use for c? '))
        BS(NEWc)
        N=['c=\''+NEWc+'\'\n' if 'c=' in x else x for x in N]
        for n in N:
                nS.write(n)
else:
        pass

try:
        nS.close()
except:
        pass

def parser(ROOT,Planet,DATE):
        #Create Empty List to hold info
        FClist=[]
        #Vars
        FPS='FPS (avg.)'
        FCfile=os.path.join(SettingsRoot,Planet,DATE+'.txt')
        if not os.path.isdir(os.path.join(SettingsRoot,Planet)):
                os.mkdir(os.path.join(SettingsRoot,Planet))
        else:
                pass
        if not os.path.isfile(FCfile):
                print 'Creating '+FCfile
                open(FCfile,'a').close()
        else:
                pass
        CAPS=os.listdir(ROOT)
        for RGB in CAPS:
                fldr=os.listdir(os.path.join(ROOT,RGB))
                txt = [l for l in fldr if 'txt' in l]
                FClist.append(RGB)
                FClist.append('======================')
                for i in txt:
                        f=open(os.path.join(ROOT,RGB,i)).readlines()
                        for l in f:
                                if re.search('^Filter=', l):
                                        FClist.append(l.strip())
                        for l in f:
                                if FPS in l:
                                        FClist.append('FPS = '+filter(lambda l: l.isdigit(), l))
                        for l in f:
                                if re.search('^Gain=', l):
                                        FClist.append('Gain = '+str(round(float(filter(lambda l: l.isdigit(), l))/100)).rstrip('.0'))

                                        FClist.append('')
                FClist.append('======================')
                #Results to Screen and file
                FCwrite=open(FCfile,'wb')
                for l in FClist:
                        print l
                        FCwrite.write(l+'\r\n')
                       
                        
