#! "D:\Program Files\Python2.7\python.exe"


import os, xmlrpclib, shutil, logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

'''

This script automates RGB combine in GIMP 2.10.
It will ask for where your stacked or sharped source files are,
sort them into RBG sequences, calculate the mid time and make them
into color images.

'''

STACKEDFOLDER = raw_input("Where are you stacked files?")
L=os.listdir(os.path.join(STACKEDFOLDER))

cli = xmlrpclib.ServerProxy("http://127.0.0.1:1337",allow_none=True)

try:
        os.mkdir(os.path.join(STACKEDFOLDER,'RGB'))
except:
        pass
try:
        os.mkdir(os.path.join(STACKEDFOLDER,'temp'))
except:
        pass

BLUES=[]
CAPS=[]
for f in L:
	if '-B-' in f:
		BLUES.append(f)
for f in L:
        if '-B-' in f:
                BLUE=f
                MID=f[11:17]
                if '-R-' in L[L.index(f)-1]:
                        RED = L[L.index(f)-1]
                        RGB=RED[0:11]+MID+'-RGB'+RED[19:]
                else:
                        RED = ''
                if '-G-' in L[L.index(f)+1]:
                        GREEN = L[L.index(f)+1]
                else:
                        GREEN = ''
                print 'MIDTIME = '+str(MID)+' Processing ('+str(BLUES.index(BLUE)+1)+' of '+str(len(BLUES))+')'
                print '=================='
                print 'RED = '+RED
                print 'GREEN = '+GREEN
                print 'BLUE = '+f
                if not RED=='' and not GREEN=='' and not BLUE=='':
						print 'All RGB FOUND!'
						CAPS.append(MID)
                else:
                        print 'Not all RGB found, manually assemble'
                print ''

for c in CAPS:
	print(c)

EDIT = raw_input("Is this list complete?")


print("\nThis script has completed successfully!\n")
os.system("pause")