import os
import tkinter as tk
from tkinter import ttk
import PIL
from PIL import ImageTk, Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 321, height = 100, bg = 'gray1', relief = 'raised')
canvas1.pack()

ft = ttk.Frame()
#function to call python file
def firstFile ():
    global ein
    ein = 'python3 csvread.py '

    os.system(ein)

#button

button1 = tk.Button(text='     run    ', command=firstFile, bg='burlywood3', fg='gray1', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 50, window=button1)


#image

img = ImageTk.PhotoImage(Image.open('/home/pvl/GOS/gos-telemetry/GOS1.png'))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "no")




root.mainloop()
