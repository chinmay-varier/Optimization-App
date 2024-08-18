import os

drc = os.getcwd() + "\Reg"

def cpuButton():
    directory = drc + "\CPU Optimizations.reg"
    os.system('"' + directory + '"')

def disableWinDef():
    dirc = drc + "\Disable Windows Defender.reg"
    os.system('"' + dirc + '"')

def powerSavingForUsb():
    directory = drc + "\Disable Power Saving Features For USB and System.reg"
    os.system('"' + directory + '"')

def disableDiagnosticServices():
    dirc = drc + "\Disable Diagnostics and Telemetry Services.reg"
    os.system('"' + dirc+ '"')

def disableMaps():
    dirc = drc + "\Disable Download Maps Manager.reg"
    os.system('"' + dirc + '"')

def disableXbox():
    dirc = drc + "\Disable Xbox Services.reg"
    os.system('"' + dirc + '"')

def restart():
    os.system("shutdown /r")

def revCpu():
    pass

def winDefEn():
    os.system('"' + drc + '\Enable Windows Defender.reg' + '"')

def revUsb():
    pass

def telemetryEn():
    os.system('"' + drc + '\Enable Diagnostics & Telemtry Services.reg' + '"')

def msmapEn():
    os.system('"' + drc + '\Enable Download Maps Manager.reg' + '"')

def xboxEn():
    os.system('"' + drc + '\Enable Xbox Services.reg' + '"')

def nvInspec():
    os.system('"' + drc + '\EvidiaProfileInspector.exe' + '"')

def msiMode():
    os.system('"' + drc + '\MSI Mode Utility V2.exe' + '"')

def deFrag():
    os.system('"' + '%windir%\system32\dfrgui.exe' + '"')

def afterburner():
    os.system('"' + 'start /max https://www.msi.com/Landing/afterburner/graphics-cards' + '"')
