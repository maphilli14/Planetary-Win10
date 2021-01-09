from sikuli.Sikuli import *
#
import subprocess, sys, os, os.path, shutil, ntpath, re
from SimpleXMLRPCServer import SimpleXMLRPCServer as Server
srv = Server(("127.0.0.1", 1337),allow_none=True) # as an example on the same machine
if not srv: exit(1)
#
setAutoWaitTimeout(90)
#
#
# -*- coding: UTF-8 -*-
#

def GIMPRGB(STACKEDFOLDER,RGB):
    try:
        click(Pattern("1602212075433.png").targetOffset(-27,-46))
        sleep(5)
        type('w',KEY_CTRL+KEY_SHIFT)
        sleep(2)
        click(Pattern("1602212075433.png").targetOffset(-27,-46))
        sleep(1)
        type('w',KEY_CTRL+KEY_SHIFT)
        sleep(0.2)
        click(Pattern("1602212075433.png").targetOffset(-27,-46))
        sleep(5)
 
        click(Pattern("1602212075433.png").targetOffset(-27,-46))
        sleep(1)
        type('f',KEY_ALT)
        sleep(0.2)
        type('o')
        sleep(0.2)
        wait(Pattern("1602212194037.png").targetOffset(26,-32))
        type('l',KEY_ALT)
        sleep(0.2)
        paste(os.path.join(STACKEDFOLDER,'temp'))
        sleep(0.2)
        type(Key.ENTER)
        sleep(1)
        click(Pattern("1517067301601.png").similar(0.85))
        type('a',KEY_CTRL)
        sleep(0.2)
        click(Pattern("1517067301601.png").similar(0.85))
        type('a',KEY_CTRL)
        sleep(0.2)
        click(Pattern("1602212306126.png").targetOffset(10,6))
        sleep(5)
        waitVanish("1517065014495.png")
        sleep(5)
        click(Pattern("1602212075433.png").targetOffset(-27,-46))
        type('c',KEY_ALT)
        sleep(0.2)
        type('o')
        sleep(0.2)
        type('o')
        sleep(0.2)
        click(Pattern("1602212372783.png").targetOffset(67,-25))
        sleep(0.2)
        click("1602212456857.png")
        sleep(0.2)
        click(Pattern("1602212372783.png").targetOffset(67,9))
        sleep(0.2)
        click("1602212527627.png")
        sleep(0.2)
        click(Pattern("1602212372783.png").targetOffset(70,46))
        sleep(0.2)
        click("1602212538711.png")
        sleep(0.2)
        click("1602212607522.png")
        sleep(5)
        waitVanish("1602212607522.png")        
        sleep(5)
        click(Pattern("1602212075433.png").targetOffset(-27,-46))
        sleep(0.2)
        type('e',KEY_CTRL+KEY_SHIFT)
        wait("1602212719561.png")
        sleep(2.2)
        type('a',KEY_CTRL)
        sleep(1.2)        
        paste(os.path.join(STACKEDFOLDER,'RGB'))
        sleep(1.2)        
        type(Key.ENTER)
        sleep(1.2)        
        type('a',KEY_CTRL)
        sleep(1.2)        
        paste(os.path.join(STACKEDFOLDER,'RGB'))
        sleep(1.2)        
        type(Key.ENTER)
        sleep(1.2)        
        type('a',KEY_CTRL)
        sleep(1.2)        
        paste(RGB.strip('.tif')+'.png')
        sleep(1.2)        
        type(Key.ENTER)
        sleep(1.2)        
        type('a',KEY_CTRL)
        sleep(1.2)        
        paste(RGB.strip('.tif')+'.png')
        sleep(1.2)        
        type(Key.ENTER)
        sleep(5)
        if exists("1602212855700.png",2):
            click("1602212855700.png",2)
            sleep(2)
        else:
            pass
        sleep(4)
        wait("1602212931424.png",10)
        click(Pattern("1602212931424.png").targetOffset(0,17),10)
        waitVanish("1602212931424.png",10)
        sleep(15)
    except:
        pass

srv.register_function(GIMPRGB)
srv.serve_forever()
