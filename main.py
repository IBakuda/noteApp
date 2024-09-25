from tkinter.filedialog import *
import tkinter as tk
from message import Message
from tkinter import ttk


# todo:добавить дату модификации заметки добавить категории
# todo:добавить категории
# todo: реализовать механизм модификации заметок
#
#


# def openFile():
#     file = askopenfile(mode='r', filetypes=[('text files', '.txt')])
#     if file is not None:
#         content = file.read()
#     entry.insert(tk.INSERT, content)


# def saveFile():
#     new_file = asksaveasfile(mode='w', filetypes=[('text files', '.txt')])
#     if new_file is None:
#         return
#     text = str(entry.get(1.0, tk.END))
#     new_file.write(text)
#     new_file.close()


def clearFile():
    entry.delete(1.0, tk.END)
    date["text"] = None


def openFile():
    a = Message()
    a.load()


def saveFile():
    a = Message()
    text = str(entry.get(1.0, tk.END))
    titl = str(tit.get())
    a.add_message(titl, text)
    a.load()


def addNote():
    a = Message()
    text = str(entry.get(1.0, tk.END))
    titl = str(tit.get())
    a.add_message(titl, text)
    saveFile()
    a.load()


def showNote():
    entry.delete(1.0, tk.END)
    selection = selected()
    a = Message()
    data = a.get_message(str(selection))
    if data == None:
        entry.insert(tk.INSERT, 'no')
        return
    tex = data['text']
    dat = data['creatingDate']

    date['text'] = dat
    entry.insert(tk.INSERT, tex)
    print(tex)


def getNotes():
    openFile()
    a = Message()
    notes = a.get_messages()
    key = list(notes.keys())
    return key


def selected():
    selection = combobox.get()
    return selection


def deleteNote():
    selection = selected()
    a = Message()
    a.remove_message(selection)


def update():
    a = Message()
    notes = a.get_messages()
    keys = list(notes.keys())


def update_combobox(new_data, add_single_item=False):
    a = Message()
    notes = a.get_messages()
    keys = list(notes.keys())


canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="white")
top = tk.Frame(canvas)

top.pack(padx=10, pady=5, anchor='nw')

combobox = ttk.Combobox(value=getNotes())
combobox.pack(anchor='nw', padx=6, pady=6)

tit = tk.Entry(canvas)
tit.pack(anchor='nw', padx=8, pady=8)

date = tk.Label()
date.pack(anchor='nw', padx=8, pady=8)

b1 = tk.Button(canvas, text="open", bg="white", command=openFile)
b1.pack(in_=top, side=tk.LEFT)

b2 = tk.Button(canvas, text="save", bg="white", command=saveFile)
b2.pack(in_=top, side=tk.LEFT)

b3 = tk.Button(canvas, text="clear", bg="white", command=clearFile)
b3.pack(in_=top, side=tk.LEFT)

b4 = tk.Button(canvas, text="exit", bg="white", command=exit)
b4.pack(in_=top, side=tk.LEFT)

b4 = tk.Button(canvas, text="add", bg="white", command=addNote)
b4.pack(in_=top, side=tk.LEFT)

b4 = tk.Button(canvas, text="show", bg="white", command=showNote)
b4.pack(in_=top, side=tk.LEFT)

b4 = tk.Button(canvas, text="del", bg="white", command=deleteNote)
b4.pack(in_=top, side=tk.LEFT)

entry = tk.Text(canvas, wrap=tk.WORD, bg="#F9DDA4", font=("poppins", 15))
entry.pack(padx=10, pady=5, expand=True, fill=tk.BOTH)

canvas.mainloop()
