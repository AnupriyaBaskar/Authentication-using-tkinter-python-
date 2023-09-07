from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import pymysql
import re

obj=Tk()
obj.title("DOLPHIN DRYS")
obj.geometry("900x900")
img=PhotoImage(file="bgfinal2.png")
l1=Label(image=img)
l1.pack()
myfont1=Font(family='times',size=12,weight='bold')





def button():
    h=Toplevel(obj)
    h.geometry("940x1000")
    h.title('REGISTER')
    h.config(bg="#182052")
    img1=PhotoImage(file="loginedit1.png")
    l2=Label(h,image=img1)
    l2.pack(fill="both")
    h.resizable(height="false",width="false")
    myfont2=Font(family='times',size=12,weight='bold')
    l4=Label(h,text="NAME",bg="#182052",fg="white",pady=10,padx=10,relief="flat",width=40,font=myfont2)
    l4.place(x=485,y=120)

    def clear():
         e2.delete(0,END)
         e3.delete(0,END)
         e4.delete(0,END)



    def insert():
          l4=e2.get();
          l5=e3.get();
          l6=e4.get();
      #     password='(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?&])'
      #     findall=re.findall(password,"e4")
      #     if (findall):
      #       messagebox.showinfo("success",'the password is strong')
      #     elif(findall!=True):
      #           messagebox.showerror("error",'the password is not strong')
               
         
            
            
           
          if (e2.get()=="" or e3.get()=="" or e4.get()==""):
                 messagebox.showinfo("Insert status","all required")
         
          
                

          
          else:
                con=pymysql.connect(host="localhost",user="root",passwd="anupriya17",port=3308,database='project')
                cursor=con.cursor()
                cursor.execute("insert into  DATAnu values('"+l4+"','"+l5+"','"+l6+"')")
                cursor.execute("commit")
                messagebox.showinfo("insert status","inserted sucessfully")
                con.close()
                clear()
    
    
                   

                
                
           

    
    e2=Entry(h,bg='#ffffff',fg='black',width=35,font=('times',15,'bold'))
    e2.place(x=503,y=190)

    l5=Label(h,text="E-MAIL ID",bg="#182052",fg="white",pady=10,padx=10,relief="flat",width=40,font=myfont2)
    l5.place(x=485,y=260)

    e3=Entry(h,bg='#ffffff',fg='black',width=35,font=('times',15,'bold'))
    e3.place(x=503,y=334)

    l6=Label(h,text="PASSWORD",bg="#182052",fg="white",pady=10,padx=10,relief="flat",width=40,font=myfont2)
    l6.place(x=485,y=400)
    
    check=IntVar()

    c=Checkbutton(h,text="I agree the terms and conditions",fg="white",bg="#182052",width=40,relief="flat",font=("times",12),variable=check,onvalue=1,offvalue=0)
    c.place(x=480,y=530)
    
    b4=Button(h,text="REGISTER",bg="#ef6b48",fg="white",relief="flat",font=("times",20,"bold"),command=insert)
    b4.place(x=600,y=575)

    b5=Button(h,text="SIGN IN",bg="#ef6b48",fg="white",relief="flat",width=13,font=("times",20,"bold"),command=login)
    b5.place(x=30,y=320)

    

    e4=Entry(h,bg='#ffffff',fg='black',width=35,font=('times',15,'bold'))
    

   
    e4.place(x=503,y=477)

    

    h.mainloop()

def login():
        new=Toplevel(obj)
        new.geometry("960x380")
        new.title("login")
        img2=PhotoImage(file="sign.png")
        l7=Label(new,image=img2)
        l7.pack(fill="both")
        def newwindow():
             newwins=Toplevel(new)
             newwins.geometry("1000x1200")
             newwins.title("WELCOME")
             newi=PhotoImage(file="loginnew2edit.png")
             lanewi=Label(newwins,image=newi)
             lanewi.pack(fill="both")
             newwins.resizable(height="false",width="false")
             newwins.mainloop()
       

        def loginuser():
          if (e5.get()=="" or e6.get()==""):
                messagebox.showerror("Insert status","all fields are required")
          else:
                con=pymysql.connect(host="localhost",user="root",passwd="anupriya17",port=3308,database='project')
                cursor=con.cursor()
                cursor.execute("use project")
                E=e5.get()
                E1=e6.get()
                cursor.execute("select * from DATAnu where name=%s and password=%s",[(E),(E1)])
                row=cursor.fetchone()
                if row==None:
                      messagebox.showerror("ERROR","invalid username or password")
                else:
                      messagebox.showinfo("SUCCESS","logged in")
                      cursor.execute("commit")
                      con.close()
                      newwindow()

        
                           
                           
                     
                      
                
                
                
                
         
        myfont2=Font(family='times',size=10,weight='bold')

        b6=Button(new,text="LOGIN",bg="#ef6b48",fg="white",relief="flat",font=("times",18,"bold"),command=loginuser)
        b6.place(x=600,y=300)
        

        l6=Label(new,text="USERNAME",bg="#182052",fg="white",pady=10,padx=10,relief="flat",width=35,font=myfont2)
        l6.place(x=510,y=80)

        e5=Entry(new,bg='#ffffff',fg='black',width=25,font=('times',15,'bold'))
        e5.place(x=518,y=135)

        l7=Label(new,text="PASSWORD",bg="#182052",fg="white",pady=10,padx=10,relief="flat",width=35,font=myfont2)
        l7.place(x=510,y=180)

        e6=Entry(new,bg='#ffffff',fg='black',width=25,font=('times',15,'bold'),show="*")
        e6.place(x=518,y=230)


        b7=Button(new,text="Want help connect with us click here!!",bg="#ef6b48",fg="white",relief="flat",font=("times",14,"bold"))
        b7.place(x=50,y=260)
        

        
        new.resizable(height="false",width="false")
        new.mainloop()


def close():
      obj.destroy()
def services():
      s=Toplevel(obj)
      s.geometry("1000x800")
      s.title("SERVICES")
      se=PhotoImage(file="services4.png")
      lase=Label(s,image=se)
      lase.pack(fill="both")
      s.mainloop()
def aboutus():
      a=Toplevel(obj)
      a.geometry("1000x1000")
      a.title("ABOUT US")
      aii=PhotoImage(file="aboutus9.png")
      ai=Label(a,image=aii)
      ai.pack(fill="both")
      a.mainloop()

b1=Button(obj,text="MENU",font=myfont1,bg="#005ad2",fg="white",activebackground="#1E90FF",relief="flat",width=10,height=2)
b1.place(x=150,y=19)

B=Button(obj,text="ABOUT US",font=myfont1,bg="#005ad2",fg="white",activebackground="#1E90FF",relief="flat",command=aboutus,width=10,height=2)
B.place(x=240,y=19)

B1=Button(obj,text="SERVICES",font=myfont1,bg="#005ad2",fg="white",activebackground="#1E90FF",relief="flat",command=services,width=10,height=2)
B1.place(x=340,y=19)


B2=Button(obj,text="LOGIN",font=myfont1,bg="#005ad2",fg="white",activebackground="#1E90FF",relief="flat",command=login,width=10,height=2)
B2.place(x=440,y=19)

B4=Button(obj,text="CLOSE",font=myfont1,bg="#005ad2",fg="white",activebackground="#1E90FF",relief="flat",command=close,width=10,height=2)
B4.place(x=630,y=19)

B3=Button(obj,text="SIGN UP",font=myfont1,bg="#005ad2",fg="white",activebackground="#1E90FF",relief="flat",command=button,width=10,height=2)
B3.place(x=540,y=19)

obj.resizable(width="false",height="false")



obj.mainloop()