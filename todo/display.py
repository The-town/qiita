import tkinter as tk
from todo import Todo
from gui_object import Frame, Label


class TodoDisplay:
    def __init__(self):
        self.root = tk.Tk()
        self.label = Label(self.root)
        self.todo = Todo()

    def display_todo(self):
        paths = self.todo.search_file()
        for key in paths.keys():
            for path in paths[key]:
                self.label = Label(self.root)
                self.label["text"] = path.split("\\")[-1].split(".")[0]
                self.label.grid()

    def mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    todo_display = TodoDisplay()
    todo_display.display_todo()
    todo_display.mainloop()