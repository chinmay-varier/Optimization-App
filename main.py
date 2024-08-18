import tkinter.messagebox
from customtkinter import *
import customtkinter
import tkinter
from after_login import App
import mysql.connector as ms

app = CTk()
app.geometry("1600x900")

customtkinter.set_default_color_theme("green")
login = False

user = ""

cnct = ms.connect(user='admin', password='password', host='localhost', database='appdetails')


def Register():
    def check():
        cursor = cnct.cursor()
        cursor.execute('use appdetails')

        if user_pass.get() == user_pass2.get():
            try:
                cursor.execute(f"insert into info values('{user_entry.get()}', '{user_pass.get()}')")
                cnct.commit()
                tkinter.messagebox.showinfo(title="Success", message="Registered Successfully!")
                regWin.destroy()
            except:
                tkinter.messagebox.showwarning(title="Username", message="Please Choose an Unique USERNAME!")
                
        else:
            tkinter.messagebox.showwarning(title="Password", message="Password doesn't match!")  
            
        
        

    regWin = CTkToplevel(master=app, takefocus=True)
    regWin.geometry("400x400")
    frame = CTkFrame(master=regWin) 
    frame.pack(pady=20,padx=40,fill='both',expand=True) 
    label = CTkLabel(master=frame,text='Enter Details', font=("Helvetica", 20)) 
    label.pack(pady=12,padx=10)     
    
    user_entry= CTkEntry(master=frame,placeholder_text="Username", height=50, width=220) 
    user_entry.pack(pady=12,padx=10) 
    
    user_pass= CTkEntry(master=frame,placeholder_text="Password",show="*", height=50, width=200) 
    user_pass.pack(pady=12,padx=10)    

    user_pass2= CTkEntry(master=frame,placeholder_text="Enter Password Again",show="*", height=50, width=200) 
    user_pass2.pack(pady=12,padx=10)   
    
    button = CTkButton(master=frame,text='Register', command=check) 
    button.pack(pady=12,padx=10) 
    
def Login():
    def check():
        cursor = cnct.cursor()
        cursor.execute('use appdetails')
        cursor.execute(f"SELECT EXISTS(SELECT * FROM info WHERE Username='{user_entry.get()}');")
        if cursor.fetchone()[0] == 1:
            tkinter.messagebox.showinfo(title="Signed In", message="Sign in was successful!")
            global user
            user = user_entry.get()
            regWin.destroy()
            app.withdraw()
            App(user)
        else:
            tkinter.messagebox.showwarning(title="Error", message="Please check the username and password!")



    regWin = CTkToplevel(master=app, takefocus=True)
    regWin.geometry("400x400")
    frame = CTkFrame(master=regWin) 
    frame.pack(pady=20,padx=40,fill='both',expand=True) 
    label = CTkLabel(master=frame,text='Enter Details', font=("Helvetica", 20)) 
    label.pack(pady=12,padx=10)     
    
    user_entry= CTkEntry(master=frame,placeholder_text="Username", height=50, width=220) 
    user_entry.pack(pady=12,padx=10) 
    
    user_pass= CTkEntry(master=frame,placeholder_text="Password",show="*", height=50, width=200) 
    user_pass.pack(pady=12,padx=10)    
    
    button = CTkButton(master=frame,text='login', command=check) 
    button.pack(pady=12,padx=10) 


framea = CTkFrame(master=app, width=200, height = 200)

login_btn = CTkButton(master=framea,
                    text="Login", width=500, height=50, font=("Helvetica",24),
                    hover_color="green", border_width=1.5, border_color="black",
                    command=Login
                    )
sign_up_btn =CTkButton(master=framea,
                    text="Sign Up", width=500, height=50, font=("Helvetica",24),
                    hover_color="green", border_width=1.5, border_color="black",
                    command=Register
                    )

Fh = 800
Sh = 450

login_btn.configure(bg_color='transparent')

framea.pack(pady=20,padx=40,fill='both',expand=True)
login_btn.pack(pady=20, anchor=tkinter.CENTER)
sign_up_btn.pack(pady=0)


app.mainloop()