#
import subprocess, sys, os, os.path, shutil, ntpath, re, time
'''
	started writing from scratch on 20131028
	This script gathers important info from all 
'''

import subprocess, sys, os, os.path, shutil, collections, fnmatch, re, xmlrpclib
from collections import defaultdict

import ChangeSettings

def parser(ROOT,Planet,DATE):
        #Create Empty List to hold info
        FClist=[]
        #Vars
        FPS='FPS (avg.)'
        FCfile=os.path.join(ChangeSettings.SavedSettingsRoot,Planet,DATE+'.txt')
        if not os.path.isdir(os.path.join(ChangeSettings.SavedSettingsRoot,Planet)):
                os.mkdir(os.path.join(ChangeSettings.SavedSettingsRoot,Planet))
        else:
                pass
        if not os.path.isfile(FCfile):
                print 'Creating '+FCfile
                open(FCfile,'a').close()
        else:
                pass
        CAPS=os.listdir(os.path.join(ROOT,Planet))
        for RGB in CAPS:
                fldr=os.listdir(os.path.join(ROOT,Planet,RGB))
                txt = [l for l in fldr if 'txt' in l]
                FClist.append(RGB)
                FClist.append('======================')
                for i in txt:
                        Time=str('Time= '+i[11:17])
                        f=open(os.path.join(ROOT,Planet,RGB,i)).readlines()
                        FClist.append(Time)
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
                       
                        
