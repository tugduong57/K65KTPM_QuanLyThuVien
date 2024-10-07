import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk 
import os
import Version0_5, connectSQL
from placeholder import apply_placeholder

PathOfFile = os.path.abspath(__file__)
PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")

def edit_book(root, Root, book):

    def on_enter(event):
        event.widget.config(cursor='hand2')  # Thay đổi màu nền và kiểu con trỏ khi chuột vào label

    def on_leave(event):
        event.widget.config(cursor='')  # Khôi phục màu nền và kiểu con trỏ khi chuột ra khỏi label


    print(12, book)
    def show_frame(frame):
        frame.tkraise()

    frame_edit = Frame(root)
    frame_edit.grid(row=0, column=0, sticky='nsew')
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)  

    show_frame(frame_edit)

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

    ig_bg_SuaSach = Xuly_Anh(PathOfFile + "/Image/" +'bgSuaSach.png', window_width, window_height)
    bg_SuaSach = Label(root, image = ig_bg_SuaSach, borderwidth=0, highlightthickness=0); bg_SuaSach.place(x = 0, y = 0)
    bg_SuaSach.bind("<Button-1>", on_label_click)
 
    # Các label cho thông tin sách bên trái
    labels_left = ['Mã sách', 'Tên sách', 'Thể loại', 'Tác giả']
    entries_left = []

    for i, label in enumerate(labels_left):

        entry = Entry(root, width=24, font=('Arial', 14), fg='black', border = 0, bg = '#d1e6fa')
        entry.place(x=180, y=202 + i * 76)
        entry.insert(0, book[0][i])  # Chèn dữ liệu đã có vào Entry
        entries_left.append(entry)    

    # Các label cho thông tin sách bên phải
    labels_right = ['Nhà xuất bản', 'Ngày sản xuất', 'Số lượng', 'Giá']
    entries_right = []

    for i, label in enumerate(labels_left):
        
        entry = Entry(root, width=24, font=('Arial', 14), fg='black', border = 0, bg = '#d1e6fa')
        entry.place(x=610, y=202 + i * 76)
        entry.insert(0, book[0][4+i])  # Chèn dữ liệu đã có vào Entry
        entries_right.append(entry)    

    def sua_sach():
        connectSQL.update_sach(entries_left[0].get(), entries_left[1].get(), entries_left[2].get(), entries_left[3].get(), entries_right[0].get(), entries_right[1].get(), entries_right[2].get(), entries_right[3].get())
        Version0_5.quanlykhosach(root)
    
    # Nút Thêm sách và Hủy

    ig_Button_Save = Xuly_Anh(PathOfFile + "/Image/" +'button_Save.png', 57, 57)
    button_Save = Button(root, image = ig_Button_Save, borderwidth=0, highlightthickness=0, command = lambda : sua_sach()); 
    button_Save.place(x = 552, y = 485)

    ig_Button_Back = Xuly_Anh(PathOfFile + "/Image/" +'button_Back.png', 57, 57)
    button_Back = Button(root, image = ig_Button_Back, borderwidth=0, highlightthickness=0, command = lambda : khosach()); 
    button_Back.place(x = 443, y = 487)

    for N in [button_Save, button_Back]:
        N.bind("<Enter>", on_enter)
        N.bind("<Leave>", on_leave)


    root.update_idletasks()
    root.mainloop()