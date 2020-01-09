import Hospital_Database as hd
print(hd)
import tkinter as tk

r=tk.Tk()
r.title("Parking")
r.geometry('1920x1080')

title=tk.Label(r,text="Parking FORM",font=50,fg='red')
title.place(x=600,y=100)

#for vehicle number
vehicle=tk.Label(r,text="Enter Vehicle No.",font='20')
vehicle.place(x=450,y=200)
vehicle=tk.Entry(r,width=50)
vehicle.place(x=700,y=205)


def submit_data():
    vehicle_no=vehicle.get()
    hd.cursor.execute("INSERT INTO parking(vehicle_no) VALUES('%s')"%(vehicle_no))
    hd.database.commit()
#for submit button
submit_button=tk.Button(r,text="Submit",font=20,command=submit_data)
submit_button.place(x=700,y=505)
r.mainloop()