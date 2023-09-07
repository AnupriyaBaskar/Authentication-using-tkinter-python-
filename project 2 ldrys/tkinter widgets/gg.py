import tkinter as tk
from PIL import ImageTk, Image

path = 'https://www.bing.com/ck/a?!&&p=372f9d76ea28ee0bJmltdHM9MTY4Mjk4NTYwMCZpZ3VpZD0zZDBlZjcwNi0xYjMyLTZlMWItMjVmYi1lNWEyMWFlMDZmYWUmaW5zaWQ9NTYwNg&ptn=3&hsh=3&fclid=3d0ef706-1b32-6e1b-25fb-e5a21ae06fae&u=a1L2ltYWdlcy9zZWFyY2g_cT1pbWFnZXMgb2YgbmF0dXJlJkZPUk09SVFGUkJBJmlkPUQwNUE1NDExRUE2NEI0QzVDQzk3NUEzMTg3NjVFNDcyNjlGRTk0RDk&ntb=1'

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()