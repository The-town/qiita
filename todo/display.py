import tkinter as tk
from todo import Todo
from gui_object import Frame, Label, Listbox, Text, Button, Combobox


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

        self.refresh_button = Button(master=self.function_frame)
        self.refresh_button.grid(column=1, row=0)
        self.refresh_button["text"] = "更新"
        self.refresh_button["command"] = self.refresh

        self.combbox = Combobox(master=self.function_frame)
        self.combbox.grid(column=0, row=0, padx=(0,100))
        self.set_value_for_combbox()

    def display_todo(self):
        todo_list_box_id = 0
        self.todo_list_box_dict = {}

        if (self.combbox.get() == "all") or (self.combbox.get() == ""):
            paths = self.todo.search_file()
        else:
            paths = self.todo.limit_search_file(self.combbox.get())

        for key in paths.keys():
            for path in paths[key]:
                insert_statement = " ".join([path.split("\\")[-1].split(".")[0]])
                self.listbox.insert(todo_list_box_id, insert_statement)

                importance_color = self.todo.search_importance(path.split("\\")[-1].split(".")[0])
                self.listbox.itemconfig(todo_list_box_id, {'bg': importance_color})

                self.todo_list_box_dict[todo_list_box_id] = path
                todo_list_box_id = todo_list_box_id + 1

        self.listbox.set_todo_list(self.todo_list_box_dict)

    def refresh(self, event=None):
        self.listbox.delete(0, "end")
        self.display_todo()

    def set_value_for_combbox(self):
        self.combbox["value"] = ["all"] + [dir_name.split("\\")[-1] for dir_name in self.todo.get_dir_name_keys()]

    def mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    todo_display = TodoDisplay()
    todo_display.display_todo()
    todo_display.mainloop()