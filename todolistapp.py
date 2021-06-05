from tkinter import *
from tkinter.font import Font  
from tkinter import filedialog
import pickle

root = Tk()
root.geometry("550x455")
root.title("★To ★Do★ List★")

# Functions
def delete_item():
	my_list.delete(ANCHOR)

def add_item():
	my_list.insert(END, my_entry.get())
	my_entry.delete(0, END)

def delete_list():
	my_list.delete(0, END)
 
# Define Font
my_font = Font(
    family='Terminal', 
	size=30,
	weight="bold")

# Creat frame  
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create listbox
my_list = Listbox(my_frame,
	font=my_font,
	width=50,
	height=7,
	bg="SystemButtonFace",
	bd=0,
	fg="#2FBC82",
	highlightthickness=0,
	selectbackground="#F0879D",
	activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

# Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# create entry-box to add items to the list
my_entry = Entry(root, font=("Comic Sans MS", 25), width=26)
my_entry.pack(pady=20)

# Create button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# Add dropdown items
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=delete_list)


# Add some buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)

root.mainloop()