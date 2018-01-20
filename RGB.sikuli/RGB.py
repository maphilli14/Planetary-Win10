import os



L=os.listdir(os.path.join('C:\Personal\A-Inbox\FC\Jup\Jup_2018_01_20\AS_f2000\VerL'))

for f in L:
        if '-B-' in f:
                MID=f[11:17]
                if '-R-' in L[L.index(f)-1]:
                        RED = L[L.index(f)-1]
                else:
                        RED = ''
                if '-G-' in L[L.index(f)+1]:
                        GREEN = L[L.index(f)+1]
                else:
                        GREEN = ''
                print 'MIDTIME = '+str(MID)
                print '=================='
                print 'RED = '+RED
                print 'GREEN = '+GREEN
                print 'BLUE = '+f
                print ''



