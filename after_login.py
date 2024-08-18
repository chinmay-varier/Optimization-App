import tkinter.messagebox
from customtkinter import *
from func import *
import psutil
import cpuinfo
import GPUtil
import tkinter

home_count = 0

wind = ''


def App(username):
    def HomePage():
        global home_count

        global wind
        if type(wind) != str:
            wind.destroy()
        wind = CTkFrame(frame)
        wind.pack(pady=20,padx=40,fill='both',expand=True)
        cpuOpt = CTkLabel(wind, text="Apply CPU Optimizations🖥",width= 20, height=40, font=("Great Vibes", 28))
        defBl = CTkLabel(wind, text="Disable Windows Defender🛡", width= 20, height=40, font=("Great Vibes", 28))
        defBl.grid(row=0, column=6, padx=490, pady= 60)
        cpuOpt.grid(row=0, column=0, padx=60)
        cpuBtn = CTkButton(wind, text="Confirm Optimization ✔", fg_color='#00FFFF', text_color='black', command=cpuButton)
        cpuBtn.grid(row=2, column=0)

        defBlBtn = CTkButton(wind, text="Confirm Optimization ✔", fg_color='#00FFFF', text_color='black', command=disableWinDef)
        defBlBtn.grid(row=2, column=6, pady=10)

        usb = CTkLabel(wind, text="Apply USB Optimizations🔌", width= 20, height=40, font=("Great Vibes", 28))
        usb.grid(row=4, column=0, padx=90, pady=60)
        usbBtn = CTkButton(wind, text="Confirm Optimization ✔", fg_color='#00FFFF', text_color='black', command=powerSavingForUsb)
        usbBtn.grid(row=8, column=0, pady=5)

        dt = CTkLabel(wind, text='''Disable Diagnostic &Telemetry\nServices⚙️''', width= 20, height=40, font=("Great Vibes", 28))
        dt.grid(row=4, column=6, padx=5, pady=20)
        dtBtn = CTkButton(wind, text="Confirm Optimization ✔", fg_color='#00FFFF', text_color='black', command=disableDiagnosticServices)
        dtBtn.grid(row=8, column=6, pady=5)

        maps = CTkLabel(wind, text="Disable MS Maps 🗺", width= 20, height=40, font=("Great Vibes", 28))
        maps.grid(row=10, column=0, padx=90, pady=60)
        mapBtn = CTkButton(wind, text="Confirm Optimization ✔", fg_color='#00FFFF', text_color='black', command=disableMaps)
        mapBtn.grid(row=12, column=0, pady=5)

        xbox = CTkLabel(wind, text="Disable Xbox Services 🎮", width= 20, height=40, font=("Great Vibes", 28))
        xbox.grid(row=10, column=6, padx=90, pady=60)
        xboxBtn = CTkButton(wind, text="Confirm Optimization ✔", fg_color='#00FFFF', text_color='black', command=disableXbox)
        xboxBtn.grid(row=12, column=6, pady=5)
            
        
    def ComSpec():
        global wind
        if type(wind) != str:
            wind.destroy()
        wind = CTkFrame(frame)
        wind.pack(pady=20,padx=40,fill='both',expand=True)
        cpu = CTkLabel(wind, text=f'CPU NAME:               {cpuinfo.cpu.info[0]["ProcessorNameString"]}', width= 20, height=40, font=("Helvetica", 23))
        cpu.place(x=50, y = 20)
        cpuClock = CTkLabel(wind, text=f'CPU Clock Speed:               {len(cpuinfo.cpu.info)} Cores @{cpuinfo.cpu.info[0]["~MHz"]}MHz', width= 20, height=40, font=("Helvetica", 23))
        cpuClock.place(x=50, y = 70)
        totalRam = CTkLabel(wind, text=f'Total RAM:               {psutil.virtual_memory().total/1073741824} GB', width= 20, height=40, font=("Helvetica", 23))
        totalRam.place(x=50, y = 120)
        UsedRam = CTkLabel(wind, text=f'RAM Utilization:               {psutil.virtual_memory().percent}%', width= 20, height=40, font=("Helvetica", 23))
        UsedRam.place(x=50, y = 170)
        if psutil.virtual_memory().percent > 50:
            warn = CTkLabel(wind, text='Optimization Needed!', width=20, height=40, font=("Helvetica", 23), text_color='red')
            warn.place(x=600, y=170)
        diskSpace = CTkLabel(wind, text=f'Total Disk Space:               {psutil.disk_usage("/").total/1073741824} GB', width= 20, height=40, font=("Helvetica", 23))
        diskSpace.place(x=50, y = 220)
        freeSpace = CTkLabel(wind, text=f'Free Disk Space:               {psutil.disk_usage("/").free/1073741824} GB', width= 20, height=40, font=("Helvetica", 23))
        freeSpace.place(x=50, y=270)
        gpuName = CTkLabel(wind, text=f'GPU NAME:               {GPUtil.getGPUs()[0].name}', width= 20, height=40, font=("Helvetica", 23))
        gpuName.place(x=50, y=320)
        driver = CTkLabel(wind, text=f'GPU Driver Version:               {GPUtil.getGPUs()[0].driver}', width= 20, height=40, font=("Helvetica", 23))
        driver.place(x=50, y=370)
        vram = CTkLabel(wind, text=f'GPU Total VRAM:               {GPUtil.getGPUs()[0].memoryTotal} MB', width= 20, height=40, font=("Helvetica", 23))
        vram.place(x=50, y = 420)
        vramuse = CTkLabel(wind, text=f'GPU USED VRAM:               {GPUtil.getGPUs()[0].memoryUsed} MB', width= 20, height=40, font=("Helvetica", 23))
        vramuse.place(x=50, y=470)
        gpuLoad = CTkLabel(wind, text=f'GPU Load:               {GPUtil.getGPUs()[0].load*100}%', width= 20, height=40, font=("Helvetica", 23))
        gpuLoad.place(x=50, y=520)
        gpuTemp = CTkLabel(wind, text=f'GPU Temperature:               {GPUtil.getGPUs()[0].temperature}°C', width= 20, height=40, font=("Helvetica", 23))
        gpuTemp.place(x=50, y= 570)
        if  GPUtil.getGPUs()[0].temperature == 0:
            w = CTkLabel(wind, text='Cannot Be Read!', width= 20, height=40, font=("Helvetica", 23), text_color='red')
            w.place(x=600, y = 570)


    def Revert():
        global wind
        if type(wind) != str:
            wind.destroy()
        wind = CTkFrame(frame)
        wind.pack(pady=20,padx=40,fill='both',expand=True)
        cpuOpt = CTkLabel(wind, text="Revert CPU Optimizations🖥",width= 20, height=40, font=("Great Vibes", 28))
        defBl = CTkLabel(wind, text="Enable Windows Defender🛡", width= 20, height=40, font=("Great Vibes", 28))
        defBl.grid(row=0, column=6, padx=490, pady= 60)
        cpuOpt.grid(row=0, column=0, padx=60)
        cpuBtn = CTkButton(wind, text="Revert Optimization 🔄", fg_color='#00FFFF', text_color='black', command=revCpu)
        cpuBtn.grid(row=2, column=0)

        defBlBtn = CTkButton(wind, text="Revert Optimization 🔄", fg_color='#00FFFF', text_color='black', command=winDefEn)
        defBlBtn.grid(row=2, column=6, pady=10)

        usb = CTkLabel(wind, text="Revert USB Optimizations🔌", width= 20, height=40, font=("Great Vibes", 28))
        usb.grid(row=4, column=0, padx=90, pady=60)
        usbBtn = CTkButton(wind, text="Revert Optimization 🔄", fg_color='#00FFFF', text_color='black', command=revUsb)
        usbBtn.grid(row=8, column=0, pady=5)

        dt = CTkLabel(wind, text='''Enable Diagnostic &Telemetry\nServices⚙️''', width= 20, height=40, font=("Great Vibes", 28))
        dt.grid(row=4, column=6, padx=5, pady=20)
        dtBtn = CTkButton(wind, text="Revert Optimization 🔄", fg_color='#00FFFF', text_color='black', command=telemetryEn)
        dtBtn.grid(row=8, column=6, pady=5)

        maps = CTkLabel(wind, text="Enable MS Maps 🗺", width= 20, height=40, font=("Great Vibes", 28))
        maps.grid(row=10, column=0, padx=90, pady=60)
        mapBtn = CTkButton(wind, text="Revert Optimization 🔄", fg_color='#00FFFF', text_color='black', command=msmapEn)
        mapBtn.grid(row=12, column=0, pady=5)

        xbox = CTkLabel(wind, text="Enable Xbox Services 🎮", width= 20, height=40, font=("Great Vibes", 28))
        xbox.grid(row=10, column=6, padx=90, pady=60)
        xboxBtn = CTkButton(wind, text="Revert Optimization 🔄", fg_color='#00FFFF', text_color='black', command=xboxEn)
        xboxBtn.grid(row=12, column=6, pady=5)

    
    def Adv():
        global wind
        if type(wind) != str:
            wind.destroy()
        wind = CTkFrame(frame)
        wind.pack(pady=20,padx=40,fill='both',expand=True)
        tkinter.messagebox.showwarning(title='Careful!', message='DONOT mess with these Settings if you don\'t know what you are doing')
        nvInspector = CTkLabel(wind, text="Edit Nvidia Profile Values 🔰",width= 20, height=40, font=("Great Vibes", 28))
        nvInspector.grid(row=0, column=0, padx=60)
        inspecBtn = CTkButton(wind, text="Open Profile Inspector", fg_color='#00FFFF', text_color='black', command=nvInspec)
        inspecBtn.grid(row=2, column=0)

        Msi = CTkLabel(wind, text="Open MSI Mode Utility 🛠", width= 20, height=40, font=("Great Vibes", 28))
        Msi.grid(row=0, column=6, padx=490, pady= 60)

        MsiBtn = CTkButton(wind, text="Edit MSI Settings", fg_color='#00FFFF', text_color='black', command=msiMode)
        MsiBtn.grid(row=2, column=6, pady=10)

        defrag = CTkLabel(wind, text="Defragment / Retrim Drives 💾", width= 20, height=40, font=("Great Vibes", 28))
        defrag.grid(row=4, column=0, padx=90, pady=60)
        defBtn = CTkButton(wind, text="Open Defragmentor", fg_color='#00FFFF', text_color='black', command=deFrag)
        defBtn.grid(row=8, column=0, pady=5)

        oc = CTkLabel(wind, text="OverClock GPU (Afterburner)⏲", width= 20, height=40, font=("Great Vibes", 28))
        oc.grid(row=4, column=6, padx=5, pady=20)
        ocBtn = CTkButton(wind, text="Install Afterburner", fg_color='#00FFFF', text_color='black', command=afterburner)
        ocBtn.grid(row=8, column=6, pady=5)



    def Page(choice):
        if choice == '🏠Home':
            HomePage()
        elif choice == "🖥Computer Specifications":
            ComSpec()
        elif choice == "🔄Revert Changes":
            Revert()
        elif choice == "🛠Advanced Settings":
            Adv()
    k = CTk()
    k.geometry('1600x900')
    k.resizable(False, False)
    frame = CTkFrame(master=k) 
    frame.pack(pady=20,padx=40,fill='both',expand=True)

    options = ["🏠Home","🖥Computer Specifications", "🔄Revert Changes", "🛠Advanced Settings"]
    menu = CTkOptionMenu(frame, values=options, width=500, height = 50,
                          fg_color="#00FFFF", button_color="#00FFFF", text_color="black",
                          font=("Great Vibes", 24), anchor='center', dropdown_font=("Great Vibes", 24),
                          command=Page
                        )
    menu.pack()
    a = CTkLabel(frame, text=f'Hello, {username} !!', anchor="w",font=("Great Vibes", 24))
    a.place(x=50, y=20)
    b = CTkButton(frame, text="RESTART PC", fg_color="#39FF14", text_color="black", font=("Great Vibes", 15), command=restart)
    b.place(x=1200, y= 20)
    k.mainloop()

#App("HI")