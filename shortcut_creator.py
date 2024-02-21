import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
import os

def quit():
    root.destroy()

def click_ok():
    messagebox.showinfo(message="Shortcut Created")
    file = open(filenametext.get(), "w")
    file.write("[Desktop Entry]\n")
    file.write("Name=" + nametext.get() + "\n")
    file.write("Exec=" + exectext.get() + "\n")
    file.write("Icon=" + icontext.get() + "\n")

    file.close()
    root.destroy()

def choose_file():
    exectext.delete(0, tk.END)
    exectext.insert(0, fd.askopenfilename())

def choose_filename():
    filenametext.delete(0, tk.END)
    filenametext.insert(0, fd.askdirectory())

def choose_icon():
    icontext.delete(0, tk.END)
    icontext.insert(0, fd.askopenfilename())

root = tk.Tk()
root.title("Create Desktop Shortcut")

titleframe = tk.Frame(root)
titleframe.columnconfigure(0, weight=1)
titleframe.columnconfigure(1, weight=1)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

filenamelabel = tk.Label(frame, text = "Filename:")
filenametext = tk.Entry(frame, width = 40)
filenametext.insert(0, os.getcwd() + "/untitled.desktop")

choose_filename_button = tk.Button(frame, text = "Choose",
        command = choose_filename)

namelabel = tk.Label(titleframe, text = "Title:")
nametext = tk.Entry(titleframe, width=40)
nametext.insert(0, "Untitled")

iconlabel = tk.Label(frame, text = "Icon:")
icontext = tk.Entry(frame, width=40)

choose_icon_button = tk.Button(frame, text="Choose", command =
        choose_icon)

choosebutton = tk.Button(frame, text="Choose", command = choose_file)

execlabel = tk.Label(frame, text = "Execute:")
exectext = tk.Entry(frame, width = 40)
exectext.insert(0, "Path to Executable")

okbutton = tk.Button(buttonframe, text="Ok", command = click_ok)
cancelbutton = tk.Button(buttonframe, text="Cancel", command = quit)

namelabel.grid(row=0, column=0)
nametext.grid(row=0, column=1)



filenamelabel.grid(row=0, column=0)
filenametext.grid(row=0, column=1)
choose_filename_button.grid(row=0, column=2)
execlabel.grid(row=1, column=0)
exectext.grid(row=1, column=1)
choosebutton.grid(row=1, column=2)
iconlabel.grid(row=2, column=0)
icontext.grid(row=2, column=1)
choose_icon_button.grid(row=2, column=2)

okbutton.grid(row=0, column=0)
cancelbutton.grid(row=0, column=1)

titleframe.pack()
frame.pack(fill="x")
buttonframe.pack()


root.mainloop()
