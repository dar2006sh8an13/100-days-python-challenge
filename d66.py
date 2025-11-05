#tkinter input form
#take user input and show greetings
import tkinter as tk
def show():
    name = entry.get()
    lbl2.config(text=f"hello,{name}!")

root = tk.Tk()
tk.Label(root,text="enter Name:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root,text="submit",command=show).pack()
lbl2=tk.Label(root,text="")
lbl2.pack()

root.mainloop()