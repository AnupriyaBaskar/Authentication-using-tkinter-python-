from tkinter import *
from tkinter import messagebox
h=Tk()
h.geometry("800x800")
h.title('check button')
def submit():
    if(c1.get()==1):
        val=chk1.cget("text")
        #val=c1.get()
        messagebox.showinfo('message',val)
    if(c2.get()==1):
        val=chk1.cget("text")
        #val=c2.get()
        messagebox.showinfo('message',val)
    if(c3.get()==1):
        val=chk1.cget("text")
        #val=c3.get()
        messagebox.showinfo('message',val)
def clear():
     chk1.deselect()
     chk2.deselect()
     chk3.deselect()
     messagebox.showinfo('message','clear')


           
c1=IntVar()
c2=IntVar()
c3=IntVar()
label=Label(h,text='NAME',fg='black',bg='blue',padx='15',pady='15',font=('times',20,'bold'))
label.pack(fill='x')
chk1=Checkbutton(h,text="male",variable=c1,onvalue=1,offvalue=0)
chk2=Checkbutton(h,text="female",variable=c2,onvalue=1,offvalue=0)
chk3=Checkbutton(h,text="others",variable=c3,onvalue=1,offvalue=0)
button=Button(h,text='submit',fg='black',bg='white',padx=20,pady=20,font=('times',15,'bold'),command=submit)
button1=Button(h,text='clear',fg='black',bg='white',padx=20,pady=20,font=('times',15,'bold'),command=clear)
chk1.pack()
chk2.pack()
chk3.pack()
button.pack()
button1.pack()

h.mainloop()
