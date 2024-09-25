import tkinter as tk
from tkinter import Tk, Frame, Button, Label, ttk, Entry
from tkinter import PhotoImage
from tkinter import ttk

def show_frame(frame):
	frame.tkraise()

root = tk.Tk(); root.title("Quản lý thư viện")
icon = "iconBook.ico"; root.iconbitmap(icon)

# Lấy kích thước màn hình desktop
screen_width = root.winfo_screenwidth(); 
screen_height = root.winfo_screenheight()

window_width = 1050; window_height = 570

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
center_y -= 25;
# geometrey: hàm kích thước cửa sổ
# 'wigthXheight + x + y' // đặt cửa sổ ở tọa độ (x,y) khi mở
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

min_width = 700; min_height = 500; root.minsize(min_width, min_height)

# Tạo các Frame khác nhau
frameRoot = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root) 
frame3 = Frame(root) 

# Sử dụng grid() để đảm bảo các Frame chiếm toàn bộ không gian cửa sổ
for frame in (frameRoot, frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

# Đảm bảo các hàng và cột của root mở rộng
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

show_frame(frameRoot)

button1 = tk.Button(frameRoot,text="Quản lý kho sách", font=("Arial", 20), command=lambda: show_frame(frame1))
button1.place(relx=0.5, rely=0.2, anchor="center",  width=250, height=50)

button2 = tk.Button(frameRoot,text="Thông tin bạn đọc", font=("Arial", 20), command=lambda: show_frame(frame2))
button2.place(relx=0.5, rely=0.4, anchor="center",  width=250, height=50)

button3 = tk.Button(frameRoot,text="Thống kê, báo cáo", font=("Arial", 20), command=lambda: show_frame(frame3))
button3.place(relx=0.5, rely=0.6, anchor="center",  width=250, height=50)

## Fame 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## Các hàm để tạo Dòng chữ mờ tại Entry  - placeholder
def set_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text); entry.config(fg='grey')

