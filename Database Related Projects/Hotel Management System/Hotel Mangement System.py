import tkinter as tk
# from Hotel_Database import *
# import Hotel_Database as hd
from tkinter import *


r=tk.Tk()
r.geometry('1920x1080')
r.title("Hospital Management System")

def raise_frame(Frame):
    Frame.tkraise()


Frame1=Frame(r)
Frame2=Frame(r)
Frame3=Frame(r)
Frame4=Frame(r)

for Used_frame in(Frame1,Frame2,Frame3,Frame4):
    Used_frame.grid(row=0,column=0)


def Hotel_Details():
    raise_frame(Frame1)
    r.title("Hotel Details")
    H_name=tk.Label(Frame1,text="Enter hotel name")
    H_name.grid(row=0,column=1,padx=10,pady=10)
    
    H_name=tk.Label(Frame1,text="Enter hotel name")
    H_name.grid(row=1,column=3,padx=10,pady=10)
   
    
Hotel_Details()
r.mainloop()