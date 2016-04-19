from sikuli.Sikuli import *
#
import subprocess, sys, os, os.path, shutil, ntpath, re
from SimpleXMLRPCServer import SimpleXMLRPCServer as Server
#srv = Server(("127.0.0.1", 1337),allow_none=True) # as an example on the same machine
#if not srv: exit(1)
#
setAutoWaitTimeout(300)
#
#
# -*- coding: UTF-8 -*-
#


#Notify='notify-send -i \'/home/miphilli/Dropbox/5-Permanent/Icons/WinJUPOS-N-up.png\' \'Starting a Sikuli Script\' -t 30000'
#os.popen(Notify+Key.ENTER)
arcsec='\"'
Deg="°"
degree=unicode(Deg, errors="ignore")

CurrentFile="D:\\D-Permanent\\Dropbox\\D-Permanent\\Astronomy\\Logs\\currentephem.txt"
#file = open(CurrentFile,"r")
#
ISODATE=""
#
#
#WINJUPOS
#
Cmsys=(Pattern("system.png").similar(0.29))

Eph=(Pattern("ephem.png").similar(0.36))
#Cmsys=(Pattern("1433027845741.png").similar(0.29))
#Eph=(Pattern("1433027864991.png").similar(0.22))

#
os.popen("killall workrave")
switchApp("WinJUPOS")
#
#CMSYS
#
wait(Cmsys)
switchApp("WinJUPOS")
hover(Cmsys)
rightClick(Cmsys)
sleep(0.5)
type("c")
sleep(0.5)
UTandCM=ALTtext = Env.getClipboard()
DATE=UTandCM.split()[0]
T=UTandCM.split()[2]+UTandCM.split()[3]+'C'
TIME=T.replace(':','-')[:-5]
CMSYStext=UTandCM[35:].lstrip()


#
#ALT
#hover(Alt)
dragDrop(Pattern("alt.png").similar(0.40).targetOffset(-317,-30),Pattern("alt.png").similar(0.36).targetOffset(162,21))
#dragDrop(Pattern("1433027942175.png").targetOffset(-407,-22), Pattern("1433027946540.png").targetOffset(128,18))

type("c", KEY_CTRL)
ALTtext = Env.getClipboard()
ALT = ALTtext.split()[2]
#
#Ephemerdis
#
hover(Eph)
rightClick(Eph)
sleep(0.5)
type("c")
sleep(0.5)
Ephtext = Env.getClipboard()

E=Ephtext.split()

Planet=E[0]

if Planet == 'Jupiter':
    Dia=E[51]
    Mag=E[71]
    Ring=E[80].rstrip(',')
    Elong=E[39]
    ElongDir=E[41]
    LoS=E[87]
    #
    #RESULTS
    #
    R=("j"+DATE+"_"+TIME+"\n\n"+CMSYStext+"\n\n"+
        "Dia:"+Dia+", mag:"+Mag+"\n"+
        "Alt:"+ALT+", Ls:"+LoS+
        "\nElong: "+Elong+"("+ElongDir+")")

if Planet == 'Saturn':
    Dia=E[51]
    Mag=E[71]
    Ring=E[80].rstrip(',')
    Elong=E[39]
    ElongDir=E[41]
    LoS=E[87]
    #
    #RESULTS
    #
    R=("s"+DATE+"_"+TIME+"\n\n"+CMSYStext+"\n\n"+
        "Dia:"+Dia+", mag:"+Mag+"\n"+
        "Alt:"+ALT+", Ring:"+Ring+
        "\nElong: "+Elong+"("+ElongDir+")")

if Planet == 'Mars':
    Dia=E[49]
    Mag=E[73]
    Elong=E[39]
    ElongDir=E[41]
    LoS=E[79].lstrip(':').replace('','')[:-1]
    print "LoS="+LoS
    Phase=str(1-float(E[53]))
    #
    #RESULTS
    #
    R=("m"+DATE+"_"+TIME+"\n\n"+CMSYStext+"\n"+"Ls= "+LoS+degree+"\n\n"+
        "Dia:"+Dia+", mag:"+Mag+"\n"+
        "Alt:"+ALT+", Phase:"+Phase+
        "\nElong: "+Elong+"("+ElongDir+")")


if Planet == 'Venus':
    Dia=E[49]
    Mag=E[74]
    Elong=E[39]
    ElongDir=E[41]
    Phase=str(1-float(E[54]))
    #
    #RESULTS
    #
    R=("v"+DATE+"_"+TIME+"\n\n"+CMSYStext+"\n\n"+
        "Dia:"+Dia+", mag:"+Mag+"\n"+
        "Alt:"+ALT+", Phase:"+Phase+
        "\nElong: "+Elong+"("+ElongDir+")")

if Planet == 'Mercury':
    Dia=E[51]
    Mag=E[74]
    Ring=E[80].rstrip(',')
    Elong=E[39]
    ElongDir=E[41]
    LoS=E[90]
    #
    #RESULTS
    #
    R=("Me"+DATE+"_"+TIME+"\n\n"+CMSYStext+"\n\n"+
        "Dia:"+Dia+", mag:"+Mag+"\n"+
        "Alt:"+ALT+", Ls:"+LoS+
        "\nElong: "+Elong+"("+ElongDir+")")


if Planet == 'Neptune':
    Dia=E[51]
    Mag=E[71]
    Ring=E[80].rstrip(',')
    Elong=E[39]
    ElongDir=E[41]
    LoS=E[87]
    #
    #RESULTS
    #
    R=("n"+DATE+"_"+TIME+"\n\n"+CMSYStext+"\n\n"+
        "Dia:"+Dia+", mag:"+Mag+"\n"+
        "Alt:"+ALT+", Ring:"+Ring+
        "\nElong: "+Elong+"("+ElongDir+")")

if Planet == 'Uranus':
    Dia=E[51]
    Mag=E[71]
    Ring=E[80].rstrip(',')
    Elong=E[39]
    ElongDir=E[41]
    LoS=E[87]
    #
    #RESULTS
    #
    R=("n"+DATE+"_"+TIME+"\n\n"+CMSYStext+"\n\n"+
        "Dia:"+Dia+", mag:"+Mag+"\n"+
        "Alt:"+ALT+", Ring:"+Ring+
        "\nElong: "+Elong+"("+ElongDir+")")

#popup(R)
#UnicodeEncodeError: 'ascii' codec can't encode character u'\xb0' in position 39: ordinal not in range(128)
#file.write(R)

#
#

os.popen("notepad "+CurrentFile)
sleep(5)
type(Key.END, KEY_CTRL)
sleep(0.5)
paste(Key.ENTER)
paste(Key.ENTER)
paste(Planet)
paste(Key.ENTER)
paste(DATE+" - "+T)
paste(Key.ENTER)
paste(R)
type('s', KEY_CTRL)
sleep(2)
os.popen("workrave")
Notify='notify-send -i \'/home/miphilli/Dropbox/5-Permanent/Icons/WinJUPOS-N-up.png\' \'WinJUPOS Info DONE\' -t 5000'
os.popen(Notify+Key.ENTER)
