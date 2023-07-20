import tkinter
from typing import Optional, Tuple, Union
import customtkinter
import pandas as ps
import matplotlib as mp
from CTkMessagebox import CTkMessagebox
from pandastable import Table
import login



def show_info():
    CTkMessagebox(title="Info", message="This is a CTkMessagebox!")


def show_data():
    
    cnvTest.grid(row=2, padx=10, pady=10, columnspan=3, sticky="n")
    cnvTest.config(width=900,height=600)
    pt.config(width=900,height=600)
    pt.show()
    btnShow.configure(text="Hide")
    btnShow.configure(command=hid_data)

def hid_data():
    cnvTest.grid_forget()
    btnShow.configure(text="Show")
    btnShow.configure(command=show_data)

#def add_record():
     

#run app
class App(customtkinter.CTk):
          def __init__(self):
            super().__init__()

            self.geometry("1000x800")
            self.title("test")

            #making grid
            #self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure(2, weight=1)
            #self.grid_rowconfigure(2,weight=2)


login.loginOpend()
app = App()
cnvTest = customtkinter.CTkCanvas(app, width=50,height=40)
pt = Table(cnvTest)
btnShow=customtkinter.CTkButton(app, text="Show", command=show_data)
btnShow.grid(row=0, column=0, padx=10,pady=10,)
#btnAddData=customtkinter.CTkButton(app, text="Add Record", command=add_record)
app.mainloop()

