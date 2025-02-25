from tkinter import *

root = Tk()
root.title('New Window')

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(index=0, weight=1)
root.rowconfigure(index=0, weight=1)

new_window = Button(mainframe, text='New Window', command=root.destroy)
new_window.grid(column=1, row=1)

root.mainloop()