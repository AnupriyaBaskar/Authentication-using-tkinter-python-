from tkinter import *

from tkinter.font import Font
h=Tk()

h.geometry("1800x1800")
h.title('frame')


img1=PhotoImage(file="loginedit.png")
l2=Label(image=img1)
l2.pack()


def database():
      if e2.get()=="" or e3.get()=="" or e4.get()=="":
           messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")

h.mainloop()