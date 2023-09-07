from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
o=Tk()
o.title('project')
o.geometry('900x900')
global sno
sno=1
def addrecord():
    pass
def select():
    pass
def update():
    pass
def delete():
    pass
def delete_all():
    pass
frame=Frame(o,bg='blue',width='500',height='200',highlightbackground='black',highlightthickness=3,pady=50,padx=200)
lblnew1=Label(frame,text='NAME',font=('times',15,'bold'),pady=10,bg='blue')
lblnew2=Label(frame,text='ADDRESS',font=('times',15,'bold'),pady=15,bg='blue')
lblnew3=Label(frame,text='E-MAIL ID',font=('times',15,'bold'),pady=25,bg='blue')
lblnew4=Label(frame,text='PHONE NO',font=('times',15,'bold'),pady=25,bg='blue')

mlp=PhotoImage(file="imap.png")
mllabel=Label(M,image=mlp)
mllabel.pack()
t1=Entry(frame,font=('times',15,'bold'))
t2=Entry(frame,font=('times',15,'bold'))
t3=Entry(frame,font=('times',15,'bold'))
t4=Entry(frame,font=('times',15,'bold'))

t1.grid(row=1,column=5)
t2.grid(row=2,column=5)
t3.grid(row=3,column=5)
t4.grid(row=4,column=5)

frame2=Frame(o,pady=20)

b=Button(frame2,text='Addrecord',bg='#1289A7',width=10,padx=5,pady=5,fg='black',activebackground='red',font=('times',15,'bold'),command=addrecord)
frame.pack()
b1=Button(frame2,text='Select',bg='#10ac84',width=10,padx=5,pady=5,fg='black',activebackground='red',font=('times',15,'bold'),command=select)
b2=Button(frame2,text='update',bg='#3c6382',width=10,padx=5,pady=5,fg='black',activebackground='red',font=('times',15,'bold'),command=update)
b3=Button(frame2,text='delete',bg='#d63031',width=10,padx=5,pady=5,fg='black',activebackground='red',font=('times',15,'bold'),command=delete)
b4=Button(frame2,text='delete all',bg='#0a3d62',width=10,padx=5,pady=5,fg='black',activebackground='red',font=('times',15,'bold'),command=delete_all)
frame.pack()
frame2.pack()
b.grid(row=1,column=0,pady=10,padx=5)
b1.grid(row=1,column=1,pady=10,padx=5)
b2.grid(row=1,column=2,pady=10,padx=5)
b3.grid(row=1,column=3,pady=10,padx=5)
b4.grid(row=1,column=3,pady=10,padx=5)

lblnew1.grid(row=1,column=0,sticky=E)
lblnew2.grid(row=2,column=0,sticky=E)
lblnew3.grid(row=3,column=0,sticky=E)
lblnew4.grid(row=4,column=0,sticky=E)

mytree=ttk.Treeview(o)
mytree['columns']=('S.NO','NAME','ADDRESS','EMAIL-ID','PHONE NO')
mytree.column('#0',width=0,stretch=NO)
mytree.column('#1',width=20)
mytree.column('#2',width=60)
mytree.column('#3',width=100)
mytree.column('#4',width=80)
mytree.column('#5',width=70)

mytree.heading('#0',text='')
mytree.heading('#1',text='S.NO')
mytree.heading('#2',text='NAME')
mytree.heading('#3',text='ADDRESS')
mytree.heading('#4',text='E-MAIL ID')
mytree.heading('#5',text='PHONE NO')

#mytree.insert('',index=0,values=(1,'sathya','salem','salem@gmail.com','6383651824'))
data=[
    ['sathya','salem','salem@gmail.com','6383651824'],
    ['anu','salem','salem@gmail.com','6383651824'],
    ['aishu','salem','salem@gmail.com','6383651824'],
    ['baskar','salem','salem@gmail.com','6383651824'],
    ['lakshmi','salem','salem@gmail.com','6383651824'],
    ['baskarm','salem','salem@gmail.com','6383651824'],
]
for datas in data:
    mytree.insert('',index='end',iid=sno,values=(sno,datas[0],datas[1],datas[2],datas[3]))
    sno+=1
mytree.pack(fill=X)
o.mainloop()




