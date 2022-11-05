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
        master.title('Wish list Manager')
        # width and height
        master.geometry('700x350')
        # create widgets/grid
        self.create_widgets() # todo: create widgets method
        # Init selected item variable
        self.selected_item = 0
        # Populate initial list
        self.populate_list() # todo: create populate_list method



root = tk.Tk()
app = Application(master=root)
app.mainloop()