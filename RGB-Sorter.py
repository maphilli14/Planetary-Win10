import os, xmlrpclib, shutil


STACKEDFOLDER = raw_input("Where are you stacked files?")
L=os.listdir(os.path.join(STACKEDFOLDER))

cli = xmlrpclib.ServerProxy("http://127.0.0.1:1337",allow_none=True)


for f in L:
        if '-B-' in f:
                BLUE=f
                shutil.copy2(os.path.join(STACKEDFOLDER,BLUE),os.path.join(STACKEDFOLDER,'BLUE.tif'))
                MID=f[11:17]
                if '-R-' in L[L.index(f)-1]:
                        RED = L[L.index(f)-1]
                        shutil.copy2(os.path.join(STACKEDFOLDER,RED),os.path.join(STACKEDFOLDER,'RED.tif'))
                        RGB=RED[0:11]+MID+'-RGB'+RED[19:]
                else:
                        RED = ''
                if '-G-' in L[L.index(f)+1]:
                        GREEN = L[L.index(f)+1]
                        shutil.copy2(os.path.join(STACKEDFOLDER,GREEN),os.path.join(STACKEDFOLDER,'GREEN.tif'))
                else:
                        GREEN = ''
                print 'MIDTIME = '+str(MID)
                print '=================='
                print 'RED = '+RED
                print 'GREEN = '+GREEN
                print 'BLUE = '+f
                if not RED=='' and not GREEN=='' and not BLUE=='':
                        print 'All RGB FOUND!'
                else:
                        print 'Not all RGB found, manually RsGB'
                print ''
                cli.GIMPRGB(STACKEDFOLDER,RGB)
