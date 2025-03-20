# main.py
from models.connectSQL import C_database
# connect hoặc tạo cơ sở dữ liệu mới
C_database()
import tkinter as tk
from tkinter import *

from controllers.user_control import start_app

root = Tk(); root.title("Quản lý thư viện")

window_width = 1050; window_height = 570
screen_width = root.winfo_screenwidth(); screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2); center_y = int(screen_height/2 - window_height/2); center_y -= 25;
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Mặc định kích thước của cửa sổ
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

start_app(root)


# Bắt đầu giao diện
root.mainloop()
