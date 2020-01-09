import Hospital_Database as hd
print(hd)
import tkinter as tk

r=tk.Tk()
r.title("Medical Info")
r.geometry('1920x1080')

title=tk.Label(r,text="MEDICAL FORM",font=50,fg='red')
title.place(x=600,y=100)

#for patient name
date_of_examinition_of_patient=tk.Label(r,text="Enter Date Of Examinition ",font='20')
date_of_examinition_of_patient.place(x=450,y=200)
date_of_examinition_of_patient=tk.Entry(r,width=50)
date_of_examinition_of_patient.place(x=700,y=205)

#for patient address
p_problem=tk.Label(r,text="Enter Patient Problem",font='20')
p_problem.place(x=450,y=300)
p_problem=tk.Entry(r,width=50)
p_problem.place(x=700,y=305)


def submit_data():
    Date_of_examination = date_of_examinition_of_patient.get()
    Problem=p_problem.get()
    hd.cursor.execute("INSERT INTO medical(Date_of_examination,Problem) VALUES('%s','%s')"%(Date_of_examination,Problem))
    hd.database.commit()
#for submit button
submit_button=tk.Button(r,text="Submit",font=20,command=submit_data)
submit_button.place(x=700,y=505)
r.mainloop()