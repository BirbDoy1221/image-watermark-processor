from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Image Watermark Processor")

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

image = Image.open('punpun.png')
im2 = Image.open('signature-sample.png')
padding = 20
image.paste(im=im2, box=(0 + padding, image.height - im2.height - padding), mask=im2)
photo = ImageTk.PhotoImage(image)

image.save('testimage.png')

image_label = Label(mainframe, image=photo)
image_label.grid()

root.mainloop()