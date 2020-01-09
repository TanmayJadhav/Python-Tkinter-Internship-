import tkinter as tk
from tkinter import *
import Login_Signup_Database as hd
import random
import string 
from string import *
from tkinter import messagebox
from cryptography.fernet import Fernet
from tkcalendar import Calendar
from tkinter import filedialog


r=tk.Tk()
r.title('Home Page')
r.geometry('700x600')




def raise_frame(Frame):
    Frame.tkraise()

Frame1=Frame(r)
Frame2=Frame(r)
Frame3=Frame(r)
Frame4=Frame(r)




def Login_Form():
    raise_frame(Frame2)
    r.title('Login Form')
    L_title=tk.Label(Frame2,text="Login Page",font='20')
    L_title.grid(row=0,column=0,padx=100,pady=10)    

    Login_Email=tk.Label(Frame2,text="Email",font='10')
    Login_Email.grid(row=1,column=0,pady=50)   
    Login_Email=tk.Entry(Frame2)
    Login_Email.grid(row=1,column=1)
    
    Login_Password=tk.Label(Frame2,text="Password",font='10')
    Login_Password.grid(row=2,column=0,pady=20)   
    Login_Password=tk.Entry(Frame2,show="*")
    Login_Password.grid(row=2,column=1)

    def submit():
        email_password="SELECT * FROM details WHERE email='%s' and password='%s'"%(Login_Email.get(),Login_Password.get())
        hd.cursor.execute(email_password)
        data=hd.cursor.fetchone()
        
        try:
            if(Login_Password.get() in data and Login_Email.get() in data and (("@" in Login_Email.get() and len(Login_Email.get()) >= 5 and (Login_Email.get().endswith('com') or Login_Email.get().endswith('in'))))):
                pass
            first_page(Login_Email.get())    
        except:
            tk.messagebox.showerror('Error','Invalid Email or Password ')


    Submit=tk.Button(Frame2,text="Login",font='10',command=submit)
    Submit.grid(row=3,column=1,pady=20) 

    back_button=tk.Button(Frame2,text="Back",font='10',command=lambda:raise_frame(Frame1))
    back_button.grid(row=4,column=2,pady=20)   


def signup_form():
    raise_frame(Frame3)
    r.title('Signup Form')
    S_title=tk.Label(Frame3,text="Signup Page",font='20')
    S_title.grid(row=0,column=0,padx=100,pady=10)    

    Signup_name=tk.Label(Frame3,text="Name",font='10')
    Signup_name.grid(row=1,column=0,pady=20)   
    Signup_name=tk.Entry(Frame3)
    Signup_name.grid(row=1,column=1)
   
    
    Signup_Email=tk.Label(Frame3,text="Email",font='10')
    Signup_Email.grid(row=2,column=0,pady=20)   
    Signup_Email=tk.Entry(Frame3)
    Signup_Email.grid(row=2,column=1)  

    Signup_Password=tk.Label(Frame3,text="Password",font='10')
    Signup_Password.grid(row=3,column=0,pady=20)   
    Signup_Password=tk.Entry(Frame3,show="*")
    Signup_Password.grid(row=3,column=1)

    key = Fernet.generate_key()
    f = Fernet(key)
    E_password=bytes(Signup_Password.get(),encoding='utf8')
    E_password=f.encrypt(E_password)

    Signup_Confirm_Password=tk.Label(Frame3,text="Confirm Password",font='10')
    Signup_Confirm_Password.grid(row=4,column=0,pady=20)   
    Signup_Confirm_Password=tk.Entry(Frame3,show="*")
    Signup_Confirm_Password.grid(row=4,column=1)

    Captcha=tk.Label(Frame3,text="Captcha",font='10')
    Captcha.grid(row=5,column=0,pady=20)   
    Captcha=tk.Entry(Frame3)
    Captcha.grid(row=5,column=1)

    def randomStringDigits(stringLength=6):
        global R_Captcha
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        R_Captcha=''.join(random.choice(lettersAndDigits) for i in range(stringLength))
        Refresh_Captcha=tk.Label(Frame3,text=R_Captcha,width=10)
        Refresh_Captcha.grid(row=5,column=3)

        
    randomStringDigits(6)
    Refresh_Captcha=tk.Button(Frame3,text="Refresh",font='10',command=lambda:randomStringDigits(6))
    Refresh_Captcha.grid(row=5,column=2,pady=20)
       
    def submit():
        Name=Signup_name.get()
        Name=Name.replace(" ","") 
        if(not R_Captcha==Captcha.get() ):
            tk.messagebox.showerror("Error","Invalid Captcha!!")
        elif(not Signup_Confirm_Password.get()==Signup_Password.get()):
            tk.messagebox.showerror("Error","Password does not match!!")
        elif(not("@" in Signup_Email.get() and len(Signup_Email.get()) >= 5 and (Signup_Email.get().endswith('com') or Signup_Email.get().endswith('in')))):    
            tk.messagebox.showerror("Error","Invalid Email!!")
        elif(not Name.isalpha() and len(Name.get())==0):
            tk.messagebox.showerror("Error","Invalid Name!!")
        else:
           
            name=Signup_name.get()
            email=Signup_Email.get()
            password=E_password
            InsertData="INSERT INTO details(name,email,password) VALUES('%s','%s','%s')"%(name,email,password)
            hd.cursor.execute(InsertData)
            hd.database.commit()
                       


        
                 
    Submit=tk.Button(Frame3,text="Submit",font='10',command=submit)
    Submit.grid(row=6,column=1,pady=20)   

    back_button=tk.Button(Frame3,text="Back",font='10',command=lambda:raise_frame(Frame1))
    back_button.grid(row=7,column=2,pady=20)   
    
    
