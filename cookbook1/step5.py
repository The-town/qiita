from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import datetime
#step5で追加
##############################################################################
#ノートブック
class Use_NoteBook(ttk.Notebook):
    """Textを管理するNoteBookウィジェット"""

    def __init__(self, master=None):
        ttk.Notebook.__init__(self, master)

##############################################################################
#フレーム
class Use_Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self["width"] = 600
        self["height"] = 600
        self["padx"] = 20
        self["pady"] = 20

##############################################################################
#ボタン
class Use_Button(tk.Button):
    def __init__(self, master=None):
        tk.Button.__init__(self, master)

        self["height"] = 2
        self["width"] = 20
        self["font"] = ("Helvetica", 15)
##############################################################################
#ラベル
class Use_Label(tk.Label):
    def __init__(self, master=None):
        tk.Label.__init__(self, master)

        self["font"] = ("Helvetica", 20)
        self["width"] = 10
        self["anchor"] = "e"
        self["padx"] = 10
        self["pady"] = 10

##############################################################################
#エントリー
class Use_Entry(tk.Entry):
    def __init__(self, master=None):
        tk.Entry.__init__(self, master)

        self["font"] = ("Helvetica", 20)
        self["width"] = 10

##############################################################################
#ラジオボタン
class Use_Radio(tk.Radiobutton):
    def __init__(self, master=None):
        tk.Radiobutton.__init__(self, master)

        self["font"] = ("Helvetica", 20)


##############################################################################

root = tk.Tk()
root.title("家計簿")

Main = Use_Frame(root)
Main["width"] = 1200
Main["height"] = 1200
Main.grid(column=0, row=0)

Main_left = Use_Frame(Main)
Main_left.grid(column=0, row=0)

note = Use_NoteBook(Main)
note.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

Main_right = Use_Frame(note)
Main_right.grid(column=0, row=0)
note.add(Main_right, text="送信")


###############################################################################
#****************************************************************************#
#日付の取得
Time = StringVar()
day = datetime.datetime.now()
day = day.strftime("%Y/%m/%d")

#****************************************************************************#
#Frame_date(日付の入力)
#ラベル、エントリーの作成
Frame_date = Use_Frame(Main_left)
Frame_date.grid(column=0, row=0)

Label_date_1 = Use_Label(Frame_date)
Label_date_1.grid(column=0, row=0)
Label_date_1["text"] = "日付の入力"

Entry_date = Use_Entry(Frame_date)
Entry_date.grid(column=1, row=0)
Entry_date.insert(0, day)
#****************************************************************************#
#Frame_item(品目の選択)
#ラジオボタンの作成

Frame_item = Use_Frame(Main_left)
Frame_item.grid(column=0, row=1)

Label_radio = Use_Label(Frame_item)
Label_radio.grid(column=0, row=0)
Label_radio["text"] = "品目を選択"

Dict_item = {"1": "娯楽費　", "2": "食費　　", "3": "交通費　", \
             "4": "日用品費"}

for i in range(len(Dict_item)):
    Radio = Use_Radio(Frame_item)
    Radio.grid(column=0, row=i + 1)
    Radio["text"] = Dict_item[str(i + 1)]

#****************************************************************************#
#Frame_cash(金額入力)

Frame_cash = Use_Frame(Main_left)
Frame_cash.grid(column=0, row=2)

Label_cash = Use_Label(Frame_cash)
Label_cash.grid(column=0, row=0)
Label_cash["text"] = "金額の入力"

Entry_cash = Use_Entry(Frame_cash)
Entry_cash.grid(column=1, row=0)

#****************************************************************************#
Button_display = Use_Button(Main_left)
Button_display.grid(column=0, row=3)
Button_display["text"] = "送信"

root.mainloop()
