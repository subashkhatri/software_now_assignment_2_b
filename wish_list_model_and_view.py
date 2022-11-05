from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

def populate_list():
    wish_list.delete(0, END)
    for row in db.fetch():
        wish_list.insert(END, row)


def add_item():
    if list_text.get() == '' or brand_name_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(list_text.get(), brand_name_text.get(),
              retailer_text.get(), price_text.get())
    wish_list.delete(0, END)
    wish_list.insert(END, (list_text.get(), brand_name_text.get(),
                            retailer_text.get(), price_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = wish_list.curselection()[0]
        selected_item = wish_list.get(index)

        list_entry.delete(0, END)
        list_entry.insert(END, selected_item[1])
        brand_name_entry.delete(0, END)
        brand_name_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass
def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], list_text.get(), brand_name_text.get(),
              retailer_text.get(), price_text.get())
    populate_list()


def clear_text():
    list_entry.delete(0, END)
    brand_name_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)

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
wish_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Wish list', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Wish list', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Wish list', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Wish list Manager')
app.geometry('700x350')

# Populate data
populate_list()

# Start program
app.mainloop()
