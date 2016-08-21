
import PIL
import urllib
import Tkinter
from Tkinter import *
from PIL import ImageTk
from PIL import Image

local_filename, header = urllib.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg")

basewidth = 200
hola = Image.open(local_filename)
wpercent = (basewidth / float(hola.size[0]))
hsize = int((float(hola.size[1]) * float(wpercent)))
hola2 = hola.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

#Creates the master window
master = Tk()

#image = "./images/python_small.png"
#image = open(hola2)

logo = ImageTk.PhotoImage(hola2)
#logo = PhotoImage(Image.open("./images/python_small.png"))

#Organize the images their right positions
frameTop = Frame(master)
w1 = Label(frameTop, image=logo,text="1001",fg="red", compound=Tkinter.TOP).pack(side="left")
w2 = Label(frameTop, image=logo,text="2001",fg="red", compound=Tkinter.TOP).pack(side="left")
frameTop.pack(side="top")

frameBottom = Frame(master)
w3 = Label(frameBottom, image=logo, text="2001",fg="red", compound=Tkinter.TOP).pack(side="left")
w4 = Label(frameBottom, image=logo,text="2001",fg="red", compound=Tkinter.TOP).pack(side="left")
frameBottom.pack(side="bottom")

master.mainloop()

