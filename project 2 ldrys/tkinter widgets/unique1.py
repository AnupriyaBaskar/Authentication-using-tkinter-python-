from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
def submit():
    #messagebox.showinfo('Message','submitted succesfully!!!')
    # print('submitted succesfull!!!')
    #mylabel=Label(a,text='submitted succesfully!!!',fg='yellow',font=myfont1,bg='black')
    #mylabel.pack()
    messagebox.showinfo('Message','submitted succesfully!!!')
    
def clear1():
    #messagebox.showinfo('Message','cleared succesfully!!!')
    #print('cleared succesfully!!!')
    #mylabel1=Label(a,text='cleared succesfully!!!',fg='yellow',font=myfont1,bg='black')
    #mylabel1.pack()
    messagebox.showinfo('Message','cleared succesfully!!!')
a=Tk()
#'we will declare a label as a variable'
a.geometry("500x500")
a.title('grahical user interface')
a.config(bg="#4169E1")
a.title('tkinter')
#a.resizable(width='false',height='false')

myfont=Font(family='times',size=10,weight='bold',slant='italic')
myfont1=Font(family='times',size=25,weight='bold',slant='italic')
b= Button(a,text='submit',bg='red',font= myfont1, fg='black',activebackground='blue',activeforeground='white',padx='20',pady='5',width=10,command=submit)
#b.pack(side='left')
#fill option can only be used in pack method
#b.pack(fill=Y,expand='true')
#b.pack(fill=BOTH,expand='true')
b.pack(fill=X)
b1= Button(a,text='clear',bg='red',fg='black',activebackground='blue',activeforeground='white',padx='20',pady='5',width=10, command=clear1)
b1.pack(fill='x')
#b1.pack(side='right')
#b.place(x=70,y=80)
#b1.place(x=100,y=140)
label= Label(a,text="LOGIN PAGE",font= myfont,bg="#FA8072",fg="black", padx='60',pady='30',relief='groove')
label.pack()
a.mainloop()

