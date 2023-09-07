from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import pymysql


def submit():
    data=d.get()
    #label=Label(obj,text=data,font=('times',10))
    #label.pack()
    messagebox.showinfo('Message',data)
obj=Tk()
obj.title('sign in')
obj.geometry("900x700")
obj.config(bg="#4169E1")
style1= Font(weight='bold',size='12',family='times')
label=Label(obj,text='First name',fg='black',font=style1)
label1=Label(obj,text='last name',fg='black',font=style1)
label2=Label(obj,text='E-MAIL id',fg='black',font=style1)
label3=Label(obj,text='Contact no',fg='black',font=style1)
label4=Label(obj,text='Password',fg='black',font=style1)
label.place(x=120,y=10)
label1.place(x=120,y=40)
label2.place(x=120,y=70)
label3.place(x='120',y='100')
label4.place(x='120',y='130')
bt=Button(obj,text='submit',padx='15',pady='15',command= submit,font=('times',15))
bt.pack()
#bt.place(x='450',y='150')
#d=Entry(obj,width=30,font= ('times',25),bg='#55efc4',fg='blue',command=entry) we cannot use command in entry
d=Entry(obj,width=30,font= ('times',20),bg='blue',fg='#55efc4',selectbackground='white',selectforeground='black')
d1=Entry(obj,width=30,font= ('times',20),bg='blue',fg='#55efc4',selectbackground='white',selectforeground='black')
d2=Entry(obj,width=30,font= ('times',20),bg='blue',fg='#55efc4',selectbackground='white',selectforeground='black')
d3=Entry(obj,width=30,font= ('times',20),bg='blue',fg='#55efc4',selectbackground='white',selectforeground='black')
d4=Entry(obj,width=30,font= ('times',20),bg='blue',fg='#55efc4',selectbackground='white',selectforeground='black',show='*')
d.pack()
d1.pack()
d2.pack()
d3.pack()
d4.pack()
obj.resizable(width='false',height='false')
obj.mainloop()