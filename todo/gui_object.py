from tkinter import *
from tkinter import simpledialog
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
import os
import datetime
import subprocess


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

        self["font"] = ("メイリオ", 11)
        self["width"] = 50
        self["padx"] = 10
        self["pady"] = 20
        self["bg"] = "blue"
        self["fg"] = "white"


class Button(tk.Button):
    def __init__(self, master=None):
        tk.Button.__init__(self, master)

        self["height"] = 1
        self["width"] = 10
        self["font"] = ("メイリオ", 15)


class RefreshButton(Button):
    def __init__(self, master=None,):
        Button.__init__(self, master)


class Combobox(ttk.Combobox):
    def __init__(self, master=None):
        ttk.Combobox.__init__(self, master)

        self["font"] = ("メイリオ", 20)


class Text(scrolledtext.ScrolledText):
    def __init__(self, master=None):
        scrolledtext.ScrolledText.__init__(self, master)
        self["width"] = 50
        self["height"] = 20
        self["font"] = ("メイリオ", 12)


class Entry(ttk.Entry):
    def __init__(self, master=None):
        ttk.Entry.__init__(self, master)

        self["font"] = ("メイリオ", 11)
        self["width"] = 25


class TextForDisplayDetail(Text):
    def __init__(self, master=None):
        Text.__init__(self, master)

        self.tag_config('system_message_file_path', background="white", foreground="blue", underline=1)
        self.tag_config('system_message_folder_path', background="white", foreground="blue", underline=1)


class Listbox(tk.Listbox):
    def __init__(self, master=None, master_of_detail_text=None):
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)
        tk.Listbox.__init__(self, master, yscrollcommand=scrollbar.set, selectmode=EXTENDED)

        self.pack(side=LEFT, fill=BOTH)
        self["width"] = 50
        self["height"] = 20
        self["font"] = ("メイリオ", 12)
        self.master = master
        self.master_of_detail_text = master_of_detail_text
        self.text = TextForDisplayDetail(self.master_of_detail_text)
        self.date_label = Label(self.master_of_detail_text)

        scrollbar["command"] = self.yview
        self.bind("<Button-1>", self.show_detail)
        self.bind("<Return>", self.show_detail)

        self.todo_list = {}

    def show_detail(self, event=None):

        if str(event.type) == "ButtonPress":
            self.activate_line_clicked(event=event)

        self.text.destroy()

        self.text = TextForDisplayDetail(self.master_of_detail_text)
        self.text.tag_bind("system_message_file_path", "<Double-Button-1>", self.open_with_another_app)
        self.text.tag_bind("system_message_folder_path", "<Double-Button-1>", self.open_folder)
        create_time, update_time = self.get_timestamp_of_path(self.todo_list[self.index(ACTIVE)])
        self.text.insert(END, "ファイルを開く", "system_message_file_path")
        self.text.insert(END, "\t\t")
        self.text.insert(END, "フォルダを開く", "system_message_folder_path")
        self.text.insert(END, "\n\n")
        self.text.insert(END, self.read_detail_of_todo(self.index(ACTIVE)))
        self.text.insert(END, "\n\n======メタデータ======\n\n")
        self.text.insert(END, "作成 {0} 更新 {1}".format(create_time, update_time))
        self.text.insert(END, "\n")
        self.text.insert(END, self.todo_list[self.index(ACTIVE)])
        self.text.grid(column=0, row=1, columnspan=3)

    def set_todo_list(self, todo_list_dict):
        self.todo_list = todo_list_dict

    def get_todo_list(self):
        return self.todo_list

    def read_detail_of_todo(self, index):
        path = self.todo_list[index]
        with open(path, encoding="utf_8") as f:
            return f.read()

    def get_timestamp_of_path(self, path):
        stat_result = os.stat(path)
        create_time = datetime.datetime.fromtimestamp(stat_result.st_ctime).strftime("%Y/%m/%d %H:%M:%S")
        update_time = datetime.datetime.fromtimestamp(stat_result.st_mtime).strftime("%Y/%m/%d %H:%M:%S")

        return create_time, update_time

    def get_path_of_active_todo(self):
        return self.todo_list[self.index(ACTIVE)]

    def open_with_another_app(self, event=None):
        path = self.get_todo_list()[self.index(ACTIVE)]
        os.system("start " + path)

    def open_folder(self, event=None):
        path = "\\".join(self.get_todo_list()[self.index(ACTIVE)].split("\\")[:-1])
        subprocess.run("explorer {0}".format(path))

    # 選択された行をactive状態にするメソッド
    # シングルクリックの場合にactive状態へ遷移させるために実装した
    def activate_line_clicked(self, event=None):
        self.selection_clear(0, tk.END)
        self.selection_set(self.nearest(event.y))
        self.activate(self.nearest(event.y))


class DialogForAddTodo(simpledialog.Dialog):
    def __init__(self, master, items_for_combobox, title=None) -> None:
        self.items_for_combobox: dict = items_for_combobox
        simpledialog.Dialog.__init__(self, parent=master)

    def body(self, master) -> None:
        """
        Dialogオブジェクトへ配置するオブジェクトを定義する。
        Todoを追加するためにユーザーが入力する情報を受け取るための、GUIオブジェクトを作成している。

        Parameters
        ----------
        master:
            Dialogオブジェクトの親オブジェクト

        Returns
        -------
        None
        """

        discription_combobox_label: Label = Label(master)
        discription_combobox_label["text"] = "カテゴリを選択"
        discription_combobox_label["width"] = 25
        discription_combobox_label["fg"] = "black"
        discription_combobox_label["bg"] = "white"
        discription_combobox_label.grid(column=0, row=0)

        self.category: Combobox = Combobox(master)
        self.category["font"] = ("メイリオ", 11)
        self.category["value"] = list(self.items_for_combobox.keys())
        self.category.grid(column=1, row=0)

        discription_entry_label: Label = Label(master)
        discription_entry_label["text"] = "追加するTODO名を入力"
        discription_entry_label["width"] = 25
        discription_entry_label["fg"] = "black"
        discription_entry_label["bg"] = "white"
        discription_entry_label.grid(column=0, row=1)

        self.todo_name: Entry = Entry(master)
        self.todo_name.grid(column=1, row=1)

    def apply(self):
        """
        このDialogオブジェクトが破棄される際に実行される処理を定義する。
        ユーザーが入力した情報をもとに、TODOファイルを指定されたディレクトリへ作成する。

        Parameters
        ----------

        Returns
        -------
        None
        """
        # todoという文字列が入っていないと、GUI上に表示されないため追加している。
        todo_file_name: str = "[todo]" + self.todo_name.get() + ".txt"
        with open(os.path.join(self.items_for_combobox[self.category.get()], todo_file_name), "w") as f:
            pass

