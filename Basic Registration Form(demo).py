import tkinter as tk

from tkinter import*
from tkinter import messagebox
r=tk.Tk()
r.geometry("700x700")
r.title("Registration Form")

r.resizable(0,0)


def check_details():
    Name=name.get()
    Name=Name.replace(" ","")
    if(not Name.isdigit() and (len(MobileNo.get())==10 and (MobileNo.get()).isdigit()) and ("@" in Email.get() and len(Email.get()) >= 5 and (Email.get().endswith('com') or Email.get().endswith('in'))) ):
        pass
    else:
        tk.messagebox.showwarning('Error','Enter proper details')
head=tk.Label(r,text="Registration Form",width=50,font=(20),fg='red').grid(row=0,column=2)

label1=tk.Label(r,text="Name",width=20).grid(row=1,column=1)
label2=tk.Label(r,text="Mobile No",width=20).grid(row=2,column=1)

name=tk.Entry(r,text="Enter Your Name",width=20)
name.grid(column=2,row=1)
MobileNo=tk.Entry(r,text="Enter Your Mobile No",width=20)
MobileNo.grid(column=2,row=2)

label3=tk.Label(r,text="Address",width=20).grid(row=3,column=1)
label4=tk.Label(r,text="Email",width=20).grid(row=4,column=1)

Address=tk.Entry(r,text="Enter Your Address",width=20)
Address.grid(column=2,row=3)
Email=tk.Entry(r,text="Enter Your Email",width=20)
Email.grid(column=2,row=4)



def OnClick():
    if(len(name.get())==0 or len(MobileNo.get())==0 or len(Address.get())==0 or len(Email.get())==0  ):
        tk.messagebox.showwarning('Error','Enter proper details')
    else:
        check_details()         
    

submit=tk.Button(r,text="Sumbit",width=10,command=OnClick).grid(row=6,column=2)

r.mainloop()