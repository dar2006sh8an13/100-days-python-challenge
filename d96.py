#tkinter expense tracker
import tkinter as tk

total = 0

def add():
    global total
    amt = int(entry.get())
    total += amt
    label2.config(text=f"Total: ₹{total}")

root = tk.Tk()
tk.Label(root, text="Enter Expense:").pack()
entry = tk.Entry(root); entry.pack()
tk.Button(root, text="Add", command=add).pack()
label2 = tk.Label(root, text="Total: ₹0")
label2.pack()

root.mainloop()
