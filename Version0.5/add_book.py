import tkinter as tk
from tkinter import Tk, Frame, Button, Label, ttk, Entry
from PIL import Image, ImageTk 
from tkinter import ttk
import math
import os
import Version0_5

PathOfFile = os.path.abspath(__file__)
PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")

def add_book(root, Root):

    def show_frame(frame):
        frame.tkraise()

    frame_add = Frame(root)
    frame_add.grid(row=0, column=0, sticky='nsew')
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)  

    show_frame(frame_add)

    def khosach():
        Version0_5.quanlykhosach(Root)
        return

    def on_label_click(event):
        event.widget.focus_set()
        print("Label was clicked!")

    window_width = 1050; window_height = 570
    
    def Xuly_Anh(imageOfpath, size_width, size_height):
        original_image = Image.open(imageOfpath)
        image = original_image.resize((size_width, size_height), resample=Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    ig_ThemSach = Xuly_Anh(PathOfFile + "/Image/" +'bgThemSach.png', window_width, window_height)
    bg_ThemSach = Label(root, image = ig_ThemSach, borderwidth=0, highlightthickness=0); bg_ThemSach.place(x = 0, y = 0)
    bg_ThemSach.bind("<Button-1>", on_label_click)

    ## Các hàm để tạo Dòng chữ mờ tại Entry  - placeholder
    def set_placeholder(entry, placeholder_text):
        entry.insert(0, placeholder_text); entry.config(fg='grey')

    def on_entry_click(event, entry, placeholder_text):
        if entry.get() == placeholder_text:
            entry.delete(0, "end"); entry.config(fg='black')

    def on_focusout(event, entry, placeholder_text):
        if entry.get() == "":
            entry.insert(0, placeholder_text); entry.config(fg='grey')

    def apply_placeholder(entry, placeholder_text):
        # Áp dụng placeholder cho một Entry.
        set_placeholder(entry, placeholder_text) 
        entry.bind("<FocusIn>", lambda event: on_entry_click(event, entry, placeholder_text))
        entry.bind("<FocusOut>", lambda event: on_focusout(event, entry, placeholder_text))
        
    # Các label cho thông tin sách bên trái
    labels_left = ['Mã sách', 'Tên sách', 'Thể loại', 'Tác giả']
    entries_left = []

    for i, label in enumerate(labels_left):
        label_widget = Label(frame_left, text=label, font=('Arial', 15))
        label_widget.grid(row=i, column=0, pady=20, padx=20)

        entry = Entry(frame_left, font=('Arial', 15), width=25)
        entry.grid(row=i, column=1, pady=20, padx=20)
        entries_left.append(entry)

    # Các label cho thông tin sách bên phải
    labels_right = ['Nhà xuất bản', 'Ngày sản xuất', 'Số lượng', 'Giá']
    entries_right = []

    for i, label in enumerate(labels_right):
        label_widget = Label(frame_right, text=label, font=('Arial', 15))
        label_widget.grid(row=i, column=0, pady=20, padx=20)

        entry = Entry(frame_right, font=('Arial', 15), width=25)
        entry.grid(row=i, column=1, pady=20, padx=20)
        entries_right.append(entry)

    # Nút Thêm sách và Hủy
    button_add_book = Button(frame_add, text='Thêm sách', bg='green', fg='white', font=('Arial', 20))
    button_add_book.grid(row=2, column=0, pady=10, padx=20)

    button_back = Button(frame_add, text='Hủy', bg='red', fg='white', font=('Arial', 20), command = lambda : khosach() )
    button_back.grid(row=2, column=1, pady=10, padx=20)

    root.update_idletasks()
    root.mainloop()