import tkinter as tk
import os
import datetime
from todo import Todo
from gui_object import Frame, Label, Listbox, Text


class TodoDisplay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("todo")

        self.todo_list_frame = Frame(self.root)
        self.todo_list_frame.grid(column=0, row=0)
        self.todo_detail_frame = Frame(self.root)
        self.todo_detail_frame.grid(column=1, row=0)

        self.listbox = Listbox(master=self.todo_list_frame, master_of_detail_text=self.todo_detail_frame)

        self.todo = Todo()
        self.todo_list_box_dict = {}

    def display_todo(self):
        todo_list_box_id = 0
        self.todo_list_box_dict = {}
        paths = self.todo.search_file()

        for key in paths.keys():
            for path in paths[key]:
                create_time, update_time = self.get_timestamp_of_path(path)
                insert_statement = " ".join(["作成", create_time, "更新", update_time, path.split("\\")[-1].split(".")[0]])
                self.listbox.insert(todo_list_box_id, insert_statement)
                self.todo_list_box_dict[todo_list_box_id] = path
                todo_list_box_id = todo_list_box_id + 1

        self.listbox.set_todo_list(self.todo_list_box_dict)

    def get_timestamp_of_path(self, path):
        stat_result = os.stat(path)
        create_time = datetime.datetime.fromtimestamp(stat_result.st_ctime).strftime("%Y/%m/%d %H:%M:%S")
        update_time = datetime.datetime.fromtimestamp(stat_result.st_mtime).strftime("%Y/%m/%d %H:%M:%S")

        return create_time, update_time

    def mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    todo_display = TodoDisplay()
    todo_display.display_todo()
    todo_display.mainloop()