from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext


class Text(scrolledtext.ScrolledText):
    def __init__(self, master=None):
        scrolledtext.ScrolledText.__init__(self, master)
        self.master = master
        self["width"] = 100
        self["height"] = 10
        self["font"] = ("メイリオ", 12)
        self.tag_bind("link", "<Double-Button-1>", self.open_text)

    def open_text(self, event=None):
        text = Text(master=self.master)
        text.insert(tk.END, "test")
        text.grid(column=1, row=1)


if __name__ == "__main__":
    root = tk.Tk()
    text = Text(root)
    text.insert(tk.END, "linkです", "link")
    text.grid(column=1, row=1)
    root.mainloop()
