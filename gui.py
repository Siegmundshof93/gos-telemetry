import os
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 350, bg = 'gray22', relief = 'raised')
canvas1.pack()


def firstFile ():
    global ein
    ein = 'python3 csvread.py '
    
    os.system(ein)

  
button1 = tk.Button(text='      run    ', command=firstFile, bg='gold4', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=button1)



mpb = ttk.Progressbar(root,orient ="horizontal",length = 200, mode ="determinate")
mpb.pack()
mpb["maximum"] = 100
mpb["value"] = 50


root.mainloop()
