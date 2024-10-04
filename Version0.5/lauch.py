import connectSQL
# connect hoặc tạo cơ sở dữ liệu mới
connectSQL.C_database()

import sign_in
import sign_up
import Version0_5

import os

PathOfFile = os.path.abspath(__file__)
PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")

from tkinter import *

root = Tk(); root.title("Quản lý thư viện")
icon = PathOfFile + "/Image/" + "iconBook.ico"; root.iconbitmap(icon)

window_width = 1050; window_height = 570
screen_width = root.winfo_screenwidth(); screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2); center_y = int(screen_height/2 - window_height/2); center_y -= 25;
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Mặc định kích thước của cửa sổ
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

sign_in.sign_in(root)
#sign_up.sign_up(root)
#Version0_5.quanlykhosach(root)

def show_Version0_5():
    Version0_5.quanlykhosach(root)

root.mainloop()
