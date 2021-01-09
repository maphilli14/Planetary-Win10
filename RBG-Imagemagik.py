#!/usr/bin/python3


import os, shutil, logging, subprocess, time


'''

This script automates RGB combine in GIMP 2.10.
It will ask for where your stacked or sharped source files are,
sort them into RBG sequences, calculate the mid time and make them
into color images.

'''
STACKROOT='/mnt/d/B-Sorted/Astronomy/20-Stacked/SolarSystem/4-Mars/2020/'
OneDRIVERGB=''
#RECENT=os.listdir('/mnt/d/B-Sorted/Astronomy/20-Stacked/SolarSystem/4-Mars/2020/')[-1]

'''

# dicey automatic finding based upon static and rudemntaary root

STACKEDFOLDER = os.listdir(os.path.join(STACKROOT,RECENT))
for F in STACKEDFOLDER:
	if 'AS' in F:
		AS3=F
STACKEDFOLDER = os.path.join(STACKROOT,RECENT,AS3)
AIFiles=os.listdir(os.path.join(STACKROOT,RECENT,AS3))
for F in AIFiles:
	if 'LrD' in F:
		AI=F

STACKEDFOLDER = os.path.join(STACKROOT,RECENT,AS3,AI)
'''

# totally static down to final folder, this is where they are sharped
STACKEDFOLDER = input("Where are you stacked files?").replace('\\','/')


#L=os.listdir(os.path.join(STACKROOT,RECENT,AS3,AI))

cmd='wslpath '+STACKEDFOLDER

SP = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
OUT,err=SP.communicate()
RC=SP.wait()

STACKEDFOLDER=OUT.strip()

L=os.listdir(OUT.strip())

SUBFolders=['RGB','RED','GREEN','BLUE','IR','Anims']

for i in SUBFolders:
	try:
			os.mkdir(os.path.join(STACKEDFOLDER,i))
	except:
			print('No BLUE found, try another folder of stacks?')
			pass

BLUES=[]
CAPS=[]
for f in L:
	if '-B-' in f:
		BLUES.append(f)

for f in L:
	try:
		if '-B-' in f:
			BLUE=f
			shutil.copy(os.path.join(STACKEDFOLDER,BLUE),os.path.join(STACKEDFOLDER,'BLUE'))
			MID=f[11:17]
			if '-R-' in L[L.index(f)-1]:
					RED = L[L.index(f)-1]
					shutil.copy(os.path.join(STACKEDFOLDER,RED),os.path.join(STACKEDFOLDER,'RED'))
					RGB=RED[0:11]+MID+'-RGB'+RED[19:]
			else:
					RED = ''
			if '-G-' in L[L.index(f)+1]:
					GREEN = L[L.index(f)+1]
					shutil.copy(os.path.join(STACKEDFOLDER,GREEN),os.path.join(STACKEDFOLDER,'GREEN'))
			else:
					GREEN = ''
			print('MIDTIME = '+str(MID)+' Processing ('+str(BLUES.index(BLUE)+1)+' of '+str(len(BLUES))+')')
			print('==================')
			print('RED = '+RED)
			print('GREEN = '+GREEN)
			print('BLUE = '+f)
			if not RED=='' and not GREEN=='' and not BLUE=='':
					print('All RGB FOUND!')
					CAPS.append(MID)
					os.popen('convert '+os.path.join(STACKEDFOLDER,RED)+' '+os.path.join(STACKEDFOLDER,GREEN)+' '+os.path.join(STACKEDFOLDER,BLUE)+' -combine -set colorspace sRGB '+os.path.join(STACKEDFOLDER,'RGB',RGB))
					#shutil.copy(os.path.join(STACKEDFOLDER,RGB),os.path.join(STACKEDFOLDER,'RGB'))
					
			else:
					print('Not all RGB found, manually assemble')
			print('')
	except:
		pass

for i in SUBFolders:
	try:
		print('Making an animation out of the '+i+' channel.')
		os.system('convert -delay 10 '+os.path.join(STACKEDFOLDER,i)+'/*.tif '+os.path.join(STACKEDFOLDER,'Anims')+'/'+i+'anim.gif')
	except:
			pass


for c in CAPS:
	print(c)


print("\nThis script has completed successfully!\n")
time.sleep(9000)
print("CLOSING")
