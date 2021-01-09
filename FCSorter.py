#!/usr/bin/python


import subprocess, sys, os, os.path, shutil, ntpath, re, time, calendar

'''
	20201016
	This script will open the settings file and validate
	you have stacked your captures in AS3
	then move to your backuplocation

'''

import os, Settings, datetime


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)
	
Planet=os.listdir(Settings.fcroot)[0]
Date=os.listdir(os.path.join(Settings.fcroot,Planet))[-1]
CurrPath=os.path.join(Settings.fcroot,Planet,Date)
CurrFile=os.listdir(os.path.join(Settings.fcroot,Planet,Date))


# PlannedExpiriation in months from current time of script execution
PlannedExpiriation=4
NOW=datetime.datetime.now()
Expiration=add_months(NOW,PlannedExpiriation).strftime('%Y-%m-%d')
Expiration=str('Expiring--'+Expiration)
try:
	os.makedirs(os.path.join(Settings.fcarchive,Expiration,Planet,Date))
except:
	print 'Cannot create dir = '+str(os.path.join(Settings.fcarchive,Expiration,Planet,Date))


try:
	os.makedirs(os.path.join(Settings.stacked,Planet,Date))
except:
	print 'Cannot create dir = '+str(os.path.join(Settings.stacked,Planet,Date))


'''

Find all captures

>>> for c in CurrFile:
...     if '.avi' in c:
...             print c
...
2020-10-15-0116_3-R-Mars.avi
2020-10-15-0117_2-R-Mars.avi

'''

VIDEOS=[]

for c in CurrFile:
	if '.avi' in c:
		VIDEOS.append(c)

'''
archive all videos
'''

try:
	for v in VIDEOS:
		shutil.move(os.path.join(CurrPath,v),os.path.join(Settings.fcarchive,Expiration,Planet,Date))
except:
	pass
	
'''
move stacks
'''
print 'Moving stacks from '+CurrPath+' to '+os.path.join(Settings.stacked,Planet,Date)
if Planet == 'Mars':
	Planet='4-Mars'
try:
	shutil.move(CurrPath,os.path.join(Settings.stacked,Planet))
	print 'Move succeeded!'
except:
	print 'Move failed'



'''

Find all Stacked

>>> for c in CurrFile:
...     if 'AS' in c:
...             print c


'''

