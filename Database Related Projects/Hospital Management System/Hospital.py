import Hospital_Database as hd
import tkinter as tk
from tkinter import *

r=tk.Tk()
r.title("Hospital Info")
r.geometry('1920x1080')





title=tk.Label(r,text="HOSPITAL FORM",font=50,fg='red')
title.place(x=600,y=100)

#for hospital name
Hospital_name=tk.Label(r,text="Enter Hospital Name",font='20')
Hospital_name.place(x=450,y=200)
Hospital_name=tk.Entry(r,width=50)
Hospital_name.place(x=700,y=205)

#for hospital address
Hospital_address=tk.Label(r,text="Enter Hospital Address",font='20')
Hospital_address.place(x=450,y=300)
Hospital_address=tk.Entry(r,width=50)
Hospital_address.place(x=700,y=305)

#for hospital city
Hospital_city=tk.Label(r,text="Hospital City",font='20')
Hospital_city.place(x=450,y=400)
Hospital_city=tk.Entry(r,width=50)
Hospital_city.place(x=700,y=405)

def submit_data():
    H_name=Hospital_name.get()
    H_address=Hospital_address.get()
    H_city=Hospital_city.get()
    hd.cursor.execute("INSERT INTO hospital(H_name,H_address,H_city) VALUES('%s','%s','%s')"%(H_name,H_address,H_city))
    hd.database.commit()
    
#for submit button
submit_button=tk.Button(r,text="Submit",font=20,command=submit_data)
submit_button.place(x=700,y=505)

# next_button=tk.Button(Frame1,text="Next",font=20,command=lambda:frame_raise(Frame2))
# next_button.grid(row=0,column=1)

# frame_raise(Frame1)
r.mainloop()