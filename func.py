import os
import datetime


drc = os.getcwd() + "\Reg"

def cpuButton():
    directory = drc + "\CPU Optimizations.reg"
    os.system('"' + directory + '"')
    with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : -- CPU OPTIMIZATIONS APPLIED --\n')



def disableWinDef():
    dirc = drc + "\Disable Windows Defender.reg"
    os.system('"' + dirc + '"')
    with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : -- WIN DEF DISABLED --\n')

def powerSavingForUsb():
    directory = drc + "\Disable Power Saving Features For USB and System.reg"
    os.system('"' + directory + '"')
    with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : -- POWER SAVING FOR USB DISABLED --\n')

def disableDiagnosticServices():
    dirc = drc + "\Disable Diagnostics and Telemetry Services.reg"
    os.system('"' + dirc+ '"')
    with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : -- DIAGNOSTIC SERVICE DISABLED --\n')

def disableMaps():
    dirc = drc + "\Disable Download Maps Manager.reg"
    os.system('"' + dirc + '"')
    with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : -- WIN MAPS DISABLED --\n')

def disableXbox():
    dirc = drc + "\Disable Xbox Services.reg"
    os.system('"' + dirc + '"')
    with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : --XBOX SERVICES DISABLED --\n')

def restart():
    os.system("shutdown /r")with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : -- SYS RESTART --\n')

def revCpu():
    pass

def winDefEn():
    os.system('"' + drc + '\Enable Windows Defender.reg' + '"')
    with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : -- WIN DEF ENABLED --\n')

def revUsb():
    pass

def telemetryEn():
    os.system('"' + drc + '\Enable Diagnostics & Telemtry Services.reg' + '"')
    with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : -- TELEMETRY ENABLED --\n')

def msmapEn():
    os.system('"' + drc + '\Enable Download Maps Manager.reg' + '"')
    with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : -- MS MAP ENABLED --\n')

def xboxEn():
    os.system('"' + drc + '\Enable Xbox Services.reg' + '"')
    with open('temp.txt', 'r') as f:
        with open(f.read(), 'a+') as k:
            k.writelines(str(datetime.datetime.now()) + ' : -- XBOX SERVICES ENABLED --\n')

def nvInspec():
    os.system('"' + drc + '\EvidiaProfileInspector.exe' + '"')

def msiMode():
    os.system('"' + drc + '\MSI Mode Utility V2.exe' + '"')

def deFrag():
    os.system('"' + '%windir%\system32\dfrgui.exe' + '"')

def afterburner():
    os.system('"' + 'start /max https://www.msi.com/Landing/afterburner/graphics-cards' + '"')
