import tkinter as tk

root = tk.Tk()

l1 = tk.Label(root)
l1.grid(column=0, row=0)
l1["width"] = 10
l1["height"] = 10
l1["bg"] = "red"
l1["padx"] = 100

l2 = tk.Label(root)
l2.grid(column=1, row=0)
l2["width"] = 10
l2["height"] = 10
l2["bg"] = "blue"

root.mainloop()
