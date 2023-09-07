from tkinter import *
import tkinter.messagebox as MessageBox
import  pymysql as mysql


obj=Tk()
obj.geometry('800x800')
obj.title('list')
obj.config(bg='blue')


# def submit():
#     data=a.get()
#     l.insert(END,data)
# def select():
#     data=l.get(ANCHOR)
#     MessageBox.showinfo('message',data)
#
#
#
# a=Entry(obj,width=30)
# a.pack()
# l=Listbox(obj,width=30,height=15)
# l.pack(pady=20)
# l.insert(END,'hello')
# mydata=['c.net','d.net','anu','aishu','baskar','lakshmi','c','C++','java','python','web']
# for data in mydata:
#     l.insert(END,data)
# for i in range(2):
#     l.insert(END,'python')
# b=Button(obj,text='submit',pady=10,padx=10,bg='green',fg='white',width=15,font=('times',15,'bold'),activebackground='red',command=submit)
# b1=Button(obj,text='submit',pady=10,padx=10,bg='green',fg='white',width=15,font=('times',15,'bold'),activebackground='red',command=select)
# b.pack()
# b1.pack()
# obj.mainloop()












