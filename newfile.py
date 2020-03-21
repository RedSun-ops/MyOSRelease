from tkinter import *
import platform
import sys
from gtts import gTTS 
import os 
language = 'en'
root = Tk()      
canvas = Canvas(root, width = 500, height = 300)
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
info = str(uname.system) + " " + str(uname.release) + " " + str(uname.machine)
speechinfo = str(uname.system) + " " + str(uname.release)
w = Label(root, text=info)
w.pack()
canvas.create_image(0,0, anchor=NW, image=img2)
canvas.create_image(200,120, anchor=NW, image=img)
myobj = gTTS(text=speechinfo, lang=language, slow=False) 
myobj.save("output.mp3") 
os.system("start output.mp3") 
mainloop()

