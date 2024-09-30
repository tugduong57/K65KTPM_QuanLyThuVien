from tkinter import *
import sqlite3
from tkinter import messagebox

def show_frame(frame):
    frame.tkraise()
    
# def login_user():
#     username = user.get()
#     password_input = password.get()
    
#     #kết nối cơ sở dữ liệu
#     conn = sqlite3.connect('library_management.db')
#     c = conn.cursor()
    
#     #kiểm tra tk, mk
#     c.execute('select * from login where user = ? and pass = ?', (username, password_input))
#     user_info = c.fetchall()
    
#     if user_info:
#         print('1')
#         show_frame(frame_sign_up)
#     else:
#         messagebox.showerror('Login failed', 'User or Password not correct')
#     conn.close()
    
    
root = Tk()
root.title("Quản lý thư viện")
icon = "D:\Quan_ly_thu_vien\iconBook.ico"; root.iconbitmap(icon)

show_image = PhotoImage(file = 'D:/Quan_ly_thu_vien/login/show_image.png')
hide_image = PhotoImage(file = 'D:/Quan_ly_thu_vien/login/hide_image.png')

def show():
    hide_button = Button(frame_sign_in, image = hide_image, command= hide, bg = 'white')
    hide_button.place(x = 420, y = 380)
    password.config(show = '')
    
def hide():
    show_button = Button(frame_sign_in, image= show_image, command= show, bg ='white' )
    show_button.place(x = 420, y = 380)
    password.config(show = '*')

# Lấy kích thước màn hình desktop
screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight()

window_width = 1050
window_height = 570

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2) - 25

# Đặt kích thước cửa sổ
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.minsize(700, 500)

# Thêm hình nền
img = PhotoImage(file='D:/Quan_ly_thu_vien/login/background.png')
label_background = Label(root, image=img, bg='white')
label_background.place(x=0, y=0)


# Tạo frame đăng nhập
frame_sign_in = Frame(root, width=600, height=720, bg='white')
frame_sign_in.place(x=500, y=0)

# Tạo frame đăng ký
frame_sign_up = Frame(root, width=600, height=700, bg='white')
frame_sign_up.place(x=500, y=0)

show_button = Button(frame_sign_in, image= show_image, command= show, bg ='white' )
show_button.place(x = 420, y = 380)

# Thêm tiêu đề
Label(frame_sign_in, text='Tlu Library', font=('Microsoft YahHei UI Light', 30), fg='black', bg='white').place(x=150, y=75)
Label(frame_sign_in, text='Login Form', font=('Times New Roman', 23), fg='black', bg='white').place(x=170, y=150)

def on_password_focus_in(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, 'end')
        entry.config(show='*')

def on_password_focus_out(event, entry, placeholder):
    if entry.get() == '':
        entry.config(show='')
        entry.insert(0, placeholder)

def on_entry_focus(event, entry, placeholder):
    entry.delete(0, 'end')

def out_entry_focus(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)

# Nhập tên người dùng
user = Entry(frame_sign_in, width=30, border=0, font=('Microsoft YahHei UI Light', 19))
user.place(x=60, y=300)
user.insert(0, 'User')
user.bind('<FocusIn>', lambda event: on_entry_focus(event, user, 'User'))
user.bind('<FocusOut>', lambda event: out_entry_focus(event, user, 'User'))
Frame(frame_sign_in, width=400, height=2, bg='black').place(x=50, y=330)

# Nhập mật khẩu
password = Entry(frame_sign_in, width=20, border=0, font=('Microsoft YahHei UI Light', 19), show = '*')
password.place(x=60, y=380)
password.insert(0, 'Password')
password.bind('<FocusIn>', lambda event: on_entry_focus(event, password, 'Password'))
password.bind('<FocusOut>', lambda event: out_entry_focus(event, password, 'Password'))
Frame(frame_sign_in, width=400, height=2, bg='black').place(x=50, y=410)

# Nút đăng nhập
login = Button(frame_sign_in, text='Login', width=30, height=1, border=2, font=('Microsoft YahHei UI Light', 16), fg='white', bg='blue', command= lambda : login_user())
login.place(x=70, y=450)

show_frame(frame_sign_in)

# Thông báo không có tài khoản
Label(frame_sign_in, text="Don't have an account?", font=('Microsoft YahHei UI Light', 15), fg='red', bg='white').place(x=60, y=530)

# Nút đăng ký
sign_up_button = Button(frame_sign_in, text='Sign up', border=0, font=('Microsoft YahHei UI Light', 16), fg='blue', bg='white', command=lambda: show_frame(frame_sign_up))
sign_up_button.place(x=300, y=527)

# Tiêu đề đăng ký
Label(frame_sign_up, text='Create Account', font=('Microsoft YahHei UI Light', 30), fg='black', bg='white').place(x=100, y=75)

# Nhập tên người dùng cho đăng ký
user_signup = Entry(frame_sign_up, width=30, border=0, font=('Microsoft YahHei UI Light', 19))
user_signup.place(x=60, y=200)
user_signup.insert(0, 'User')
user_signup.bind('<FocusIn>', lambda event: on_entry_focus(event, user_signup, 'User'))
user_signup.bind('<FocusOut>', lambda event: out_entry_focus(event, user_signup, 'User'))
Frame(frame_sign_up, width=400, height=2, bg='black').place(x=50, y=230)

# Nhập mật khẩu cho đăng ký
password_signup = Entry(frame_sign_up, width=30, border=0, font=('Microsoft YahHei UI Light', 19), show = '*')
password_signup.place(x=60, y=280)
password_signup.insert(0, 'Password')
password_signup.bind('<FocusIn>', lambda event: on_entry_focus(event, password_signup, 'Password'))
password_signup.bind('<FocusOut>', lambda event: out_entry_focus(event, password_signup, 'Password'))
Frame(frame_sign_up, width=400, height=2, bg='black').place(x=50, y=310)

# Nhập xác nhận mật khẩu
confirm_password = Entry(frame_sign_up, width=30, border=0, font=('Microsoft YahHei UI Light', 19), show = '*')
confirm_password.place(x=60, y=360)
confirm_password.insert(0, 'Confirm Password')
confirm_password.bind('<FocusIn>', lambda event: on_entry_focus(event, confirm_password, 'Confirm Password'))
confirm_password.bind('<FocusOut>', lambda event: out_entry_focus(event, confirm_password, 'Confirm Password'))
Frame(frame_sign_up, width=400, height=2, bg='black').place(x=50, y=390)

# Nút đăng ký
sign_up_button = Button(frame_sign_up, text='Sign Up', width=30, height=1, border=2, font=('Microsoft YahHei UI Light', 16), fg='white', bg='blue')
sign_up_button.place(x=65, y=450)

root.mainloop()
