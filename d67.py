#tkinter calculator
#Goal:simple two-number calculator GUI
import  tkinter as tk
def calc():
    a = int(e1.get())
    b = int(e2.get())
    result.config(text=f"sum: {a+b}")
    
root = tk.Tk()
tk.Label(root,text="A").pack()
e1 = tk.Entry(root);e1.pack()

tk.Label(root,text="B").pack()
e2 = tk.Entry(root);e2.pack()

tk.Button(root,text="Add",command=calc).pack()
result=tk.Label(root,text="")
result.pack()

root.mainloop()
    
