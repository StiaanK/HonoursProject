import tkinter
from typing import Optional, Tuple, Union
import customtkinter
from CTkMessagebox import CTkMessagebox
import main


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def cancel():
    msg = CTkMessagebox(title="Cancel?", message="Canceling will close the program.",
                        icon="question", option_3="Yes", option_1="No" )
    response = msg.get()
    if response=="Yes":
        app.destroy()       

#Work in progress
def login():   
    main.returnMain()
    app.destroy()
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("450x200")
        self.title("Login")

        #making grid for app
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        #self.grid_columnconfigure(2, weight=1)

app = App()
#labels
lbl = customtkinter.CTkLabel(app, text="Please enter a username and password.").grid(row=0,column=0, padx=10,pady=10,columnspan=3)
lblUser = customtkinter.CTkLabel(app, text="Username:").grid(row=1,column=0, padx=10,pady=10)
lblPass = customtkinter.CTkLabel(app, text="Password:",).grid(row=2,column=0, padx=10,pady=10)
#entries
entUser = customtkinter.CTkEntry(app,width=200).grid(row=1,column=1, padx=10,pady=10,sticky="w",columnspan=2)
entPass = customtkinter.CTkEntry(app,width=200, show="*").grid(row=2,column=1, padx=10,pady=10,sticky="w",columnspan=2)
#butons
btnLogin = customtkinter.CTkButton(app, text="Login",command=login).grid(row=3,column=0, padx=10,pady=10,sticky="w")
btnCancel = customtkinter.CTkButton(app, text="Cancel",command=cancel).grid(row=3,column=1, padx=10,pady=10,sticky="e")


def open():
    app.mainloop()

#for testing
open()
