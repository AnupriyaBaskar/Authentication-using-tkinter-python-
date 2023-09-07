from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font

h=Tk()
def comboclick(event):
    data=cb.get()
    messagebox.showinfo('meassage',data)
h.geometry("250x250")
h.title('frame')
l=Label(h,text='combo',bg='white',fg='black',padx='30',pady='30',font=('times',15,'bold'))
l.pack(fill='x')
cb=ttk.Combobox(h,width=20,state='readonly')
cb.pack(pady=30)
cb['values']=('python','django','java')
cb.current(0)
m=Frame(h,background='black')

y=Scrollbar(f,orient=VERTICAL)
x=Scrollbar(m,orient=HORIZONTAL)
x.pack(side=RIGHT,fill=X)
y.pack(side=RIGHT,fill=Y)
t=Text(m,height=500,width=500,yscrollcommand=y.set,xscrollcommand=x.set,wrap='none'
       )
x.config(command=t.xview)
y.config(command=t.yview)
for i in range(400):
    t.insert(END,'python tkinter')
t.pack()
m.pack()

cb.bind('<<ComboboxSelected>>',comboclick)
h.mainloop()