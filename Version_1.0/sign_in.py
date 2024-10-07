from tkinter import *
from tkinter import messagebox
import Version0_5, sign_up, connectSQL
from PIL import Image, ImageTk 
from placeholder import apply_placeholder
import os
PathOfFile = os.path.abspath(__file__)
PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")

def sign_in(root):

    def on_label_click(event):
        event.widget.focus_set()

    window_width = 1050; window_height = 570

    def Xuly_Anh(imageOfpath, size_width, size_height):
        original_image = Image.open(imageOfpath)
        image = original_image.resize((size_width, size_height), resample=Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    # Tạo frame đăng nhập
    frame_sign_in = Frame(root)
    frame_sign_in.grid(row=0, column=0, sticky="nsew")
    frame_sign_in.tkraise()

    # Thêm hình nền
    img_bgLogIn = Xuly_Anh(PathOfFile + "/Image/" + 'bgLogIn.png', window_width, window_height)
    label_LogIn = Label(frame_sign_in, image = img_bgLogIn, borderwidth = 0, highlightthickness = 0); label_LogIn.place(x = 0, y = 0)
    label_LogIn.bind("<Button-1>", on_label_click)
    
    # Label thông báo lỗi
    error_label = Label(frame_sign_in, text='', fg='red', font=("Poppins", 12))
    error_label.place(x=400, y=450)
    
    placeholder_username = "Tài khoản"
    placeholder_password = "************"

    # Check đăng nhập
    def login_user():
        username = user.get()
        password_input = password.get()
        
        # Kiểm tra xem tên người dùng đã được nhập hay chưa
        if username == "" or username == placeholder_username:
            error_label.config(text = 'Người dùng chưa nhập tài khoản!')
            print('1')
            return

        # Kiểm tra nếu mật khẩu là placeholder
        elif password_input == "" or password_input == placeholder_password:
            error_label.config(text="Người dùng chưa nhập mật khẩu!")
            print('2')
            return
            
        check = connectSQL.check_sign_in(username, password_input)
        if check : 
            Version0_5.quanlykhosach(root)
            return
        error_label.config(text = 'Tài khoản hoặc mật khẩu không đúng!')

    def signup_user():
        sign_up.sign_up(root);
        return

    # Nhập tên người dùng
    user = Entry(frame_sign_in, justify='center', width=19, bg = 'white', fg = '#145da0', font =("Poppins", 17), border=0)
    user.place(x=383, y=198)
    apply_placeholder(user, "Tài khoản")

    # Nhập mật khẩu
    password = Entry(frame_sign_in, justify='center', width = 19, bg = 'white', fg = '#145da0', font =("Poppins", 17), border=0, show = '*')
    password.place(x = 383, y=263)
    apply_placeholder(password, "************")

    user.bind('<Return>', lambda _: login_user())
    password.bind('<Return>', lambda _: login_user())

    def on_enter(event):
        event.widget.config(cursor='hand2')     # Thay đổi kiểu con trỏ khi chuột vào label

    def on_leave(event):
        event.widget.config(cursor='')          # Khôi phụckiểu con trỏ khi chuột ra khỏi label

    # Nút đăng nhập
    login = Button(frame_sign_in, text='Đăng nhập', width=15, bg = '#145da0', fg = 'white', 
                    font =("Poppins", 15), border=0, command=lambda: login_user()); login.place(x=420, y=315)

    # Nút đăng kí
    signup = Button(frame_sign_in, text='Đăng ký', width=15, bg = '#145da0', fg = 'white', 
                    font =("Poppins", 15), border=0, command=lambda: signup_user()); signup.place(x=420, y=366)

    for B in [login, signup]:
        B.bind("<Enter>", on_enter)
        B.bind("<Leave>", on_leave)

    root.update_idletasks()
    root.mainloop()