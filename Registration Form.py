import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF
from csv import DictWriter
from csv import DictReader
import os

r= tk.Tk()
r.geometry('900x800')
r.title("Registration Form")

v = tk.IntVar()                                                                 #variable for radiobutton
b = tk.IntVar()                                                                 #variable for checkbutton




# function to check whether form is empty or not 
def empty_form():                                                              
    Name=Name_label1.get()
    Name=Name.replace(" ","")                                                             
    if(not Name.isalpha() and len(Name_label1.get())==0):                       
        tk.messagebox.showwarning('Error','Enter Name')
        return(0)
    elif(not (len(MobileNo_label2.get())==10 and (MobileNo_label2.get()).isdigit())):
        tk.messagebox.showwarning('Error','Enter a valid mobile number')
        return(0)
    elif(not("@" in Email_label3.get() and len(Email_label3.get()) >= 5 and (Email_label3.get().endswith('com') or Email_label3.get().endswith('in')))):
        tk.messagebox.showwarning('Error','Enter a valid Email')
        return(0)
    elif(not ( ((Gender_label5).get()=='Male') or Gender_label5.get()=='Female' or  Gender_label5.get()=='Other')):
        tk.messagebox.showwarning('Error','Select Male or Female or Other')
        return(0)
    elif(b.get()==0):
        terms_and_conditions()    
    else:
        return(1)
         
        
# function to print the details in textbox
def check_details():                                                    
    
    if(empty_form()==0):
        pass
    else:
        #textbox state is initially normal
         textbox.config(state="normal")                        
         textbox.insert(tk.END,"Name: "+ Name_label1.get()+"\nMobile No: "+str(MobileNo_label2.get())+"\nEmail: "+Email_label3.get()+"\nAge: "+Age_label4.get()+"\nGender: "+Gender_label5.get()+'\n')
         #after entry it becomes disabled
         textbox.config(state="disabled")                      
        
# function to check terms and condition accepted or not
def terms_and_conditions():                                         
    if(b.get()==0):
        tk.messagebox.showwarning('Warning','Accept Terms and Condtions ')
        #if terms & condition not accepted txt,pdf,csv button will be disabled
        get_txt.config(state=DISABLED)                     
        get_pdf.config(state=DISABLED)
        get_csv.config(state=DISABLED)
    else:
        tk.messagebox.showinfo('Message',' Terms and Condtions Accepted ')
         #if terms & condition accepted txt,pdf,csv button will be enabled 
        get_txt.config(state=NORMAL)                       
        get_pdf.config(state=NORMAL)
        get_csv.config(state=NORMAL)


# function to clear the contents of textbox
def clear_details():
    textbox.config(state=NORMAL)
    textbox.delete(1.0,tk.END)  
    textbox.config(state=DISABLED)   

 # function to convert into text file
def func_convert_txt():                                                        
    if(not empty_form()):
        pass
    else:
        with open('D:\Python\Registration Details.txt','a+') as f:
            f.seek(0)
            x=f.read()
            #to check whether entry is repeated or not
            if(MobileNo_label2.get() in x or Email_label3.get() in x ): 
                tk.messagebox.showwarning('Warning',"Mobile No. or Email is already present")   
            else:
                f.write("\nName :"+Name_label1.get()+"\nMobile no: "+MobileNo_label2.get()+"\nEmail : "+Email_label3.get()+"\nAge : "+Age_label4.get()+"\nGender: "+Gender_label5.get())        
 
#  function to convert into  pdf file
def func_convert_pdf():
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial',size=12)
    pdf.cell(200,10,txt="Name = "+Name_label1.get(),ln=1)
    pdf.cell(200,10,txt="Mobile No = "+MobileNo_label2.get(),ln=2)
    pdf.cell(200,10,txt="Email = "+Email_label3.get(),ln=3)
    pdf.cell(200,10,txt="Age = "+Age_label4.get(),ln=4)
    pdf.cell(200,10,txt="Gender = "+Gender_label5.get(),ln=5)
    pdf.output("D:\Python\Registration Details.pdf")


