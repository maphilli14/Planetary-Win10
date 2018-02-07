import os, xmlrpclib, shutil


STACKEDFOLDER = raw_input("Where are you stacked files?")
DONESHARPS=os.path.join('D:\\C-Archives\\Astronomy\\20-SavedStacks\\SolarSystem\\5-Jupiter\\2017\\2017-05-15\\')
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

GREENS=[]
for f in L:
	if '-G_' in f:
		GREENS.append(f)
for f in L:
        if '-G_' in f:
                GREEN=f
                shutil.copy2(os.path.join(STACKEDFOLDER,GREEN),os.path.join(STACKEDFOLDER,'temp','GREEN.tif'))
                MID=f[21:27]
                if '-R_' in L[L.index(f)-1]:
                        RED = L[L.index(f)-1]
                        shutil.copy2(os.path.join(STACKEDFOLDER,RED),os.path.join(STACKEDFOLDER,'temp','RED.tif'))
                        RGB=RED[0:11]+MID+'-RGB'+RED[19:]
                else:
                        RED = ''
                if '-B_' in L[L.index(f)+1]:
                        BLUE = L[L.index(f)+1]
                        shutil.copy2(os.path.join(STACKEDFOLDER,BLUE),os.path.join(STACKEDFOLDER,'temp','BLUE.tif'))
                else:
                        BLUE = ''
                print 'MIDTIME = '+str(MID)+' Processing ('+str(GREENS.index(GREEN)+1)+' of '+str(len(GREENS))+')'
                print '=================='
                print 'RED = '+RED
                print 'GREEN = '+f
                print 'BLUE = '+BLUE
                if not RED=='' and not GREEN=='' and not BLUE=='':
                        print 'All RGB FOUND!'
                        cli.GIMPRGB(STACKEDFOLDER,RGB)
                        shutil.move(os.path.join(STACKEDFOLDER,RED),os.path.join(DONESHARPS,RED))
                        shutil.move(os.path.join(STACKEDFOLDER,GREEN),os.path.join(DONESHARPS,GREEN))
                        shutil.move(os.path.join(STACKEDFOLDER,BLUE),os.path.join(DONESHARPS,BLUE))
                else:
                        print 'Not all RGB found, manually assemble'
                print ''

