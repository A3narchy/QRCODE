from tkinter import *
from tkinter import tk



#img = qrcode.make('+79125020383 Игорь')
#type(img)
#img.save("some_file.png")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
