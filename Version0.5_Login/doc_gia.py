import tkinter as tk
from tkinter import Tk, Frame, Button, Label, ttk, Entry
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk 
import os
import Version0_5


def doc_gia(root) :

    PathOfFile = os.path.abspath(__file__)
    PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")

    def show_frame(frame):
    	frame.tkraise()

    # root = tk.Tk(); 
    # root.title("Quản lý thư viện")
    # icon = "iconBook.ico"; 
    root.iconbitmap(r"D:\google drive\A_demo_codeBTL\test_code\iconBook.ico")

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
    frame2 = Frame(root) 


    frameRoot.grid(row=0, column=0, sticky="nsew")
    frame2.grid(row=0, column=0, sticky="nsew")


    # Đảm bảo các hàng và cột của root mở rộng
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    def on_key_press(event):
        if event.char == 'z' or event.char == 'Z':
            show_frame(frameRoot) 

    # Gán sự kiện nhấn phím Z với cửa sổ chính
    root.bind('<Key>', on_key_press)


    def Xuly_Anh(imageOfpath, size_width, size_height):
        original_image = Image.open(imageOfpath)
        image = original_image.resize((size_width, size_height), resample=Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    # Thêm background
    bgKhoSach = Xuly_Anh(PathOfFile + "/Image/" +'bgdocgia.png', window_width, window_height)
    bg_Root = Label(frame2, image = bgKhoSach, borderwidth=0, highlightthickness=0); bg_Root.place(x = 0, y = 0)


    # Định dạng tiêu đề cho treeview
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))

    # FRAME 2
    tree2 = ttk.Treeview(frame2, columns = ('MÃ ĐỘC GIẢ', 'HỌ VÀ TÊN', 'SỐ ĐT', 'TRẠNG THÁI'), show='headings', height = 10)
    tree2.place(relx=0.5, rely=0.48, anchor='center')


    for col, width in zip(('MÃ ĐỘC GIẢ', 'HỌ VÀ TÊN', 'SỐ ĐT', 'TRẠNG THÁI'), [130, 250, 100, 200]) :
        tree2.column(col, anchor="center", width = width)
        tree2.heading(col, text = col)


    # # frame thêm xóa chỉnh sửa
    # frame2_1 = Frame(frame2);
    # frame2_1.grid(row = 3, column = 0, columnspan=5, sticky='nsew')


    # Hàm để hiển thị thông báo và tự động xóa sau một khoảng thời gian
    frame2_3 = tk.Frame(frame2)
    frame2_3.place(relx = 0.5, rely = 0.95, anchor = 'center')

    def show_message():
        # Tạo một Label để hiển thị thông báo
        message_label = tk.Label(frame2_3, text= "\u26A0Vui lòng chọn bản ghi muốn xóa !", font=("Arial", 12))
        message_label.grid()

        # Sử dụng hàm after để xóa Label sau 2 giây (2000 milliseconds)
        root.after(2000, message_label.destroy)

    # Xóa bạn đọc
    def delete_ban_doc() :
        try :
            selected_item =  tree2.focus()
            tree2.delete(selected_item)
        except :
            show_message()


    # Các nút thêm, xóa, chỉnh sửa
    ig_Them = Xuly_Anh(PathOfFile + "/Image/"+'buttonThem.png', 66, 66)
    button_them = tk.Button(frame2, image=ig_Them, command=lambda: Version0_5.quanlykhosach(root), borderwidth=0, highlightthickness=0)
    # button_them.grid(row=0, column = 0, padx=80, pady = 80, sticky = 'e');
    button_them.place(x = 330, y = 470);


    ig_Xoa = Xuly_Anh(PathOfFile + "/Image/"+'buttonXoa.png', 66, 66)
    button_xoa = tk.Button(frame2,image=ig_Xoa, borderwidth=0, highlightthickness=0, command= delete_ban_doc)
    # button_xoa.grid(row=0, column = 1, padx=20);
    button_xoa.place(x = 430, y = 470);


    ig_Sua = Xuly_Anh(PathOfFile + "/Image/"+'buttonSua.png', 66, 66)
    button_chinh_sua = tk.Button(frame2,image=ig_Sua, borderwidth=0, highlightthickness=0, command=lambda: Version0_5.quanlykhosach(root))
    # button_chinh_sua.grid(row=0, column = 2, padx=70);
    button_chinh_sua.place(x = 530, y = 470);


    ig_back = Xuly_Anh(PathOfFile + "/Image/"+'3.png', 66, 66)
    button_quay_lai = tk.Button(frame2, image = ig_back,borderwidth=0, highlightthickness=0, command=lambda: Version0_5.quanlykhosach(root))
    # button_quay_lai.grid(row=0, column = 3, padx = 0)
    button_quay_lai.place(x = 630, y = 470);

    # Cơ sở dữ liệu dạng list
    Books_2 = [('1001', 'Nguyễn Văn A', '0123456789', 'Bình thường'),
            ('1002', 'Nguyễn Văn B', '0123456789', 'Bình thường'),
            ('1003', 'Nguyễn Văn C', '0123456789', 'Bình thường'),
            ('1004', 'Nguyễn Văn D', '0123456789', 'Bình thường'),
            ('1005', 'Nguyễn Văn E', '0123456789', 'Bình thường'),
            ('1006', 'Nguyễn Văn F', '0123456789', 'Bình thường'),
            ('1007', 'Nguyễn Văn G', '0123456789', 'Bình thường'),
            ('1008', 'Nguyễn Văn H', '0123456789', 'Bình thường'),
            ('1009', 'Nguyễn Văn M', '0123456789', 'Bình thường'),
            ('1010', 'Nguyễn Văn N', '0123456789', 'Bình thường'),
            ('1010', 'Nguyễn Văn N', '0123456789', 'Bình thường'),
            ('1010', 'Nguyễn Văn N', '0123456789', 'Bình thường'),
            ('1010', 'Nguyễn Văn N', '0123456789', 'Bình thường')]
    # Chèn dữ liệu và1001
    for book in Books_2:
        tree2.insert('', tk.END, values=book)

    # Thanh trượt cho treeview
    vsb = ttk.Scrollbar(frame2, orient="vertical", command = tree2.yview); 
    vsb.place(relx=0.832, rely=0.48, anchor='center',height=226)
    tree2.configure(yscrollcommand = vsb.set)



    # Frame cho Label entry tìm kiếm
    # frame2_2 = Frame(frame2)
    # frame2_2.place(relx=0.5, rely=0.7, anchor='center')

    # Hàm tạo các chữ mờ trên entry
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


    # Tạo nút tìm kiếm 
    # label_Timkiem = tk.Label(frame2_2, text = "Tìm kiếm: ", font=("Arial", 24) )
    # label_Timkiem.grid(row=0, column=0, padx=5, pady=5, sticky = "nsew")


    # Tạo entry
    entry_Timkiem = tk.Entry(frame2, width = 15, font=("Arial", 20),bg = "#ceddea",  borderwidth=0, highlightthickness=0)
    apply_placeholder(entry_Timkiem, "         Search")
    entry_Timkiem.place(x = 375, y = 410)


    # Hàm tìm kiếm trong treeview

    def show_message_2():
        # Tạo một Label để hiển thị thông báo
        message_label = tk.Label(frame2_3, text= "\u26A0 Không có thông tin cần tìm !", font=("Arial", 12))
        message_label.grid()

        # Sử dụng hàm after để xóa Label sau 2 giây (2000 milliseconds)
        root.after(2000, message_label.destroy)


    def search_in_treeview():
        search_term = entry_Timkiem.get().lower()  # Lấy chuỗi tìm kiếm từ Entry
        for item in tree2.get_children():  # Duyệt qua các item trong Treeview
            values = tree2.item(item, "values")  # Lấy giá trị của mỗi hàng
            if any(search_term in str(value).lower() for value in values):  # Kiểm tra nếu từ khóa có trong bất kỳ cột nào
                tree2.selection_set(item)  # Chọn hàng khớp
                tree2.see(item)  # Cuộn đến hàng khớp
        # else:
            # show_message_2()
            # print('Không có thong tin cần tìm')


    def show_message():
        # Tạo một Label để hiển thị thông báo
        message_label = tk.Label(frame2_3, text= "\u26A0 Vui lòng chọn bản ghi muốn xóa !", font=("Arial", 12))
        message_label.grid()

        # Sử dụng hàm after để xóa Label sau 2 giây (2000 milliseconds)
        root.after(2000, message_label.destroy)


    # Tạo frame search
    frame_search = tk.Frame(root)
    frame_search.grid(row = 0, column = 0, sticky = 'snew')

    Label(frame_search, text = 'THÔNG TIN BẠN ĐỌC', font=("Arial", 24)).grid(row = 0, column = 0, padx = 350, pady = 20)


    book_search = []
    tree_search = ttk.Treeview(frame_search, columns = ('MaSV', 'Họ và Tên', 'Lớp', 'Thông tin sách', 'Số lượng mượn', 'Ngày mượn', 'Hạn trả sách'), show = 'headings', height = 13)
    tree_search.grid(row = 1, column = 0, columnspan = 5, padx = 70, pady = 0, sticky = 'nsew')
    for col, width in zip(('MaSV', 'Họ và Tên', 'Lớp', 'Thông tin sách', 'Số lượng mượn', 'Ngày mượn', 'Hạn trả sách'), [100, 150, 75, 150, 175, 120, 120]) :
        tree_search.column(col, anchor = 'center', width = width)
        tree_search.heading(col, text = col)

    # Tạo nút search với icon
    ig_search = Xuly_Anh(PathOfFile + "/Image/"+'4.png', 50, 50)
    search_button = tk.Button(frame2, image=ig_search, borderwidth=0, highlightthickness=0 ,command = search_in_treeview)
    search_button.place(x = 620, y = 403) 

    frame_back = tk.Frame(frame_search)
    frame_back.place(relx=0.5, rely=0.75, anchor='center')


    # button_quay_lai = tk.Button(frame2_1,text="\u2B05", font=("Arial", 20), command=lambda: show_frame(frameRoot))
    # button_quay_lai.grid(row=0, column = 3, padx = 0)

    # ig_back = Xuly_Anh(PathOfFile + "/Image/"+'3.png', 66, 66)
    # button_back = tk.Button(frame_back, image =ig_back ,borderwidth=0, highlightthickness=0, command=lambda: show_frame(frame2))
    # button_back.grid(row=0, column = 0)

    show_frame(frame2)
    root.mainloop()