def on_entry_click(event, entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end"); entry.config(fg='black')

def on_focusout(event, entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text); entry.config(fg='grey')

def apply_placeholder(entry, placeholder_text):
    # Áp dụng placeholder cho một Entry.
    set_placeholder(entry, placeholder_text) 
    entry.bind("<FocusIn>", lambda event: on_entry_click(event, entry, placeholder_text))
    entry.bind("<FocusOut>", lambda event: on_focusout(event, entry, placeholder_text))

label_Timkiem = tk.Label(frame1, text = "Tìm kiếm: ", font=("Arial", 24))
label_Timkiem.grid(row=0, column=0, padx=5, pady=5)

entry_Timkiem = tk.Entry(frame1, width = 25, font=("Arial", 20))
apply_placeholder(entry_Timkiem, "Nhập nội dung tìm kiếm")
entry_Timkiem.grid(row=0, column = 1, padx=5, pady=5)

label_Timtheo = tk.Label(frame1, text = "Tìm theo: ", font=("Arial", 24))
label_Timtheo.grid(row=0,column = 2, padx=5, pady=5)

def on_option_select(selection):
    print(f"Selected option: {selection}")

# Các lựa chọn đã được thêm vào sẵn
options = ["Tên sách", "Tên tác giả", "Năm sáng tác"]

# Biến để lưu lựa chọn được chọn
selected_option = tk.StringVar()
selected_option.set(options[0])  # Đặt giá trị mặc định

# Tạo OptionMenu
dropdown = tk.OptionMenu(frame1, selected_option, *options, command=on_option_select)
dropdown.config(font=("Arial", 20))
dropdown.grid(row=0, column=3, padx=5, pady=5)

# Tạo nút với icon
search_icon = PhotoImage(file="search_icon.png")
search_button = tk.Button(frame1, image=search_icon, width = 40, height = 40)
search_button.grid(row=0, column = 4, padx=5, pady=5)

## Các trường: 
#Mã sách, tên sách, thể loại, tác giả, nhà xuất bản, ngày xuất bản, tổng số sách, đang mượn, giá tiền
# làm sao để có thể tùy chọn hiện thị và tắt hiện thị những cái này !!

# cơ sở dữ liệu giả lập

Books = [('001', 'Lập trình python', 'CNTT', 'Tên Tác Giả', 'Nhà xuất bản Kim Đồng', '17/01/2000', 100, 10, 100000),
		('002', 'Lập trình nâng cao', 'CNTT', 'Tên Tác Giả', 'Nhà xuất bản Kim Đồng', '17/01/2000', 100, 10, 100000),
		('003', 'Lập trình OOP', 'CNTT', 'Tên Tác Giả', 'Nhà xuất bản Kim Đồng', '17/01/2000', 100, 10, 100000),
		('001', 'Lập trình python', 'CNTT', 'Tên Tác Giả', 'Nhà xuất bản Kim Đồng', '17/01/2000', 100, 10, 100000),
		('002', 'Lập trình nâng cao', 'CNTT', 'Tên Tác Giả', 'Nhà xuất bản Kim Đồng', '17/01/2000', 100, 10, 100000),
		('003', 'Lập trình OOP', 'CNTT', 'Tên Tác Giả', 'Nhà xuất bản Kim Đồng', '17/01/2000', 100, 10, 100000),
		('001', 'Lập trình python', 'CNTT', 'Tên Tác Giả', 'Nhà xuất bản Kim Đồng', '17/01/2000', 100, 10, 100000),
		('002', 'Lập trình nâng cao', 'CNTT', 'Tên Tác Giả', 'Nhà xuất bản Kim Đồng', '17/01/2000', 100, 10, 100000),
		('003', 'Lập trình OOP', 'CNTT', 'Tên Tác Giả', 'Nhà xuất bản Kim Đồng', '17/01/2000', 100, 10, 100000),
		('003', 'Lập trình OOP', 'CNTT', 'Tên Tác Giả', 'Nhà xuất bản Kim Đồng', '17/01/2000', 100, 10, 100000),]

# Tạo Treeview
tree = ttk.Treeview(frame1, columns=('ID', 'Tên sách', 'Thể loại', 'Tác giả', 'Nhà xuất bản', 'Ngày xuất bản', 'Tổng số lượng', 'Số đang mượn' , 'Giá sách'), show='headings', height=20)

# Định nghĩa chiều rộng cột
for col, width in zip(('ID', 'Tên sách', 'Thể loại', 'Tác giả', 'Nhà xuất bản', 'Ngày xuất bản', 'Tổng số lượng', 'Số đang mượn', 'Giá sách'), [50, 150, 75, 120, 175, 100, 100, 100, 100]):
    tree.column(col, width=width)
    tree.heading(col, text=col)

# Thêm dữ liệu vào Treeview
for book in Books:
    tree.insert('', tk.END, values=book)

# Thêm thanh trượt
vsb = ttk.Scrollbar(frame1, orient="vertical", command=tree.yview); 
vsb.grid(row=1, column = 5, sticky='ns')
tree.configure(yscrollcommand=vsb.set)

# Đặt Treeview vào cửa sổ
tree.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

# Các button row 2

frame1_3 = Frame(frame1);

frame1_3.grid(row = 2, column = 0, columnspan=5, sticky='nsew')

button_Tao = tk.Button(frame1_3,text="Thêm sách", font=("Arial", 20), command=lambda: show_frame(frameRoot))
button_Tao.grid(row=0, column = 0, padx=10);

button_Sua = tk.Button(frame1_3,text="Sửa sách", font=("Arial", 20), command=lambda: show_frame(frameRoot))
button_Sua.grid(row=0, column = 1, padx=10);

button_Xoa = tk.Button(frame1_3,text="Xóa sách", font=("Arial", 20), command=lambda: show_frame(frameRoot))
button_Xoa.grid(row=0, column = 2, padx=10);

entry_ID = tk.Entry(frame1_3, width = 18, font=("Arial", 27))
apply_placeholder(entry_ID, "ID sách muốn sửa/xóa")
entry_ID.grid(row=0, column = 3, padx=10)

# Hàm xử lý sự kiện bàn phím (phím Z)
def on_key_press(event):
    if event.char == 'z' or event.char == 'Z':
        show_frame(frameRoot) 

# Gán sự kiện nhấn phím Z với cửa sổ chính
root.bind('<Key>', on_key_press)

root.mainloop()