#  function to convert into csv file
def func_convert_csv():
    x=0
    file=open('D:\Python\Registration Details.csv','a',newline="")
    dict_write=DictWriter(file,fieldnames=['Name','Mobile No.','Email','Age','Gender'])
    dict_read=DictReader(open("Registration Details.csv"))
    for row in dict_read:
        #to check the repetition of values in file
        if(MobileNo_label2.get() in row['Mobile No.']  or  Email_label3.get() in  row['Email'] ):
            x=1  
    if(not empty_form()):
        pass
    elif(x==1):    
        tk.messagebox.showwarning('Warning',"Mobile No. or Email is already present")    
    else:
        # if initially when the size of file is 0 the heading is displayed  
        if(os.path.getsize('D:\Python\Registration Details.csv')==0):  
            dict_write.writeheader()
        
        
        dict_write.writerow({
            'Name': Name_label1.get(),
            'Mobile No.': MobileNo_label2.get(),
            'Email':Email_label3.get(),
            'Age': Age_label4.get(),
            'Gender': Gender_label5.get()})

   

 #title label
heading=tk.Label(r,text='Registration Form',font=('red',35),fg ='red')          
heading.place(x=270,y=20)
 
 #name label
Name_label1=tk.Label(r,text='Name',font=30)                                     
Name_label1.place(x=200,y=100)
Name_label1=tk.Entry(r,text="Enter your Name",width=50)
Name_label1.place(x=330,y=105)

 #mobile  label
MobileNo_label2=tk.Label(r,text='Mobile No.',font=30)                           
MobileNo_label2.place(x=200,y=150)
MobileNo_label2=tk.Entry(r,text="Enter your Mobile No.",width=50)
MobileNo_label2.place(x=330,y=155)

#email label
Email_label3=tk.Label(r,text='Email ID',font=30)                                  
Email_label3.place(x=200,y=200)
Email_label3=tk.Entry(r,text="Enter your Email",width=50)
Email_label3.place(x=330,y=205)

 #age label
Age_label4=tk.Label(r,text='Age',font=30)                                         
Age_label4.place(x=200,y=250)
Age_label4=Spinbox(r,from_=1,to=100,width=49)
Age_label4.place(x=330,y=255)

#gender label
Gender_label5=tk.Label(r,text='Gender',font=30)                                    
Gender_label5.place(x=200,y=300)
Gender_label5=ttk.Combobox(r,values=['Male','Female','Other'],width=49)
Gender_label5.place(x=330,y=305)

 #Eligibility radio button
Eligible_radio=tk.Label(r,text='Eligibility',font=30)                              
Eligible_radio.place(x=200,y=355)
Eligible_radio=tk.Radiobutton(r,text="Eligible", variable=v,value='1',font=30)
Eligible_radio.place(x=350,y=355)
Eligible_radio=tk.Radiobutton(r,text="Not Eligible", variable=v,value='2',font=30)
Eligible_radio.place(x=450,y=355)
v.set(1)

#terms & condition checkbutton
terms=tk.Checkbutton(r,text='Agree Terms and Condition',font=30,variable=b,command=terms_and_conditions)  
terms.place(x=200,y=405)

 # txt button to convert into txt file 
get_txt=tk.Button(r,text='Get txt',font=25,bg='white',command=func_convert_txt)         
get_txt.place(x=330,y=455)

 # pdf button to convert into pdf file
get_pdf=tk.Button(r,text='Get pdf',font=25,bg='white',command=func_convert_pdf)                                 
get_pdf.place(x=435,y=455)

 # csv button toconver into csv file
get_csv=tk.Button(r,text='Get csv',font=25,bg='white',command=func_convert_csv)                                 
get_csv.place(x=550,y=455)

#display textbox
textbox=tk.Text(r,height=15,width=60,state=DISABLED)                               
textbox.place(x=200,y=505)

#check button for printing details
check_button=tk.Button(r,text='Check',font=25,bg='white',width=10,command=check_details) 
check_button.place(x=700,y=555)

 #clear button for clearing details
clear_button=tk.Button(r,text='Clear',font=25,bg='white',width=10,command=clear_details)                 
clear_button.place(x=700,y=605)

#initailly txt,pdf,csv button are disabled
get_txt.config(state=DISABLED)                                                 
get_pdf.config(state=DISABLED)
get_csv.config(state=DISABLED)


r.mainloop()


   