from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


# Create window object
app = Tk()

# Wish List
list_text = StringVar()
list_label = Label(app, text='List Name', font=('bold', 14), pady=20)
list_label.grid(row=0, column=0, sticky=W)
list_entry = Entry(app, textvariable=list_text)
list_entry.grid(row=0, column=1)
# brand_name
brand_name_text = StringVar()
brand_name_label = Label(app, text='Brand Name', font=('bold', 14))
brand_name_label.grid(row=0, column=2, sticky=W)
brand_name_entry = Entry(app, textvariable=brand_name_text)
brand_name_entry.grid(row=0, column=3)
# Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('bold', 14))
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)
# Price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# wish list (Lightbox)
wish_list = Listbox(app, height=8, width=50, border=0)
wish_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Set scroll to listbox
wish_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=wish_list.yview)
# Bind select
