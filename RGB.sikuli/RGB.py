from sikuli.Sikuli import *
#
import subprocess, sys, os, os.path, shutil, ntpath, re
from SimpleXMLRPCServer import SimpleXMLRPCServer as Server
srv = Server(("127.0.0.1", 1337),allow_none=True) # as an example on the same machine
if not srv: exit(1)
#
setAutoWaitTimeout(15)
#
#
# -*- coding: UTF-8 -*-
#

def GIMPRGB(STACKEDFOLDER,RGB):
    try:
        switchApp('GNU')
        click("1516829911499.png")            
        sleep(1)
        type('w',KEY_CTRL+KEY_SHIFT)
        sleep(0.2)
        switchApp('GNU')
        click("1516829911499.png")            
        sleep(1)
        type('f',KEY_ALT)
        sleep(0.2)
        type('o')
        sleep(0.2)
        click("1516830020089.png")
        sleep(0.2)
        if exists("1517064575408.png"):
            pass
        else:
            type('l',KEY_ALT)
        sleep(0.2)
        paste(os.path.join(STACKEDFOLDER,'temp'))
        type(Key.ENTER)
        sleep(1)
        click(Pattern("1517067301601.png").similar(0.85))
        type('a',KEY_CTRL)
        sleep(0.2)
        click("1517067073574.png")
        sleep(1)
        if exists("1517065014495.png",2):
            sleep(3)
        sleep(2)
        click("1516829911499.png")            
        type('c',KEY_ALT)
        sleep(0.2)
        type('o')
        sleep(0.2)
        type('o')
        sleep(0.2)
        click(Pattern("1516830319137.png").targetOffset(38,-38))
        sleep(0.2)
        click("1516831933131.png")
        sleep(0.2)
        click(Pattern("1516830319137.png").targetOffset(34,5))
        sleep(0.2)
        click("1516831956391.png")
        sleep(0.2)
        click(Pattern("1516830319137.png").targetOffset(35,46))
        sleep(0.2)
        click("1516831970389.png")
        sleep(0.2)
        click("1516830977806.png")        
        sleep(1)
        click("1516829911499.png")            
        type('e',KEY_CTRL+KEY_SHIFT)
        wait("1516854495300.png")
        sleep(0.2)
        click("1516830020089.png")
        sleep(0.2)
        type('n',KEY_ALT)
        sleep(0.2)
        paste(os.path.join(STACKEDFOLDER,'RGB',RGB.strip('.tif')))
        type(Key.ENTER)
        sleep(1)
        if exists("1516832477260.png",2):
            click("1516832477260.png",2)
            sleep(2)
        else:
            pass
        sleep(2)
        click(Pattern("1516833090528.png").targetOffset(-5,15),2)
        waitVanish(Pattern("1516833090528.png").targetOffset(-5,15))
        click(Pattern("1516829911499.png").targetOffset(26,5),2)
        sleep(1)
        type('w',KEY_CTRL+KEY_SHIFT)
        sleep(0.2)
    except:
        pass

srv.register_function(GIMPRGB)
srv.serve_forever()
