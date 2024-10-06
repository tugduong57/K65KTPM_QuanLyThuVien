from tkinter import *
from tkinter import messagebox
import os
import Version0_5
from PIL import Image, ImageTk 
import sign_up

def sign_in(root):

    def mouse_index(event):
        x, y = event.x, event.y
        print(f"Vị trí chuột: x={x}, y={y}")
    root.bind("<Button-1>", mouse_index)

    def on_label_click(event):
        event.widget.focus_set()
        print("Label was clicked!")

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

    # Tạo frame đăng nhập
    frame_sign_in = Frame(root)
    frame_sign_in.grid(row=0, column=0, sticky="nsew")

    show_frame(frame_sign_in)

    # Thêm hình nền
    img_bgLogIn = Xuly_Anh(PathOfFile + "/Image/" + 'bgLogIn.png', window_width, window_height)
    label_LogIn = Label(frame_sign_in, image = img_bgLogIn, borderwidth = 0, highlightthickness = 0); label_LogIn.place(x = 0, y = 0)
    label_LogIn.bind("<Button-1>", on_label_click)
    
    # Check đăng nhập
    def login_user():
        username = user.get()
        password_input = password.get()

        # Đọc database
        with open(PathOfFile + '/Image/users.txt', 'r') as file:
            users = file.readlines()
            for line in users:
                stored_user, stored_password = line.strip().split(',')
                print(f"User: {stored_user}, Password: {stored_password}")
                if stored_user == username and stored_password == password_input:
                    print("Login successful")
                    Version0_5.quanlykhosach(root)
                    return
            messagebox.showerror("Error", "Invalid username or password")

    def signup_user():
        sign_up.sign_up(root);
        return

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

    user.bind('<Return>', lambda _: login_user())
    password.bind('<Return>', lambda _: login_user())

    def on_enter(event):
        event.widget.config(cursor='hand2')     # Thay đổi kiểu con trỏ khi chuột vào label

    def on_leave(event):
        event.widget.config(cursor='')          # Khôi phụckiểu con trỏ khi chuột ra khỏi label

    # Nút đăng nhập
    login = Button(frame_sign_in, text='Đăng nhập', width=15, bg = '#145da0', fg = 'white', 
                    font =("Poppins", 15), border=0, command=lambda: login_user())
    login.place(x=420, y=315)

    # Nút đăng kí
    signup = Button(frame_sign_in, text='Đăng ký', width=15, bg = '#145da0', fg = 'white', 
                    font =("Poppins", 15), border=0, command=lambda: signup_user())
    signup.place(x=420, y=366)

    for B in [login, signup]:
        B.bind("<Enter>", on_enter)
        B.bind("<Leave>", on_leave)

    root.update_idletasks()
    root.mainloop()
