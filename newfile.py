from tkinter import *
import platform
import sys
root = Tk()      
canvas = Canvas(root, width = 500, height = 400)
canvas.pack() 
system = str(sys.platform)
uname = platform.uname()
if system == "linux":
	img2 = PhotoImage(file="123.png")
if system == "win32":
	img2 = PhotoImage(file="windows.png")
if system == "darwin":
	img2 = PhotoImage(file="macosx.png")
if system == "linux":
	img = PhotoImage(file="linux.png")
if system == "win32":
	img = PhotoImage(file="win.png")
if system == "darwin":
	img = PhotoImage(file="macos.jpg")
w = Label(root, text=str(uname.system) + " " + str(uname.release) + " " + str(uname.machine))
w.pack()
canvas.create_image(0,0, anchor=NW, image=img2)
canvas.create_image(0,0, anchor=NW, image=img)  
mainloop()
