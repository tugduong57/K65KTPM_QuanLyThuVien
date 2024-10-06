import tkinter as tk
from tkinter import Tk, Frame, Button, Label, ttk, Entry
from PIL import Image, ImageTk 
from tkinter import ttk
import math
import os
import add_book
import connectSQL
import doc_gia

PathOfFile = os.path.abspath(__file__)
PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")


def show_frame(frame):
    frame.tkraise()

def quanlykhosach(root):
    def mouse_index(event):
        x, y = event.x, event.y
        print(f"Vị trí chuột: x={x}, y={y}")

    root.bind("<Button-1>", mouse_index)
    
    def on_label_click(event):
        event.widget.focus_set()
        print("Label was clicked!")

    window_width = 1050; window_height = 570
    
    def Xuly_Anh(imageOfpath, size_width, size_height):
        original_image = Image.open(imageOfpath)
        image = original_image.resize((size_width, size_height), resample=Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    # Tạo frame Root - frame chính của phần mềm
    Root = Frame(root);
    Root.grid(row = 0, column = 0, sticky = 'nsew')

    show_frame(Root);

    # Thêm background
    bgKhoSach = Xuly_Anh(PathOfFile + "/Image/" +'bg5.png', window_width, window_height)
    bg_Root = Label(Root, image = bgKhoSach, borderwidth=0, highlightthickness=0); bg_Root.place(x = 0, y = 0)
    bg_Root.bind("<Button-1>", on_label_click)

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
    
    def Add_book(root, Root):
        add_book.add_book(root, Root);
        return

    def Edit_book(root, Root):
        pass
    
    def sua_sach(root):
        frame_edit = Frame(root)
        frame_edit.grid(row=0, column=0, sticky='nsew')
        
        # Cấu hình grid cho root để frame_add có thể lấp đầy toàn bộ không gian
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        title_label = Label(frame_edit, text='Sửa đầu sách', font=('Arial', 24))
        title_label.grid(row=0, column=0, columnspan=3, pady=20)

        # Tạo Frame cho hai bên
        frame_left = Frame(frame_edit)
        frame_left.grid(row=1, column=0, padx=10, pady=10)

        frame_right = Frame(frame_edit)
        frame_right.grid(row=1, column=1, padx=10, pady=10)

        # Các label cho thông tin sách bên trái
        labels_left = ['Mã sách', 'Tên sách', 'Thể loại', 'Tác giả']
        entries_left = []

        # Dữ liệu mẫu để sửa
        existing_data = ['001', 'Lập trình python', 'CNTT', 'Tên Tác Giả']  # Dữ liệu sách hiện có

        for i, label in enumerate(labels_left):
            label_widget = Label(frame_left, text=label, font=('Arial', 15))
            label_widget.grid(row=i, column=0, pady=20, padx=20)

            entry = Entry(frame_left, font=('Arial', 15), width=25)
            entry.grid(row=i, column=1, pady=20, padx=20)
            entry.insert(0, existing_data[i])  # Chèn dữ liệu đã có vào Entry
            entries_left.append(entry)

        # Các label cho thông tin sách bên phải
        labels_right = ['Nhà xuất bản', 'Ngày sản xuất', 'Số lượng', 'Giá']
        entries_right = []

        # Dữ liệu mẫu để sửa
        existing_data_right = ['Nhà xuất bản Kim Đồng', '17/01/2000', '100', '100000']  # Dữ liệu sách hiện có

        for i, label in enumerate(labels_right):
            label_widget = Label(frame_right, text=label, font=('Arial', 15))
            label_widget.grid(row=i, column=0, pady=20, padx=20)

            entry = Entry(frame_right, font=('Arial', 15), width=25)
            entry.grid(row=i, column=1, pady=20, padx=20)
            entry.insert(0, existing_data_right[i])  # Chèn dữ liệu đã có vào Entry
            entries_right.append(entry)

        button_save = Button(frame_edit, text='Lưu', bg='green', fg='white', font=('Arial', 20))
        button_save.grid(row=2, column=1, pady=10)

        button_cancel = Button(frame_edit, text='Hủy', bg='red', fg='white', font=('Arial', 20),
                            command=lambda: show_frame(Root))  # Quay lại màn hình chính
        button_cancel.grid(row=2, column=2)

        show_frame(frame_edit)

    # cơ sở dữ liệu giả lập

    Books = []

    with open(PathOfFile + "/Image/"+"data.txt", encoding='utf-8') as inp:
        for i in range(10000):
            t = list(inp.readline().split(','))
            Books.append(t);
     
    Members = []
    with open(PathOfFile + "/Image/"+"data2.txt", encoding='utf-8') as inp:
        for i in range(10000):
            t = list(inp.readline().split(','))
            Members.append(t);

    global Timkiem_; Timkiem_ = ["",""]
    global listOfBook; listOfBook = []
    global listOfID; listOfID = []

    if Timkiem_[0] == "" and Timkiem_[1] == "":
        for b in Books[:10000]:
            listOfID.append(b[0])
            listOfBook.append(b[1])
    elif Timkiem_[0] != "" and Timkiem_[1] != "":
        if Timkiem_[0] == "Mã sách":
            for b in Books[:10000]:
                if b[0] == Timkiem_[1]:
                    listOfID.append(b[0])
                    listOfBook.append(b[1])

    listLabelOfBook = []; listLabelOfID = []
    listPlaceOfID = [[320, 32],[345,78], [365,124], [379, 169], [387,215], [391, 260], [389, 305], [383,352], [373,397], [358,442]]
    m = 50; n = 46

    for i in range(min(10,len(listOfID))):
        listLabelOfBook.append(Label(Root, text = listOfBook[i], bg = 'white', fg = '#145da0', font =("Poppins", 17), borderwidth=0, highlightthickness=0 ))
        listLabelOfID.append(Label(Root, text = listOfID[i], bg = 'white', fg = '#145da0', font =("Poppins", 10), borderwidth=0, highlightthickness=0))

    for i in range(min(10,len(listOfID))):
        listLabelOfID[i].place(x= listPlaceOfID[i][0]-5,y= listPlaceOfID[i][1])
        listLabelOfBook[i].place(x = listPlaceOfID[i][0]+57, y= listPlaceOfID[i][1]-5)

    def update_Timkiem(event):
        global listOfBook; global listOfID 
        global Timkiem_;
        print("174",Timkiem_)
        listOfID = []; listOfBook = []
        if Timkiem_[0] == "" or Timkiem_[1] == "":
            for i in range(len(Books)):
                listOfID.append(Books[i][0])
                listOfBook.append(Books[i][1])
        elif Timkiem_[0] != "" and Timkiem_[1] != "":
            book = connectSQL.find_sach(Timkiem_[0], Timkiem_[1])
            for i in range(len(book)) :
                listOfID.append(book[i][0])
                listOfBook.append(book[i][1])


            # if Timkiem_[0] == "Mã sách":
            #     print("Tìm theo mã sách")
            #     for i in range(len(Books)):
            #         if Books[i][0] == Timkiem_[1]:
            #             listOfID.append(Books[i][0])
            #             listOfBook.append(Books[i][1])
            # elif Timkiem_[0] == "Tên sách":
            #     print("Tìm theo tên sách")
            #     for i in range(len(Books)):
            #         if Timkiem_[1].lower() in Books[i][1].lower():
            #             listOfID.append(Books[i][0])
            #             listOfBook.append(Books[i][1])
            # elif Timkiem_[0] == "Thể loại":
            #     print("Tìm theo thể loại")
            #     for i in range(len(Books)):
            #         if Timkiem_[1].lower() in Books[i][2].lower():
            #             listOfID.append(Books[i][0])
            #             listOfBook.append(Books[i][1])
            # elif Timkiem_[0] == "Tên tác giả":
            #     print("Tìm theo tác giả")
            #     for i in range(len(Books)):
            #         if Timkiem_[1].lower() in Books[i][3].lower():
            #             listOfID.append(Books[i][0])
            #             listOfBook.append(Books[i][1])
        for i in range(min(10,len(listOfID))):
            listLabelOfBook[i].config(text = listOfBook[i])
            listLabelOfID[i].config(text = listOfID[i])
        try:
            for i in range(min(10,len(listOfID)),10):
                listLabelOfBook[i].config(text = "")
                listLabelOfID[i].config(text = "") 
        except:
            pass  
    
    # Tính năng cuộn
    global scroll_index; scroll_index = 0  # Để lưu chỉ số của sách hiện tại

    def mouse_scroll(event):
        global scroll_index; global listOfID;
        if event.delta > 0:     # Cuộn lên
            scroll_index = max(scroll_index - 1, 0)
        elif event.delta < 0:   # Cuộn xuống
            scroll_index = min(scroll_index + 1, len(listOfID) - 10)

        if scroll_index >= 0:   # Cập nhật nội dung của các label
            update_labels()

    def update_labels():
        for i in range(min(10,len(listOfID))):
            if scroll_index + i < len(listOfID):
                listLabelOfID[i].config(text=listOfID[scroll_index + i])
                listLabelOfBook[i].config(text=listOfBook[scroll_index + i])
            else:
                listLabelOfID[i].config(text="")
                listLabelOfBook[i].config(text="")

    def enter_on_Timkiem(event):
        Timkiem_text = entry_Timkiem.get()
        Timkiem_[1] = Timkiem_text
        update_Timkiem(event)

    entry_Timkiem = tk.Entry(Root, width = 14, font=("Arial", 20), bg = "#ceddea", borderwidth=0, highlightthickness=0)
    entry_Timkiem.place(x= 35, y = 107)

    entry_ID = tk.Entry(Root, width = 12, font=("Arial", 23), bg = "#94b5d3", borderwidth=0, highlightthickness=0)
    apply_placeholder(entry_ID, "ID xóa/sửa")
    entry_ID.place(x = 774, y = 517)

    entry_Timkiem.bind('<Return>', enter_on_Timkiem)

    def on_option_select(selection):
        print(f"Selected option: {selection}")
        selected_option = selection;
        Timkiem_[0] = selected_option
        print(selected_option)
    # Các lựa chọn đã được thêm vào sẵn
    # Mã sách, tên sách, thể loại, tác giả, nhà xuất bản, ngày xuất bản, giá sách, tổng số sách
    options = ["Mã sách", "Tên sách", "Thể loại", "Tên tác giả"]
    
    # Biến để lưu lựa chọn được chọn
    selecting_option = tk.StringVar()
    selecting_option.set("Chọn kiểu muốn tìm") 

    # Tạo OptionMenu
    dropdown = tk.OptionMenu(Root, selecting_option, *options, command=on_option_select)
    dropdown.config(font=("Arial", 17), bg = "#ceddea", fg = "black", borderwidth=0, highlightthickness=0)
    dropdown.place(x=35, y=177)

    def on_enter(event):
        event.widget.config(cursor='hand2')  # Thay đổi màu nền và kiểu con trỏ khi chuột vào label

    def on_leave(event):
        event.widget.config(cursor='')  # Khôi phục màu nền và kiểu con trỏ khi chuột ra khỏi label

    buttonBanDoc = Button(Root, text = "Độc giả", bg = '#145da0', fg = "white", font =("Poppins", 20), borderwidth=0, highlightthickness=0, command = lambda : doc_gia.doc_gia(root))
    buttonBanDoc.place(x=95, y=310, height = 30)

    buttonBaoCao = Button(Root, text = "Báo cáo", bg = '#145da0', fg = "white", font =("Poppins", 20), borderwidth=0, highlightthickness=0)
    buttonBaoCao.place(x=95, y=427, height = 30)

    ig_Them = Xuly_Anh(PathOfFile + "/Image/"+'buttonThem.png', 66, 66)
    buttonThem = Button(Root, image=ig_Them, command = lambda : Add_book(Root, root), borderwidth=0, highlightthickness=0); buttonThem.place(x=425, y=490)

    ig_Sua = Xuly_Anh(PathOfFile + "/Image/"+'buttonSua.png', 66, 66)
    buttonSua = Button(Root, image=ig_Sua, command = lambda : Edit_book(Root, root), borderwidth=0, highlightthickness=0); buttonSua.place(x=530, y=490)

    ig_Xoa = Xuly_Anh(PathOfFile + "/Image/"+'buttonXoa.png', 66, 66)
    buttonXoa = Button(Root, image=ig_Xoa, borderwidth=0, highlightthickness=0); buttonXoa.place(x=635, y=490)

    for N in [buttonThem, buttonSua, buttonXoa, buttonBanDoc, buttonBaoCao]:
        N.bind("<Enter>", on_enter)
        N.bind("<Leave>", on_leave)

    # Liên kết sự kiện cuộn chuột
    root.bind("<MouseWheel>", mouse_scroll) # lăn chuột

    root.update_idletasks()
    root.mainloop()