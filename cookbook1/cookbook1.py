# -*- coding: utf-8 -*-
#python3からはtkinter
#python2で実行したい場合は、Tkinter
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import datetime
#from Tk_Guid_graph import graph

##############################################################################
#ノートブック
class Use_NoteBook(ttk.Notebook):
    """Textを管理するのNoteBookウィジェット."""
 
    def __init__(self, master=None):
        ttk.Notebook.__init__(self, master)

    def change_tab(self, event=None):
        pass
        
##############################################################################
#フレーム
class Use_Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(column=0, row=0)
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
#        self["command"] = self.Insert

"""
    def Insert(self, event=None):
        entry_date = Entry_date.get()
        entry_cash = Entry_cash.get()

        Val_Radio = str(val.get() + 1)

        List_display.insert(END, "  ".join([entry_date, Dict_item[Val_Radio], entry_cash]))

        detail_dic["date"].append(entry_date)

        for i in range(4):
            if str(i + 1) == Val_Radio:
                detail_dic[str(i + 1)].append(entry_cash)
            else:
                detail_dic[str(i + 1)].append(0)        
    
    def Send(self, event=None):

        self.insert_num = len(detail_dic["date"])
        
        File = open("data_file.txt", "a")
        
        for i in range(self.insert_num):
            Y, M, D = detail_dic["date"][i].split("/") 
            
            File.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n"\
                       .format(Y, M, D,\
                               detail_dic["1"][i],\
                               detail_dic["2"][i],\
                               detail_dic["3"][i],\
                               detail_dic["4"][i]
                       )
            )
            
        File.close()

        List_display.delete(END)

        #コンボボックスのvaluesを更新
        cbox.Set_values()

    def Delete(self, event=None):
        index = List_display.index(ANCHOR)
        List_display.delete(ANCHOR)

        detail_dic["date"].pop(index)

        for i in range(4):
            detail_dic[str(i + 1)].pop(index)

    def Graph(self, event=None):
        date = cbox.get()
        graph(date)

        image = tk.PhotoImage(file = "./graph.png")
        Label_Display["image"] = image

        #.photo = すると関数を呼び出したときに画像を再度表示してくれる。
        #何故かは不明だが、うまくいくのでこれで
        Label_Display.photo = image
"""        
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
#コンボボックス
class Use_Combobox(ttk.Combobox):
    def __init__(self, master=None):
        ttk.Combobox.__init__(self, master)

        self["font"] = ("Helvetica", 20)

    def Set_values(self):
        data = np.loadtxt("data_file.txt", dtype=int, delimiter="\t")

        Year = data[:, 0] * 100
        Month = data[:, 1]

        #arrat >>> set (重複削除) >>> list
        Y_M = list(set(Year + Month))
        
        self["values"] = Y_M
        
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

#不明だがtab_id=0にnewタブが作成されてしまうので削除する
#note.forget(0)

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

detail_dic = {"date" : [], "1" : [], "2" : [], "3" : [], "4" : []}

val = IntVar()
val.set(1)

for i in range(len(Dict_item)):
    Radio = Use_Radio(Frame_item)
    Radio.grid(column=0, row=i + 1)
    Radio["text"] = Dict_item[str(i + 1)]
    Radio["value"] = i
    Radio["variable"] = val
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
#Frame_Listbox(entryの取得、表示)
#値の取得

Frame_Listbox = Use_Frame(Main_right)
Frame_Listbox.grid(column=0, row=0)

scrollbar = Scrollbar(Frame_Listbox)
scrollbar.pack(side = RIGHT, fill = Y)

List_display = Listbox(Frame_Listbox, yscrollcommand = scrollbar.set, selectmode=EXTENDED)
List_display.pack(side = LEFT, fill = BOTH)
List_display["width"] = 30
List_display["height"] = 10
List_display["font"] = ("Helvetica", 20)

scrollbar["command"] = List_display.yview

Button_display = Use_Button(Main_left)
Button_display.grid(column=0, row=3)
Button_display["text"] = "送信"
#Button_display["command"] = Button_display.Insert
Button_display["fg"] = "white"
Button_display["bg"] = "blue"
#****************************************************************************#
#Frame_Fix
#確定

Frame_Fix = Use_Frame(Main_right)
Frame_Fix.grid(column=0, row=1)

Button_Fix = Use_Button(Frame_Fix)
Button_Fix.grid(column=0, row=0)
#Button_Fix["command"] = Button_Fix.Send
Button_Fix["text"] = "確定"

Button_Clear = Use_Button(Frame_Fix)
Button_Clear.grid(column=1, row=0)
#Button_Clear["command"] = Button_Clear.Delete
Button_Clear["text"] = "クリア"

#****************************************************************************#
#key-bind
root.bind("<Control-KeyPress-n>", note.change_tab)
#root.bind("<Return>", Button_Fix.Insert)

Entry_cash.focus_set()

#############################################################################
#グラフの描画
Graph = Use_Frame(note)
Graph.grid(column=0, row=0)
note.add(Graph, text="グラフ")

cbox = Use_Combobox(Graph)
cbox.grid(column=0, row=0)
cbox.Set_values()

"""
Button_Display = Use_Button(Graph)
Button_Display.grid(column=1, row=0)
Button_Display["text"] = "描画"
Button_Display["command"] = Button_Display.Graph

Label_Display = Use_Label(Graph)
Label_Display.grid(column=0, row=1, columnspan=2)
image = tk.PhotoImage(file = "./graph.png")
Label_Display["image"] = image
Label_Display["width"] = 500
Label_Display["height"] = 500
"""

root.mainloop()
