#! /usr/bin/python

'''     20180427
        Usable CLI interface to data analytics and program interactions


'''

import ChangeSettings
import os
from oslib import bcolors

def settings():
  conf=raw_input('\n Configure options? (y/n) ')
  if conf == 'y':
    print 'Ok, let\'s customize this...\n'
    m2()
  else:
    print '\n\nMoving on with default settings:  Scan which folders?\n'
    for l in Captures:
        try:
          os.listdir(l)
        except:
          pass


def menu():
  print '\n\n\nThis app will analyze your captures and automate your processing routine.\n'
  print ' a = List directory usage'
  print ' b ='
  menu = {}
  #menu['1']="What Planet? Enter single letter [jup,mars,sat]- for "+bcolors.green+"Jupiter"+bcolors.off+", "+bcolors.yellow+" Saturn "+bcolors.off+", or "+bcolors.red+"Mars"+bcolors.off
  menu['- ']=""
  #menu['2) ']="1.5x or 3x Drizzle? Enter single number [1 or 3]"
  options=menu.keys()
  options.sort()
  for entry in options:
    print entry, menu[entry]
    selection=raw_input("Please Select:")
    if selection == 'a':
      print "\nGeting disk utilization\n"
      print sizeof_fmt(disk(ChangeSettings.firecaptureroot))
    elif selection == 'm':
      print "\nSetting Multi Point Alignment\n"
      AP='m'
    elif selection == '1':
      print "\nSetting 1.5x Drizzle\n"
      Drizzle='1'
    elif selection == '3':
      print "\nSetting 3x Drizzle\n"
      Drizzle='3'
    else: 
      print "Unknown Option Selected!\n"
      break

  

def m3(planet):
  extcfg=raw_input('Accept defaults? (y/n) ')
  if extcfg =='n':
    print 'more options here...'
    return options
  elif extcfg =='y':
    return nocfg

def disk(FOLDER):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(FOLDER):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

################## RUNTIME ###################

menu()
print
print 'Done Stacking'
#os.popen2('%windir%\\system32\\rundll32.exe user32.dll,LockWorkStation') # Locks screen when done
