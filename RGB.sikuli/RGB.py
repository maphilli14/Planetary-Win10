from sikuli.Sikuli import *
#
import subprocess, sys, os, os.path, shutil, ntpath, re
from SimpleXMLRPCServer import SimpleXMLRPCServer as Server
srv = Server(("127.0.0.1", 1337),allow_none=True) # as an example on the same machine
if not srv: exit(1)
#
setAutoWaitTimeout(300)
#
#
# -*- coding: UTF-8 -*-
#

def GIMPRGB(STACKEDFOLDER,RGB):
    try:
        COLORS=['RED.tif','GREEN.tif','BLUE.tif']
        for c in COLORS:
            switchApp('GNU')
            click("1516829911499.png")            
            sleep(1)
            type('f',KEY_ALT)
            sleep(0.2)
            type('o')
            sleep(0.2)
            click("1516830020089.png")
            sleep(0.2)
            type('l',KEY_ALT)
            sleep(0.2)
            paste(os.path.join(STACKEDFOLDER,c))
            type(Key.ENTER)
            sleep(7)
            click("1516829911499.png")            
            sleep(0.2)
            type('f',KEY_ALT)
            sleep(0.2)
            type('a')
            sleep(0.2)
            type(os.path.join(c[18]))
            type(Key.ENTER)
            sleep(1)
            if exists("1516830061908.png",2):
                click("1516830061908.png")
                sleep(2)
            else:
                click("1516830108568.png")
                sleep(3)
            click("1516829911499.png")            
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
        type('f',KEY_ALT)
        sleep(0.2)
        type('e')
        paste(os.path.join(STACKEDFOLDER,RGB))
        type(Key.ENTER)
        sleep(7)
        type('w',KEY_CTRL+KEY_SHIFT)
        sleep(0.2)
    except:
        pass


srv.register_function(GIMPRGB)
srv.serve_forever()
