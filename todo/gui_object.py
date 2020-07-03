from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk


class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(column=0, row=0)
        self["width"] = 600
        self["height"] = 600
        self["padx"] = 20
        self["pady"] = 20


class Label(tk.Label):
    def __init__(self, master=None):
        tk.Label.__init__(self, master)

        self["font"] = ("Helvetica", 11)
        self["width"] = 50
        self["anchor"] = "e"
        self["padx"] = 10
        self["pady"] = 10

