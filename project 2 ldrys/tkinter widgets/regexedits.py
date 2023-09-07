
e4=Entry(h,bg='#ffffff',fg='black',width=35,font=('times',15,'bold'),show="*")
    password='(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?&])'
    findall=re.findall(password,e4.get())
    if (findall):
          messagebox.showinfo("correct","password strong")
    elif():
          messagebox.showerror("correct","password not strong")
        
          p=input("enter the password:")
          password='(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?&])'
          findall=re.findall(password,p)

    elif(findall):
                 messagebox.showinfo("correct","password strong")
          elif():
                 messagebox.showerror("correct","password not strong")
                
    e4.place(x=503,y=477)





password = "R@m@_f0rtu9e$"
          flag = 0
          while True:
              if (len(password)<=8):
               flag = -1
               break
              elif not re.search("[a-z]", password):
               flag = -1
               break
    
              else:
               flag = 0
              messagebox.showinfo("correct","password strong")
              break
 
          if flag == -1:
               print("Not a Valid Password ")


               password='((?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?&]))'
          findall=re.findall(password,"e4")
          if (findall):
           messagebox.showinfo("success",'the password is strong')
          else:
           messagebox.showerror("error",'the password is not strong')
                  