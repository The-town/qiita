from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk


class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(column=0, row=0)
        self["width"] = 100
        self["height"] = 100
        self["padx"] = 20
        self["pady"] = 20


class Label(tk.Label):
    def __init__(self, master=None):
        tk.Label.__init__(self, master)

        self["font"] = ("Helvetica", 11)
        self["width"] = 50
        self["anchor"] = "e"
        self["padx"] = 10
        self["pady"] = 20
        self["highlightcolor"] = "blue"


class Text(tk.Text):
    def __init__(self, master=None):
        tk.Text.__init__(self, master)
        self["width"] = 100
        self["height"] = 10


class Listbox(tk.Listbox):
    def __init__(self, master=None, master_of_detail_text=None):
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)
        tk.Listbox.__init__(self, master, yscrollcommand=scrollbar.set, selectmode=EXTENDED)

        self.pack(side=LEFT, fill=BOTH)
        self["width"] = 100
        self["height"] = 10
        self["font"] = ("Helvetica", 12)
        self.master = master
        self.master_of_detail_text = master_of_detail_text
        self.text = Text(self.master_of_detail_text)

        scrollbar["command"] = self.yview
        self.bind("<Double-Button-1>", self.show_detail)
        self.bind("<Return>", self.show_detail)

        self.todo_list = {}

    def show_detail(self, event=None):
        self.text.destroy()
        self.text = Text(self.master_of_detail_text)
        self.text.insert(END, self.read_detail_of_todo(self.index(ACTIVE)))
        self.text.pack()

    def set_todo_list(self, todo_list_dict):
        self.todo_list = todo_list_dict

    def read_detail_of_todo(self, index):
        path = self.todo_list[index]
        with open(path, encoding="utf_8") as f:
            return f.read()
