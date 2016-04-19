#! /usr/bin/python

'''     20140501
        Menu tree feeds into AS2.py script to pass variables


'''

import AS2
import os
from oslib import bcolors

def m1():
  conf=raw_input('\n\n\nThis script will stack your images in AutoStakkert2\n Configure options? (y/n) ')
  if conf == 'y':
    print 'Ok, let\'s customize this...\n'
    m2()
  else:
    print '\n\nMoving on with default settings:\n  1.5x Drizzle\n  Single Point Alignment\n  Percent as 66%\n'
    AS2.AS2('s','1','66')
   

def m2():
  menu = {}
  #menu['1']="What Planet? Enter single letter [jup,mars,sat]- for "+bcolors.green+"Jupiter"+bcolors.off+", "+bcolors.yellow+" Saturn "+bcolors.off+", or "+bcolors.red+"Mars"+bcolors.off
  menu['1) ']="Single or Multi-Point Alignment? Enter single letter [s,m]"
  menu['2) ']="1.5x or 3x Drizzle? Enter single number [1 or 3]"
  options=menu.keys()
  options.sort()
  for entry in options:
    print entry, menu[entry]
    selection=raw_input("Please Select:")
    if selection == 's':
      print "\nSetting Single Point Alignment\n"
      AP='s'
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
  menu3 = {}
  menu3['3) ']="Select the percentage you wish to stack [66]"
  options3=menu3.keys()
  options3.sort()
  for entry in options3:
    print entry, menu3[entry]
    percent=raw_input("Please Select Percentage to Stack: ")
  AS2.AS2(AP,Drizzle,percent)
  

def m3(planet):
  extcfg=raw_input('Accept defaults? (y/n) ')
  if extcfg =='n':
    print 'more options here...'
    return options
  elif extcfg =='y':
    return nocfg


################## RUNTIME ###################

m1()
print
print 'Done Stacking'
os.popen2('%windir%\\system32\\rundll32.exe user32.dll,LockWorkStation') # Locks screen when done
