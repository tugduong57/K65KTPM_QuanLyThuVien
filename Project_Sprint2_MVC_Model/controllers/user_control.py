#user_controller
from tkinter import messagebox
from views.user_views import sign_up, sign_in
from models.user_model import check_sign_in, check_sign_up_model, Insert_admin
from controllers.reader_control import show_reader
# Check đăng nhập
def login_user(root, username_input, password_input):
    check = check_sign_in(username_input, password_input)
    if check : 
        show_reader(root)
        return

    messagebox.showerror("Thông báo", "Tài khoản hoặc mật khẩu không đúng")

# Function to handle signup
def check_sign_up(root, username, password_input, confirm_password_input):
    if password_input != confirm_password_input:
        messagebox.showerror("Thông báo", "Mật khẩu không giống nhau!")
        return

    check = check_sign_up_model(username)

    if not(check): 
        Insert_admin(username, password_input)
        messagebox.showinfo("Sign Up", "Đã tạo tài khoản thành công!")
        sign_in(root, login_user, show_signup)
        return
    else:
        messagebox.showinfo("Thông báo", "Tạo tài khoản không thành công!")
        return

def start_app(root):
    sign_in(root, login_user, show_signup)
    return

def show_signup(root):
    sign_up(root, check_sign_up, start_app);
    return
