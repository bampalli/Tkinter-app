import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Greeting App")
root.geometry("300x200")

def greet():
    name=name_entry.get()
    if name:
        messagebox.showinfo("Greeting",f"Hello,{name}!")
    else:
        messagebox.showwarning("Input Error","Please enter your name")


name_Label=tk.Label(root,text="Enter Your name:")
name_Label.pack(pady=10)


name_entry=tk.Entry(root)
name_entry.pack(pady=10)

greet_button=tk.Button(root,text="Greet",command=greet)
greet_button.pack(pady=10)

root.mainloop()