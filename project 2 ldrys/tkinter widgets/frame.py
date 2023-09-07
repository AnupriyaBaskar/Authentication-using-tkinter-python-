from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from tkinter.font import Font
h=Tk()

h.geometry("800x800")
h.title('frame')

frame1=Frame(h,highlightbackground='blue',highlightthickness=2,padx='80',pady='80')
frame1.grid(row=0,column=2,padx='40',pady='40')

img=PhotoImage(file='dolphin.png')
label8=Label(h,image=img)
label8.place(x=100,y=100)


style1= Font(weight='bold',size='12',family='Microsoft YaHei UI Light')
label=Label(frame1,text='First name',fg='black',font=style1)
label1=Label(frame1,text='last name',fg='black',font=style1)
label2=Label(frame1,text='E-MAIL id',fg='black',font=style1)
label3=Label(frame1,text='Contact no',fg='black',font=style1)
label4=Label(frame1,text='Password',fg='black',font=style1)
label.grid(columnspan=2)
label1.grid(columnspan=4)
label2.grid(columnspan=6)
label3.grid(columnspan=8)
label4.grid(columnspan=10)

h.mainloop()