def first_page(user_email):


    def Submit_details():
        age=Age.get()
        DOB=var
        image=Image
        about=About.get()
        insert="INSERT INTO user_info(age,DOB,image,about) VALUES('%s','%s','%s','%s')"%(age,DOB,image,about)
        hd.cursor.execute(insert)
        hd.database.commit()


    raise_frame(Frame4)
    r.title('First Page')

    title=tk.Label(Frame4,text=" Fill Details",font='20')
    title.grid(row=0,column=0,padx=100,pady=10)    
    
    username="SELECT * FROM details WHERE email='%s'"%(user_email)
    hd.cursor.execute(username)
    name=hd.cursor.fetchone()

    name_logout=tk.Label(Frame4,text=name[1],font='10')
    name_logout.grid(row=1,column=4)   
    name_logout_button=tk.Button(Frame4,text="Logout",command=lambda:raise_frame(Frame1))
    name_logout_button.grid(row=2,column=4)    
    
    Age=tk.Label(Frame4,text="Age",font='10')
    Age.grid(row=3,column=0,pady=20)   
    Age=tk.Entry(Frame4)
    Age.grid(row=3,column=1)

    def calendar():
        global D_DOB
        
        top=tk.Toplevel(Frame4)
        def print_set():
            global var
            var=Cal.selection_get()
            D_DOB=tk.Label(Frame4,text=var,font='20')
            D_DOB.grid(row=4,column=1,pady=20)
            top.destroy()
            
        Cal=Calendar(top,font="Arial 14",selectmode='day',cursor='hand1')
        Cal.pack()
        btn=tk.Button(top,text='ok',command=print_set).pack()

    DOB=Button(Frame4,text='Date of Birth',command=calendar,font='20')
    DOB.grid(row=4,column=0,pady=20)   
    
    def Image_upload():
        global Image
        Image=filedialog.askopenfilename(initialdir=' ',title='Select Image file',filetypes=(('png files','*.png'),))
        Image_address=tk.Label(Frame4,text=Image,font='20')
        Image_address.grid(row=5,column=1,pady=20)
        file=open(Image,'rb')
        image_read=file.read()
        print(image_read)
        file.close()
    

    

    
    Upload_Image=tk.Button(Frame4,text="Upload Image",font='20',command=Image_upload)
    Upload_Image.grid(row=5,column=0,pady=20)

    
    
    Submit=tk.Button(Frame4,text="Submit",font='10',command=Submit_details)
    Submit.grid(row=7,column=1,pady=20) 

    About=tk.Label(Frame4,text="About",font='10')
    About.grid(row=6,column=0,pady=20)  
    About=tk.Entry(Frame4)
    About.grid(row=6,column=1,pady=20)  
    


    

for Used_frame in(Frame1,Frame2,Frame3,Frame4):
    Used_frame.grid(row=0,column=0,sticky='news')

title=tk.Label(Frame1,text="Home Page",font='20')
title.grid(row=0,column=0,padx=200,pady=10)    

Login=tk.Button(Frame1,text="Login",font='20',command=Login_Form)
Login.grid(row=1,column=0,pady=50)    

Signup=tk.Button(Frame1,text="Signup",font='20',command =signup_form)
Signup.grid(row=2,column=0)   

raise_frame(Frame1)
r.mainloop()    