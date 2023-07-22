import tkinter
from typing import Optional, Tuple, Union
import customtkinter
import pandas as ps
import matplotlib as mp
from CTkMessagebox import CTkMessagebox
from pandastable import Table
import login
import tableSelect



def show_info():
    CTkMessagebox(title="Info", message="This is a CTkMessagebox!")


def show_data():
    
    cnvTest.grid(row=0, column=1 ,padx=10, pady=10,  sticky="n", rowspan=6)#columnspan =3
    cnvTest.config(width=900,height=600)
    pt.config(width=900,height=600)
    pt.show()
    btnSelectTab.grid(row=0, column=0, padx=10,pady=10, sticky="nw")
    btnAddData.grid(row=0, column=2, padx=10,pady=10, sticky="ne") 
    btnSelectTab.configure(command=hid_data)
    btnSelectTab.configure(text="Change Table")
    btnRemoveData.grid(row=1, column=2, padx=10,pady=10, sticky="ne") 
    btnEditData.grid(row=2, column=2, padx=10,pady=10, sticky="ne")

def hid_data():
    cnvTest.grid_forget()
    btnSelectTab.configure(command=show_data)



    
#def add_record():

#def edit_record():

#def  remove_record():
      

#run app
class App(customtkinter.CTk):
          def __init__(self):
            super().__init__()

            self.geometry("1000x700")
            self.title("test")

            #making grid
            #self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure(2, weight=1)
            self.grid_rowconfigure(0,weight=1)
            self.grid_rowconfigure(1,weight=1)
            self.grid_rowconfigure(2,weight=1)
            self.grid_rowconfigure(3,weight=1)
            self.grid_rowconfigure(4,weight=1)
            self.grid_rowconfigure(5,weight=1)
            self.grid_rowconfigure(6,weight=1)

login.open()
app = App()
#canvas
cnvTest = customtkinter.CTkCanvas(app, width=50,height=40)
pt = Table(cnvTest)

#buttons
btnSelectTab=customtkinter.CTkButton(app, text="Select Table", command=tableSelect.open()) #!!!show_data moet table_select word!!!
btnSelectTab.grid(row=1, column=1, padx=10,pady=10) 
btnAddData=customtkinter.CTkButton(app, text="Add Record")
btnRemoveData=customtkinter.CTkButton(app, text="Remove Record")
btnEditData=customtkinter.CTkButton(app, text="Edit Record")


def returnMain():
    app.mainloop()
#select_table()
