import Hospital_Database as hd
import tkinter as tk


r=tk.Tk()
r.title("Patient Info")
r.geometry('1920x1080')

title=tk.Label(r,text="PATIENT REGISTRATION FORM",font=50,fg='red')
title.place(x=600,y=100)

#for patient name
patient_name=tk.Label(r,text="Enter Patient Name",font='20')
patient_name.place(x=450,y=200)
patient_name=tk.Entry(r,width=50)
patient_name.place(x=700,y=205)

#for patient address
address=tk.Label(r,text="Enter  Address",font='20')
address.place(x=450,y=300)
address=tk.Entry(r,width=50)
address.place(x=700,y=305)

#for patient diagnosis
diagnosis=tk.Label(r,text="Diagnosis",font='20')
diagnosis.place(x=450,y=400)
diagnosis=tk.Entry(r,width=50)
diagnosis.place(x=700,y=405)

def submit_data():
    p_name=patient_name.get()
    p_address=address.get()
    p_diagnosis=diagnosis.get()
    hd.cursor.execute("INSERT INTO patient(p_name,p_address,p_diagnosis) VALUES('%s','%s','%s')"%(p_name,p_address,p_diagnosis))
    hd.database.commit()
    
#for submit button
submit_button=tk.Button(r,text="Submit",font=20,command=submit_data)
submit_button.place(x=700,y=505)

r.mainloop()
