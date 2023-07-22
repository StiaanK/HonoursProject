import tkinter
from typing import Optional, Tuple, Union
import customtkinter

class TableSelect(customtkinter.CTk):
        def __init__(self):
            super().__init__()

            self.geometry("450x150")
            self.title("Table Select")
            #column config
            self.grid_columnconfigure(0,weight=1)
            self.grid_columnconfigure(1,weight=1)
            #row config
            self.grid_rowconfigure(0,weight=1)
            self.grid_rowconfigure(1,weight=1)
            self.grid_rowconfigure(2,weight=1)      
   
ts = TableSelect()
#labels
lblInfo=customtkinter.CTkLabel(ts, text="Please select a table.")
lblInfo.grid(row=0,column=0,columnspan=2)
#combobox
cbTable=customtkinter.CTkComboBox(ts, width=250, values=["Option 1", "Option 2", "Option 3"]) #!!!Replace placeholders with tables in future!!!
cbTable.grid(row=1,column=0,columnspan=2)
#buttons
btnSelect=customtkinter.CTkButton(ts, text="Select") #make btnSelect command
btnCancel=customtkinter.CTkButton(ts, text="Cancel",command=ts.destroy) 
btnSelect.grid(row=2,column=0,)
btnCancel.grid(row=2,column=1,)

def open():
    ts.mainloop()    