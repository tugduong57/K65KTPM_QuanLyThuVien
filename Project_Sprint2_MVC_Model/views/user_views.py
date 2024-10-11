from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
import os
PathOfFile = os.path.abspath(__file__)
PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")

def sign_in(root, login_user, show_signup):
    def on_label_click(event):
        event.widget.focus_set()

    def show_frame(frame):
        frame.tkraise()

    window_width = 1050; window_height = 570
    def Xuly_Anh(imageOfpath, size_width, size_height):
        original_image = Image.open(imageOfpath)
        image = original_image.resize((size_width, size_height), resample=Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    # Tạo frame đăng nhập
    frame_sign_in = Frame(root)
    frame_sign_in.grid(row=0, column=0, sticky="nsew")

    show_frame(frame_sign_in)

    # Thêm hình nền
    img_bgLogIn = Xuly_Anh(PathOfFile + "/Image/" + 'bgLogIn.png', window_width, window_height)
    label_LogIn = Label(frame_sign_in, image = img_bgLogIn, borderwidth = 0, highlightthickness = 0); label_LogIn.place(x = 0, y = 0)
    label_LogIn.bind("<Button-1>", on_label_click)

    ## Các hàm để tạo Dòng chữ mờ tại Entry  - placeholder
    def set_placeholder(entry, placeholder_text):
        entry.insert(0, placeholder_text); entry.config(fg='grey')

    def on_entry_click(event, entry, placeholder_text):
        if entry.get() == placeholder_text:
            entry.delete(0, "end"); entry.config(fg='#145da0')

    def on_focusout(event, entry, placeholder_text):
        if entry.get() == "":
            entry.insert(0, placeholder_text); entry.config(fg='grey')

    def apply_placeholder(entry, placeholder_text):
        # Áp dụng placeholder cho một Entry.
        set_placeholder(entry, placeholder_text) 
        entry.bind("<FocusIn>", lambda event: on_entry_click(event, entry, placeholder_text))
        entry.bind("<FocusOut>", lambda event: on_focusout(event, entry, placeholder_text))

    # Nhập tên người dùng
    user = Entry(frame_sign_in, justify='center', width=19, bg = 'white', fg = '#145da0', font =("Poppins", 17), border=0)
    user.place(x=383, y=198)
    apply_placeholder(user, "Tài khoản")

    # Nhập mật khẩu
    password = Entry(frame_sign_in, justify='center', width = 19, bg = 'white', fg = '#145da0', font =("Poppins", 17), border=0, show = '*')
    password.place(x = 383, y=263)
    apply_placeholder(password, "************")

    user.bind('<Return>', lambda _: login_user(root, user.get(), password.get()))
    password.bind('<Return>', lambda _: login_user(root, user.get(), password.get()))

    def on_enter(event):
        event.widget.config(cursor='hand2')     # Thay đổi kiểu con trỏ khi chuột vào label

    def on_leave(event):
        event.widget.config(cursor='')          # Khôi phụckiểu con trỏ khi chuột ra khỏi label

    # Nút đăng nhập
    login = Button(frame_sign_in, text='Đăng nhập', width=15, bg = '#145da0', fg = 'white', 
                    font =("Poppins", 15), border=0, command=lambda: login_user(root, user.get(), password.get()))
    login.place(x=420, y=315)

    # Nút đăng kí
    signup = Button(frame_sign_in, text='Đăng ký', width=15, bg = '#145da0', fg = 'white', 
                    font =("Poppins", 15), border=0, command=lambda: show_signup(root))
    signup.place(x=420, y=366)

    for B in [login, signup]:
        B.bind("<Enter>", on_enter)
        B.bind("<Leave>", on_leave)

    root.update_idletasks()
    root.mainloop()

def sign_up(root, check_sign_up, start_app):
    def show_frame(frame):
        frame.tkraise()

    PathOfFile = os.path.abspath(__file__)
    PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")

    window_width = 1050; window_height = 570

    def Xuly_Anh(imageOfpath, size_width, size_height):
        original_image = Image.open(imageOfpath)
        image = original_image.resize((size_width, size_height), resample=Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    # Tạo frame kí
    frame_sign_up = Frame(root)
    frame_sign_up.grid(row=0, column=0, sticky="nsew")
    
    # Đảm bảo các hàng và cột của root mở rộng
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    show_frame(frame_sign_up)

    # Thêm hình nền
    img_bgLogIn = Xuly_Anh(PathOfFile + "/Image/" + 'bgSignUp.png', window_width, window_height)
    Label(frame_sign_up, image = img_bgLogIn, borderwidth = 0, highlightthickness = 0).place(x = 0, y = 0)

    ## Các hàm để tạo Dòng chữ mờ tại Entry  - placeholder
    def set_placeholder(entry, placeholder_text):
        entry.insert(0, placeholder_text); entry.config(fg='grey')

    def on_entry_click(event, entry, placeholder_text):
        if entry.get() == placeholder_text:
            entry.delete(0, "end"); entry.config(fg='#145da0')

    def on_focusout(event, entry, placeholder_text):
        if entry.get() == "":
            entry.insert(0, placeholder_text); entry.config(fg='grey')

    def apply_placeholder(entry, placeholder_text):
        # Áp dụng placeholder cho một Entry.
        set_placeholder(entry, placeholder_text) 
        entry.bind("<FocusIn>", lambda event: on_entry_click(event, entry, placeholder_text))
        entry.bind("<FocusOut>", lambda event: on_focusout(event, entry, placeholder_text))

    # Nhập tên người dùng cho đăng kí
    user_signup = Entry(frame_sign_up, justify='center', width=19, bg = 'white', fg = '#145da0', font =("Poppins", 17), border=0)
    user_signup.place(x=383, y=198)
    apply_placeholder(user_signup, "Tài khoản")

    # Nhập mật khẩu cho đăng kí
    password_signup = Entry(frame_sign_up, justify='center', width = 19, bg = 'white', fg = '#145da0', font =("Poppins", 17), border=0, show = '*')
    password_signup.place(x = 383, y=262)
    apply_placeholder(password_signup, "************")

    # Nhập lại mật khẩu cho đăng kí
    password_confirm = Entry(frame_sign_up, justify='center', width = 19, bg = 'white', fg = '#145da0', font =("Poppins", 17), border=0, show = '*')
    password_confirm.place(x = 383, y=323)
    apply_placeholder(password_confirm, "************")

    user_signup.bind('<Return>', lambda _: start_app(root))
    password_signup.bind('<Return>', lambda _: check_sign_up(root,user_signup.get(), password_signup.get(), password_confirm.get()))
    password_confirm.bind('<Return>', lambda _: check_sign_up(root,user_signup.get(), password_signup.get(), password_confirm.get()))

    def on_enter(event):
        event.widget.config(cursor='hand2')     # Thay đổi kiểu con trỏ khi chuột vào label

    def on_leave(event):
        event.widget.config(cursor='')          # Khôi phụckiểu con trỏ khi chuột ra khỏi label


    # Nút đăng kí
    signup = Button(frame_sign_up, text='Đăng ký', width=15, bg = '#145da0', fg = 'white', 
                    font =("Poppins", 15), border=0, command=lambda: check_sign_up(root,user_signup.get(), password_signup.get(), password_confirm.get()))
    signup.place(x=420, y=375)

    # Nút đăng nhập
    login = Button(frame_sign_up, text='Đăng nhập', width=15, bg = '#145da0', fg = 'white', 
                    font =("Poppins", 15), border=0, command=lambda: start_app(root))
    login.place(x=420, y=426)

    for B in [login, signup]:
        B.bind("<Enter>", on_enter)
        B.bind("<Leave>", on_leave)

    root.update_idletasks()
    root.mainloop()