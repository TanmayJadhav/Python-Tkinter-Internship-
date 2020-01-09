import Hospital_Database as hd
print(hd)
import tkinter as tk

r=tk.Tk()
r.title("Doctor Info")
r.geometry('1920x1080')

title=tk.Label(r,text="Doctor FORM",font=50,fg='red')
title.place(x=600,y=100)

#for patient name
doctor_name=tk.Label(r,text="Enter Doctor Name",font='20')
doctor_name.place(x=450,y=200)
doctor_name=tk.Entry(r,width=50)
doctor_name.place(x=700,y=205)

#for patient address
Salary=tk.Label(r,text="Enter Salary",font='20')
Salary.place(x=450,y=300)
Salary=tk.Entry(r,width=50)
Salary.place(x=700,y=305)

#for patient diagnosis
d_qualification=tk.Label(r,text="Qualification",font='20')
d_qualification.place(x=450,y=400)
d_qualification=tk.Entry(r,width=50)
d_qualification.place(x=700,y=405)

def submit_data():
    D_name=doctor_name.get()
    salary=Salary.get()
    qualification=d_qualification.get()
    hd.cursor.execute("INSERT INTO doctor(D_name,salary,qualification) VALUES('%s','%s','%s')"%(D_name,salary,qualification))
    hd.database.commit()
#for submit button
submit_button=tk.Button(r,text="Submit",font=20,command=submit_data)
submit_button.place(x=700,y=505)
r.mainloop()