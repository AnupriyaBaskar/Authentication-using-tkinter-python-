
from tkinter import *
from tkinter import messagebox



o=Tk()
def data():
    messagebox.showinfo('message','thankyou!!!')

o.geometry('500x500')
l1= Label(o,text='LOGIN PAGE',font=('times',27,'bold'))
#l1.pack() we cannot use pack in the grid method
l1.grid(row=0,column=0)
#name=input('enter the password:')
l= Label(o,text='REGISTRATION',font=('times',15,'bold'),pady=20)
l.grid(columnspan=4)
lbl=Label(o,text='NAME',font=('times',15,'bold'),pady=20)
entry=Entry(o,bg='white',fg='black')
lbl.grid(row=9,column=0)
l.grid(row=8,column=0)
button=Button(o,text='submit',fg='black',bg='white',padx=20,pady=20,font=('times',15,'bold'),command=data)
button.grid(row=15,columns=2)
button1=Button(o,text='clear',fg='black',bg='white',padx=20,pady=20,font=('times',15,'bold'))
button1.grid(row=15,columns=2,sticky=W)
o.mainloop()