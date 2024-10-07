from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk 
from placeholder import apply_placeholder
import sign_in, connectSQL
import os
PathOfFile = os.path.abspath(__file__)
PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")

def sign_up(root):
    window_width = 1050; window_height = 570

    def Xuly_Anh(imageOfpath, size_width, size_height):
        original_image = Image.open(imageOfpath)
        image = original_image.resize((size_width, size_height), resample=Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    # Tạo frame kí
    frame_sign_up = Frame(root)
    frame_sign_up.grid(row=0, column=0, sticky="nsew")
    frame_sign_up.tkraise()

    # Đảm bảo các hàng và cột của root mở rộng
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Thêm hình nền
    img_bgLogIn = Xuly_Anh(PathOfFile + "/Image/" + 'bgSignUp.png', window_width, window_height)
    Label(frame_sign_up, image = img_bgLogIn, borderwidth = 0, highlightthickness = 0).place(x = 0, y = 0)

    # Label thông báo lỗi
    error_label = Label(frame_sign_up, text='', fg='red', font=("Poppins", 12))
    error_label.place(x=400, y = 500)
    
    placeholder_username = "Tài khoản"
    placeholder_password = "************"
    placeholder_confirm_password = "************"

    # Function to handle signup
    def signup_user():
        username = user_signup.get()
        password_input = password_signup.get()
        confirm_password_input = password_confirm.get()

        # Kiểm tra xem tên người dùng đã được nhập hay chưa
        if username == "" or username == placeholder_username:
            error_label.config(text = 'Người dùng chưa nhập tài khoản!')
            return
        elif password_input == "" or password_input == placeholder_password:
            error_label.config(text="Người dùng chưa nhập mật khẩu!")
            return
        elif confirm_password_input == "" or confirm_password_input == placeholder_confirm_password:
            error_label.config(text = "Người dùng chưa xác nhận mật khẩu!")
            return
        elif password_input != confirm_password_input:
            error_label.config(text = "Mật khẩu và mật khẩu xác nhận chưa giống nhau!")
            return 

        check = connectSQL.check_sign_up(username)

        if not(check): 
            connectSQL.Insert_admin(username, password_input)
            messagebox.showinfo("Sign Up", "Đã tạo tài khoản thành công!")
            sign_in.sign_in(root)
            return
        else:
            error_label.config(text = "Tài khoản đã tồn tại!")
            return

    def login_user():
        sign_in.sign_in(root)
        return

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

    user_signup.bind('<Return>', lambda _: signup_user())
    password_signup.bind('<Return>', lambda _: signup_user())
    password_confirm.bind('<Return>', lambda _: signup_user())

    def on_enter(event):
        event.widget.config(cursor='hand2')     # Thay đổi kiểu con trỏ khi chuột vào label

    def on_leave(event):
        event.widget.config(cursor='')          # Khôi phụckiểu con trỏ khi chuột ra khỏi label


    # Nút đăng kí
    signup = Button(frame_sign_up, text='Đăng ký', width=15, bg = '#145da0', fg = 'white', 
                    font =("Poppins", 15), border=0, command=lambda: signup_user()); signup.place(x=420, y=375)

    # Nút đăng nhập
    login = Button(frame_sign_up, text='Đăng nhập', width=15, bg = '#145da0', fg = 'white', 
                    font =("Poppins", 15), border=0, command=lambda: login_user()); login.place(x=420, y=426)

    for B in [login, signup]:
        B.bind("<Enter>", on_enter)
        B.bind("<Leave>", on_leave)

    root.update_idletasks()
    root.mainloop()