import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk 
import os
import Version0_5
import connectSQL
from placeholder import apply_placeholder

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

    window_width = 1050; window_height = 570
    
    def Xuly_Anh(imageOfpath, size_width, size_height):
        original_image = Image.open(imageOfpath)
        image = original_image.resize((size_width, size_height), resample=Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    ig_bg_ThemSach = Xuly_Anh(PathOfFile + "/Image/" +'bgThemSach.png', window_width, window_height)
    bg_ThemSach = Label(root, image = ig_bg_ThemSach, borderwidth=0, highlightthickness=0); bg_ThemSach.place(x = 0, y = 0)
    bg_ThemSach.bind("<Button-1>", on_label_click)

    # Các label cho thông tin sách bên trái
    labels_left = ['Mã sách', 'Tên sách', 'Thể loại', 'Tác giả']
    entries_left = []

    for i, label_text in enumerate(labels_left):
        entry = Entry(root, width=24, font=('Arial', 14), fg='black', border = 0, bg = '#d1e6fa')
        entry.place(x=180, y=202 + i * 76)
        
        apply_placeholder(entry, f'Nhập {label_text.lower()}')
        entries_left.append(entry)

    # Các label cho thông tin sách bên phải
    labels_right = ['Nhà xuất bản', 'Ngày sản xuất', 'Số lượng', 'Giá']
    entries_right = []

    for i, label_text in enumerate(labels_right):
        entry = Entry(root, width=24, font=('Arial', 14), fg='black', border = 0, bg = '#d1e6fa' )
        entry.place(x=610, y=202 + i * 76)
        
        apply_placeholder(entry, f'Nhập {label_text.lower()}')
        entries_right.append(entry)

    def ThemSach():
       connectSQL.Insert_sach(entries_left[0].get(), entries_left[1].get(), entries_left[2].get(), entries_left[3].get(), entries_right[0].get(), entries_right[1].get(), entries_right[2].get(), entries_right[3].get())
       Version0_5.quanlykhosach(root)
    # Nút Thêm sách và Hủy

    ig_Button_ThemSach = Xuly_Anh(PathOfFile + "/Image/" +'button_Save.png', 57, 57)
    button_Save = Button(root, image = ig_Button_ThemSach, borderwidth=0, highlightthickness=0, command = lambda : ThemSach()); 
    button_Save.place(x = 552, y = 485)

    ig_Button_QuayLai = Xuly_Anh(PathOfFile + "/Image/" +'button_Back.png', 57, 57)
    button_Back = Button(root, image = ig_Button_QuayLai, borderwidth=0, highlightthickness=0, command = lambda : khosach()); 
    button_Back.place(x = 443, y = 487)



    root.update_idletasks()
    root.mainloop()