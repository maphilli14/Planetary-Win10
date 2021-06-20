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
#STACKEDFOLDER = input("Where are you stacked files?").replace('\\','/')
STACKEDFOLDER='D:\D-Permanent\OneDrive\B-Sorted\Astronomy\\20-Stacked\SolarSystem\\5-Jupiter\\2021\Jupiter_20210618\AS_P50\LrD-1.5-12'
STACKEDFOLDER=STACKEDFOLDER.replace('\\','/')


#L=os.listdir(os.path.join(STACKROOT,RECENT,AS3,AI))

cmd='wslpath '+STACKEDFOLDER

SP = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
OUT,err=SP.communicate()
RC=SP.wait()

STACKEDFOLDER=OUT.strip()

L=os.listdir(OUT.strip())

SUBFolders=['RGB','RED','GREEN','BLUE','IR','Anims','RGB+labels']

for i in SUBFolders:
	try:
			os.mkdir(os.path.join(STACKEDFOLDER,i))
	except:
			print('No BLUE found, try another folder of stacks?')
			pass

BLUES=[]
CAPS=[]
for f in L:
	if '_b_' in f:
		BLUES.append(f)

for f in L:
	try:
		if '_b_' in f:
			BLUE=f
			shutil.copy(os.path.join(STACKEDFOLDER,BLUE),os.path.join(STACKEDFOLDER,'BLUE'))
			MID=f[11:17]
			if '_r_' in L[L.index(f)-1]:
					RED = L[L.index(f)-1]
					shutil.copy(os.path.join(STACKEDFOLDER,RED),os.path.join(STACKEDFOLDER,'RED'))
					RGB=RED[0:11]+MID+'-RGB'+RED[19:]
			else:
					RED = ''
			if '_g_' in L[L.index(f)+1]:
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
					#
					#ease of use vars
					#
					INFILE=os.path.join(STACKEDFOLDER,'RGB',RGB)
					OUTFILE=os.path.join(STACKEDFOLDER,'RGB+labels',RGB)
					LEVELS=' -level 0%,60% '
					RGBdt=RGB[:17]
					#tst
					try:
						print('trying to ls')
						os.popen('ls -la '+INFILE)
						print()
					except:
						print('failed to ls INFLE')
					#
					#
					#end ease of use vars
					#
					CAPS.append(MID)
					#This command does the RGB composition
					os.popen('convert '+os.path.join(STACKEDFOLDER,RED)+' '+os.path.join(STACKEDFOLDER,GREEN)+' '+os.path.join(STACKEDFOLDER,BLUE)+' -combine -set colorspace sRGB '+os.path.join(STACKEDFOLDER,'RGB',RGB))
					#This command adds labels
					os.popen('convert '+INFILE+LEVELS+' -font Times-Bold -pointsize 40 -stroke none -fill white -annotate +5+1275 \'Michael A. Phillips\'  -font Times-Bold -pointsize 20 -stroke none -fill white -annotate +5+25 '+RGBdt+' '+OUTFILE)
					#This command adds watermark
					time.sleep(2.2)
					os.popen('composite -geometry +1255+1190 /mnt/d/D-Permanent/Astronomy/Templates/maptag.png '+OUTFILE+' '+OUTFILE)
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
