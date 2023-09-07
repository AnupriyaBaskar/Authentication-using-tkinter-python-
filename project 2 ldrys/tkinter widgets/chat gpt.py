from tkinter import *
from tkinter import ttk
from tkinter.font import Font
obj=Tk()
obj.title("LD DRYS")
obj.geometry("900x450")
obj.config(bg="black")
def button():
    window=Toplevel(obj)
    window.geometry("900x900")
    window.title("LD DRYS")
    window.config(bg="black")

    myfont2=Font(family='Microsoft YaHei UI Light',size=10,weight='bold',slant='italic')


    

    f1=Frame(window,height=600,width=400,highlightbackground="black",bg="#4169E1")
   
     
    txt=Text(f1,width="43",height="20")
    f1.place(x=475,y=50)
    txt.place(x=500,y=80) 

    #s1=Scrollbar(f1,orient=VERTICAL)
    #s1.pack(side=RIGHT,fill=Y)

    #txt=Text(f1,width="13",height="5")
    
    #txt.pack(side=RIGHT)
    
    
        

    e1=Entry(window,bg='white',fg='black',width=27,font=('times',15,'bold'))
    e1.place(x=500,y=600)
    e1.insert(0,"Hi there!")
    
    b2=Button(window,text="ENTER",font=myfont2,padx=5,pady=1.5)
    b2.place(x=780,y=600)
    window.resizable(width='false',height='false')
    
    f2=Frame(window,height=600,width=400,highlightbackground="grey",bg="#4169E1")
    f2.place(x=30,y=50)

    myfont3=Font(family='Microsoft YaHei UI Light',size=30,weight='bold',slant='italic')
    l2=Label(window,text="REGISTERATION",fg="white",bg="#4169E1",font=myfont3,highlightcolor="white")
    l2.place(x=50,y=100)

    l4=Label(window,text="NAME",fg="black",pady=10,padx=10)
    l4.place(x=75,y=200)

    e2=Entry(window,bg='white',fg='black',width=20,font=('times',15,'bold'))
    e2.place(x=190,y=205)

    l5=Label(window,text="CONTACT NO",fg="black",pady=10,padx=10)
    l5.place(x=75,y=260)

    e3=Entry(window,bg='white',fg='black',width=20,font=('times',15,'bold'))
    e3.place(x=190,y=265)

    l6=Label(window,text="ADDRESS",fg="black",pady=10,padx=10)
    l6.place(x=75,y=320)

    e4=Entry(window,bg='white',fg='black',width=20,font=('times',15,'bold'))
    e4.place(x=190,y=325)

    l7=Label(window,text="E-MAIL-ID",fg="black",pady=10,padx=10)
    l7.place(x=75,y=380)

    e5=Entry(window,bg='white',fg='black',width=20,font=('times',15,'bold'))
    e5.place(x=190,y=385)


    b2=Button(window,text="REGISTER",pady=5,padx=5,bg='#10ac84',width=10,fg='white',activebackground='red',font=('times',15,'bold'))
    b2.place(x=150,y=450)

    l7=Label(window,text="ALREADY A USER?",fg="white",bg="#4169E1",pady=10,padx=10,font=("times",13,"bold"))
    l7.place(x=140,y=515)
    
    

    def login():
        w4=Toplevel(window)
        w4.geometry("500x500")
        w4.title("LD DRYS")

    b3=Button(window,text="LOGIN",pady=5,padx=5,bg='#1289A7',width=10,fg='white',activebackground='red',font=('Microsoft YaHei UI Light',15,'bold'),command=login)
    b3.place(x=150,y=575)

    
    
    
    def about():
        w2=Toplevel(window)
        w2.geometry("900x900")
        w2.title("LD DRYS")
    def services():
        w3=Toplevel(window)
        w3.geometry("900x900")
        w3.title("LD DRYS")  
    m=Menu(window)
    f=Menu(m,tearoff=0)
    f.add_command(label='ABOUT US',activebackground="#4169E1",background="black",foreground="white", command=about)
    f.add_separator()
    f.add_command(label='SERVICES',activebackground="#4169E1",background="black",foreground="white",command=services)
    f.add_separator()
    f.add_command(label='EXIT',command=window.destroy,activebackground="#4169E1",background="black",foreground="white")
    m.add_cascade(label='MENU',menu=f,foreground="black")
    window.config(menu=m)
    

    
myfont=Font(family='Microsoft YaHei UI Light',size=60,weight='bold',slant='italic')
myfont1=Font(family='Microsoft YaHei UI Light',size=25,weight='bold',slant='italic')
l1=Label(obj,text="WELCOME TO LD DRYS",font=myfont,bg="black",fg="white",pady=150)
b1=Button(obj,text="CLICK HERE",font=myfont1,bg="black",fg="white",activebackground="red",relief="groove",command=button)
l1.pack()
b1.place(x=350,y=250)
obj.resizable(width='false',height='false')
obj.mainloop()