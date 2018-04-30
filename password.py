# -*- coding: utf-8 -*-
import random
from tkinter import *
from tkinter import filedialog
import os, ctypes

dict = (
'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '<', '>', '#',
'@', '$', '&', '-',
'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F',
'G', 'H', 'J', 'K', 'L'
, 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=', '!', '№', ';', '%', ':',
'?', '*', '\\', '+')

dict_digit = (
'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=', '!', '№', ';', '%', ':', '?', '*', '\\', '+', '[', ']',
';', '<', '>', '#', '@', '$', '&', '-', ',', '.', '/')

dict_latin = (
'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'Q', 'W', 'E', 'R', 'T', 'Y',
'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'
, 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'z', 'x', 'c', 'v', 'b', 'n', 'm')

dict_latin_digit = (
'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'Q', 'W', 'E', 'R', 'T', 'Y',
'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'
, 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9',
'0')

password = ''

def close_win():
    root.destroy()

def proverka(event):
    l = entry_input.get()
    metod = var.get()

    try:
        if metod == 1:
            tmp = 0
            global pasword
            pasword = []

            while tmp < int(l):
                choice = random.choice(dict)
                pasword.append(choice)
                tmp += 1

            out = ''.join(pasword)
            Label_output["text"] = out
            return pasword

        if metod == 2:
            tmp = 0
            pasword = []

            while tmp < int(l):
                choice = random.choice(dict_digit)
                pasword.append(choice)
                tmp += 1

            out = ''.join(pasword)
            Label_output["text"] = out
            return pasword

        if metod == 3:
            tmp = 0
            pasword = []

            while tmp < int(l):
                choice = random.choice(dict_latin_digit)
                pasword.append(choice)
                tmp += 1

            out = ''.join(pasword)
            Label_output["text"] = out
            return pasword

    except:
        Label_output["text"] = "Input length password "


def file_save():
    try:
        pasword_save = 'Your password :  ' + ''.join(pasword)
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        file.write(pasword_save)
        file.close()
    except:
        Label_output["text"] = "Run as Admin"


root = Tk()
root.title("Generator of passwords")
var = IntVar()

m = Menu(root)
root.config(menu=m)
fm = Menu(m, tearoff=0)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Save...", command=file_save)
fm.add_command(label="Exit", command=close_win)

Label_input = Label(root, text='Length password ')
Label_input.grid(column=0, row=0, sticky='w')

Label_out = Label(root, text='Your password : ')
Label_out.grid(column=0, row=1, sticky='w')

entry_input = Entry(root, width=5)
entry_input.grid(column=1, row=0, sticky='w')

Button_input = Button(root, text='Ok')
Button_input.grid(column=2, row=0)
Button_input.bind("<Button-1>", proverka)

Frame_output = Frame(root, bg='red', bd=0.5)
Frame_output.grid(column=1, row=1, sticky='w')
Label_output = Label(Frame_output, width=20, bg="white")
Label_output.grid(column=3, row=1, sticky='w')

rbutton1 = Radiobutton(root, text='Use all signs', variable=var, value=1)
rbutton1.grid(column=0, row=2, sticky='w')
rbutton2 = Radiobutton(root, text='Use digits and signs', variable=var, value=2)
rbutton2.grid(column=0, row=3, sticky='w')
rbutton3 = Radiobutton(root, text='Use digits and letters', variable=var, value=3)
rbutton3.grid(column=0, row=4, sticky='w')

try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    if is_admin == 0:
        Label_output["text"] = "Run as Admin"

root.mainloop()
