#!/usr/bin/python


import subprocess, sys, os, os.path, shutil, ntpath, re, time
'''
	20201016
	updated to Win10 WSL for general reuse of all vars in single location
	idea is to import this for any workflow for WSL
	
	20180425
	The settings used to be stored in each script.
	This script is using proper ConfigParser functions to sectionalize all variables
	Started using GIT to syncronize changes across systems


'''

import subprocess, sys, os, os.path, shutil, collections, fnmatch, re, xmlrpclib, ConfigParser
from collections import defaultdict

N=[]
Config = ConfigParser.ConfigParser()

Sf=('Settings.txt')
Config.read(Sf)


print 'Current settings are: \n'

for section in Config.sections():
	print section
	
S = {}
options = Config.options(section)
for option in options:
	try:
		S[option] = Config.get(section, option)
		if S[option] == -1:
			DebugPrint("skip: %s" % option)
	except:
		print("exception on %s!" % option)
		S[option] = None

'''
Now all settings are stored in S as a dict

>>> for key in a_dict:
...     print(key, '->', a_dict[key])
...
color -> blue
fruit -> apple
pet -> dog


'''

for k in S:
	print 'Setting var: '+k+' to your value = '+S[k]
	k=S.get(k)


fcarchive=S.get('fcarchive')
fcroot=S.get('fcroot')
stacked=S.get('stacked')


#Config.set('Captures')
'''
S2= open('Settings.txt','w')
Config.write(S2)
S2.close()
'''
