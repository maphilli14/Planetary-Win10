#! "D:\Program Files\Python2.7\python.exe"


import os, xmlrpclib, shutil


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
for f in L:
	if '-B-' in f:
		BLUES.append(f)
for f in L:
        if '-B-' in f:
                BLUE=f
                shutil.copy2(os.path.join(STACKEDFOLDER,BLUE),os.path.join(STACKEDFOLDER,'temp','BLUE.tif'))
                MID=f[11:17]
                if '-R-' in L[L.index(f)-1]:
                        RED = L[L.index(f)-1]
                        shutil.copy2(os.path.join(STACKEDFOLDER,RED),os.path.join(STACKEDFOLDER,'temp','RED.tif'))
                        RGB=RED[0:11]+MID+'-RGB'+RED[19:]
                else:
                        RED = ''
                if '-G-' in L[L.index(f)+1]:
                        GREEN = L[L.index(f)+1]
                        shutil.copy2(os.path.join(STACKEDFOLDER,GREEN),os.path.join(STACKEDFOLDER,'temp','GREEN.tif'))
                else:
                        GREEN = ''
                print 'MIDTIME = '+str(MID)+' Processing ('+str(BLUES.index(BLUE)+1)+' of '+str(len(BLUES))+')'
                print '=================='
                print 'RED = '+RED
                print 'GREEN = '+GREEN
                print 'BLUE = '+f
                if not RED=='' and not GREEN=='' and not BLUE=='':
                        print 'All RGB FOUND!'
                        cli.GIMPRGB(STACKEDFOLDER,RGB)
                else:
                        print 'Not all RGB found, manually assemble'
                print ''

print("\nThis script has completed successfully!\n")
os.system("pause")