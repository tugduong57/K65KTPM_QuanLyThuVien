import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk 
import os
import add_book, edit_book, del_book, connectSQL
from placeholder import apply_placeholder

PathOfFile = os.path.abspath(__file__)
PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")

def quanlykhosach(root):
    def on_label_click(event):
        event.widget.focus_set()
    window_width = 1050; window_height = 570
    
    def Xuly_Anh(imageOfpath, size_width, size_height):
        original_image = Image.open(imageOfpath)
        image = original_image.resize((size_width, size_height), resample=Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image

    # Tạo frame Root - frame chính của phần mềm
    Root = Frame(root);
    Root.grid(row = 0, column = 0, sticky = 'nsew')
    Root.tkraise()

    # Thêm background
    bgKhoSach = Xuly_Anh(PathOfFile + "/Image/" +'bg5.png', window_width, window_height)
    bg_Root = Label(Root, image = bgKhoSach, borderwidth=0, highlightthickness=0); bg_Root.place(x = 0, y = 0)
    bg_Root.bind("<Button-1>", on_label_click)

    Books = connectSQL.show_sach()

    global Timkiem_; Timkiem_ = ["",""]
    global listOfBook; listOfBook = []
    global listOfID; listOfID = []

    if Timkiem_[0] == "" and Timkiem_[1] == "":
        for b in Books:
            listOfID.append(b[0])
            listOfBook.append(b[1])

    listLabelOfBook = []; listLabelOfID = []
    listPlaceOfID = [[320, 32],[345,78], [365,124], [379, 169], [387,215], [391, 260], [389, 305], [383,352], [373,397], [358,442]]
    m = 50; n = 46

    # 20 Label cố định
    for i in range(min(10,len(listOfID))):
        listLabelOfBook.append(Label(Root, text = listOfBook[i], bg = 'white', fg = '#145da0', font =("Poppins", 17), borderwidth=0, highlightthickness=0 ))
        listLabelOfID.append(Label(Root, text = listOfID[i], bg = 'white', fg = '#145da0', font =("Poppins", 9), borderwidth=0, highlightthickness=0))

    for i in range(min(10,len(listOfID))):
        listLabelOfID[i].place(x= listPlaceOfID[i][0]-5,y= listPlaceOfID[i][1])
        listLabelOfBook[i].place(x = listPlaceOfID[i][0]+57, y= listPlaceOfID[i][1]-5)

    def update_Timkiem():
        global listOfBook; global listOfID 
        global Timkiem_;

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

    def update_labels():
        for i in range(min(10,len(listOfID))):
            if scroll_index + i < len(listOfID):
                listLabelOfID[i].config(text=listOfID[scroll_index + i])
                listLabelOfBook[i].config(text=listOfBook[scroll_index + i])
            else:
                listLabelOfID[i].config(text="")
                listLabelOfBook[i].config(text="")

    def mouse_scroll(event):
        global scroll_index; global listOfID;
        if event.delta > 0:     # Cuộn lên
            scroll_index = max(scroll_index - 1, 0)
        elif event.delta < 0:   # Cuộn xuống
            scroll_index = min(scroll_index + 1, len(listOfID) - 10)

        if scroll_index >= 0:   # Cập nhật nội dung của các label
            update_labels()

    def enter_on_Timkiem(event):
        Timkiem_text = entry_Timkiem.get()
        Timkiem_[1] = Timkiem_text
        update_Timkiem()

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

    buttonBanDoc = Button(Root, text = "Độc giả", bg = '#145da0', fg = "white", font =("Poppins", 20), borderwidth=0, highlightthickness=0);  buttonBanDoc.place(x=95, y=310, height = 30)

    buttonBaoCao = Button(Root, text = "Báo cáo", bg = '#145da0', fg = "white", font =("Poppins", 20), borderwidth=0, highlightthickness=0); buttonBaoCao.place(x=95, y=427, height = 30)

    def Add_book(root, Root):
        add_book.add_book(root, Root);
        return

    ig_Them = Xuly_Anh(PathOfFile + "/Image/"+'buttonThem.png', 66, 66)
    buttonThem = Button(Root, image=ig_Them, command = lambda : Add_book(Root, root), borderwidth=0, highlightthickness=0); buttonThem.place(x=425, y=490)

    def Edit_book(root, Root):
        bookOfID = entry_ID.get()
        book = connectSQL.find_sach("Mã sách", bookOfID)
        if len(book) == 0:
            return
        edit_book.edit_book(root, Root, book);
        return

    ig_Sua = Xuly_Anh(PathOfFile + "/Image/"+'buttonSua.png', 66, 66)
    buttonSua = Button(Root, image=ig_Sua, command = lambda : Edit_book(Root, root), borderwidth=0, highlightthickness=0); buttonSua.place(x=530, y=490)

    def Del_book(root):
        bookOfID = entry_ID.get()
        book = connectSQL.find_sach("Mã sách", bookOfID)
        if len(book) == 0:
            return
        del_book.del_book(root,bookOfID)
        return

    ig_Xoa = Xuly_Anh(PathOfFile + "/Image/"+'buttonXoa.png', 66, 66)
    buttonXoa = Button(Root, image=ig_Xoa, command = lambda : Del_book(root), borderwidth=0, highlightthickness=0); buttonXoa.place(x=635, y=490)

    for N in [buttonThem, buttonSua, buttonXoa, buttonBanDoc, buttonBaoCao]:
        N.bind("<Enter>", on_enter)
        N.bind("<Leave>", on_leave)

    # Liên kết sự kiện cuộn chuột
    root.bind("<MouseWheel>", mouse_scroll) # lăn chuột

    root.update_idletasks()
    root.mainloop()