import tkinter as tk
from tkinter import messagebox
from db import Database

# Instance database object

db = Database('store.db')

# main class of the application

class Application(tk.Frame):
    # do something
    def __init__(self, master):
        self.master = master



root = tk.Tk()
app = Application(master=root)
app.mainloop()