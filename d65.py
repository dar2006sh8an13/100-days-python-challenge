#tkinter window
#Goal:create a basic window
import tkinter as tk
root=tk.Tk()
root.title("python GUI")
root.geometry("300x200")

Label = tk.Label(root,text="welcome to tkinter!")
Label.pack()

root.mainloop()