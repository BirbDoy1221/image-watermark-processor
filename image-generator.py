from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageEnhance
from sys import argv

link = argv[1]

img = Image.open(link)
enh = ImageEnhance.Contrast(img)

box = (0, 0, 64, 64)
region = img.crop(box)
region = region.transpose(Image.Transpose.ROTATE_180)
img.paste(region, box)


root = Tk()
img = ImageTk.PhotoImage(img)
root.title('Random Image Composer')


mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(mainframe, image=img).grid(column=3, row=1, sticky=(W,E))


root.mainloop()
