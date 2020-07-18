from tkinter import *
from tkinter import messagebox
import tkinter as tk
from todo import Todo
from gui_object import Frame, Label, Listbox, Text, Button, Combobox
from make_todo_progress_main import get_todo_progress


class TodoDisplay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("todo")

        self.todo = Todo()
        self.todo_list_box_dict = {}

        self.todo_list_frame = Frame(self.root)
        self.todo_list_frame.grid(column=0, row=1)
        self.todo_detail_frame = Frame(self.root)
        self.todo_detail_frame.grid(column=0, row=3)
        self.function_frame = Frame(self.root)
        self.function_frame.grid(column=0, row=0)

        self.listbox = Listbox(master=self.todo_list_frame, master_of_detail_text=self.todo_detail_frame)

        self.start_todo_button = Button(master=self.todo_detail_frame)
        self.start_todo_button["text"] = "開始"
        self.start_todo_button["command"] = self.start_todo
        self.start_todo_button.grid(column=1, row=0)

        self.stop_todo_button = Button(master=self.todo_detail_frame)
        self.stop_todo_button["text"] = "終了"
        self.stop_todo_button["command"] = self.stop_todo
        self.stop_todo_button.grid(column=2, row=0)

        self.refresh_button = Button(master=self.function_frame)
        self.refresh_button.grid(column=2, row=0)
        self.refresh_button["text"] = "更新"
        self.refresh_button["command"] = self.refresh

        self.dir_combbox = Combobox(master=self.function_frame)
        self.dir_combbox.grid(column=1, row=0, padx=(0,100))
        self.set_value_for_dir_combbox()

        self.sort_combbox = Combobox(master=self.function_frame)
        self.sort_combbox.grid(column=0, row=0, padx=(0, 100))
        self.set_value_for_sort_combbox()

    def display_todo(self):
        todo_list_box_id = 0
        self.todo_list_box_dict = {}

        if (self.dir_combbox.get() == "all") or (self.dir_combbox.get() == ""):
            paths = self.todo.search_file()
        else:
            paths = self.todo.limit_search_file(self.dir_combbox.get())

        if self.sort_combbox.get() == "":
            pass
        else:
            paths = self.todo.sort_todo(paths, method=self.sort_combbox.get())

        for path in paths:
            metadata_list = self.todo.search_meta_data(path)
            todo_status = self.todo.get_todo_status(path)
            todo_progress = get_todo_progress(path)
            insert_statement_list = [path.split("\\")[-1].split(".")[0]]
            insert_statement_list.extend(metadata_list)
            insert_statement_list.insert(0, "{0}時間{1}分{2}秒  ".format(
                int(todo_progress) // 3600, int(todo_progress) // 60, int(todo_progress)
            ))
            insert_statement_list.insert(0, "【{0}】".format(todo_status))
            insert_statement = " ".join(insert_statement_list)
            self.listbox.insert(todo_list_box_id, insert_statement)

            importance_color = self.todo.search_importance(path.split("\\")[-1].split(".")[0])
            self.listbox.itemconfig(todo_list_box_id, {'bg': importance_color})

            self.todo_list_box_dict[todo_list_box_id] = path
            todo_list_box_id = todo_list_box_id + 1

        self.listbox.set_todo_list(self.todo_list_box_dict)

    def refresh(self, event=None):
        self.listbox.delete(0, "end")
        self.display_todo()

    def set_value_for_dir_combbox(self):
        self.dir_combbox["value"] = ["all"] + [dir_name.split("\\")[-1] for dir_name in self.todo.get_dir_name_keys()]

    def set_value_for_sort_combbox(self):
        self.sort_combbox["value"] = ["importance", "limit"]

    def start_todo(self, event=None):
        path = self.listbox.get_path_of_active_todo()
        if self.todo.get_todo_status(path) == "stop":
            self.todo.start_todo(path)
            messagebox.showinfo(title="開始" ,message="{0}を開始します。".format(path.split("\\")[-1]))
            self.refresh()
        else:
            messagebox.showerror(title="エラー", message="{0}は既に開始しています。".format(path.split("\\")[-1]))

    def stop_todo(self, event=None):
        path = self.listbox.get_path_of_active_todo()
        if self.todo.get_todo_status(path) == "start":
            self.todo.stop_todo(self.listbox.get_path_of_active_todo())
            messagebox.showinfo(title="終了", message="{0}を終了します。".format(path.split("\\")[-1]))
            self.refresh()
        else:
            messagebox.showerror(title="エラー", message="{0}はまだ開始していません。".format(path.split("\\")[-1]))

    def mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    todo_display = TodoDisplay()
    todo_display.display_todo()
    todo_display.mainloop()