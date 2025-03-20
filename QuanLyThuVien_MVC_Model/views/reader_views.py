import tkinter as tk
from tkinter import *
from views.placeholder import apply_placeholder 
from PIL import Image, ImageTk 
import os

from views.move_widget_with_arrows import move_widget_with_arrows

PathOfFile = os.path.abspath(__file__)
PathOfFile = os.path.dirname(PathOfFile).replace("\\", "/")

def Quan_ly_ban_doc(root):
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
    bgKhoSach = Xuly_Anh(PathOfFile + "/Image/" +'bgQuanLyDocGia.png', window_width, window_height)
    bg_Root = Label(Root, image = bgKhoSach, borderwidth=0, highlightthickness=0); bg_Root.place(x = 0, y = 0)
    bg_Root.bind("<Button-1>", on_label_click)

    entry_Timkiem = tk.Entry(Root, width = 19, font=("Arial", 17), fg = "white", bg = "#8bbbdd", borderwidth=0, highlightthickness=0)
    apply_placeholder(entry_Timkiem,"Nhập nội dung tìm kiếm")    
    entry_Timkiem.place(x= 270, y = 25)

    def on_enter(event):
        event.widget.config(cursor='hand2')  # Thay đổi màu nền và kiểu con trỏ khi chuột vào label

    def on_leave(event):
        event.widget.config(cursor='')  # Khôi phục màu nền và kiểu con trỏ khi chuột ra khỏi label

    buttonBanDoc = Button(Root, text = "Độc giả", bg = '#0063a1', fg = "white", font =("Poppins", 20), borderwidth=0, highlightthickness=0);  
    buttonBanDoc.place(x=60, y= 162, height = 30)
    
    buttonMuonTra = Button(Root, text = "Mượn trả", bg = '#0063a1', fg = "white", font =("Poppins", 20), borderwidth=0, highlightthickness=0);  
    buttonMuonTra.place(x=50, y= 275, height = 30) 

    buttonBaoCao = Button(Root, text = "Báo cáo", bg = '#0063a1', fg = "white", font =("Poppins", 20), borderwidth=0, highlightthickness=0); 
    buttonBaoCao.place(x=60, y=400, height = 30)

    ig_Them = Xuly_Anh(PathOfFile + "/Image/"+'buttonThem.png', 60, 60)
    buttonThem = Button(Root, image=ig_Them, borderwidth=0, highlightthickness=0); 
        #command = lambda : Add_reader(Root, root), borderwidth=0, highlightthickness=0); 
    buttonThem.place(x=770, y=10)

    ig_Sua = Xuly_Anh(PathOfFile + "/Image/"+'buttonSua.png', 60, 60)
    buttonSua = Button(Root, image=ig_Sua, borderwidth=0, highlightthickness=0); 
        #command = lambda : Edit_reader(Root, root), borderwidth=0, highlightthickness=0); 
    buttonSua.place(x=870, y=10)

    ig_Xoa = Xuly_Anh(PathOfFile + "/Image/"+'buttonXoa.png', 60, 60)
    buttonXoa = Button(Root, image=ig_Xoa, borderwidth=0, highlightthickness=0); 
        #command = lambda : Del_reader(root), borderwidth=0, highlightthickness=0); 
    buttonXoa.place(x=970, y=10)

    for N in [buttonThem, buttonSua, buttonXoa, buttonBanDoc, buttonMuonTra, buttonBaoCao]:
        N.bind("<Enter>", on_enter)
        N.bind("<Leave>", on_leave)


    #columns = ('MaDocGia', 'HoTen', 'NgaySinh', 'GioiTinh', 'SoDienThoai', 'DiaChi', 'NgayTao', 'TongNo')
    label1 = Label(Root, text = "MĐG001", fg = '#0063a1', bg = "white", font=("Poppins", 10), borderwidth=0, highlightthickness=0)
    
    #move_widget_with_arrows(root, label1)
    # y += 44
    placeOfLabel = [[262, 138], [350, 138], [470, 138], [576, 138], [642, 138], [744, 138], [856, 138], [950, 138]]

    Reader = [('DG001', 'Keith Payne', '20/12/1955', 'Nam', '(700)620-8654', '663 Townsend Locks, Hollyport, NC 16205', '26/09/2023', 209871), ('DG002', 'Jennifer Cooper', '15/03/1993', 'Nam', '701.861.6156', '42996 Hall Pike Suite 119, West Debramouth, MN 89844', '22/12/2022', 300920), ('DG003', 'Casey Davis', '21/09/1940', 'Nam', '777.322.8705x276', '75024 Dean Expressway Apt. 086, Buckborough, WI 25604', '21/06/2022', 393005), ('DG004', 'Thomas Knight', '29/09/1953', 'Nam', '394-597-3065x811', '90838 Samantha Light Suite 419, Williamsborough, MI 02034', '10/12/2021', 17813), ('DG005', 'Jason Gonzalez', '20/08/1964', 'Nam', '983.603.9237x965', '448 Timothy Prairie Suite 304, Munozmouth, MH 93469', '07/09/2022', 67748), ('DG006', 'Francisco Nichols', '11/02/1952', 'Nữ', '752.906.7598', 'Unit 8471 Box 5584, DPO AP 58857', '27/03/2023', 114946), ('DG007', 'Christina Stokes', '20/10/1988', 'Nữ', '(599)656-8875', '1388 Williams Lock, Olsonshire, MA 36855', '11/06/2024', 425245), ('DG008', 'Paul Foster', '14/07/1942', 'Nữ', '908.649.5940x591', '1059 Nichole Burgs Apt. 705, Shawnbury, GU 99764', '12/06/2022', 402381), ('DG009', 'Sara Evans', '24/07/1939', 'Nữ', '001-462-557-9411', '286 Ethan Land Apt. 338, West Jennifer, OH 55795', '17/01/2021', 484993), ('DG010', 'Donald Myers', '13/01/1962', 'Nữ', '416-486-4815x903', '7808 Jay Canyon, East Kari, MA 68648', '23/07/2020', 410751), ('DG011', 'Stephanie Fernandez', '06/12/2003', 'Nam', '606-984-3670x401', '653 Connor Islands Suite 084, Rayfurt, GA 71550', '20/01/2020', 404637), ('DG012', 'Lisa Freeman', '14/10/1943', 'Nữ', '(813)348-4746x014', '5500 Ian Prairie Suite 519, Ericmouth, CO 29121', '25/07/2023', 351037), ('DG013', 'Rodney Horn', '07/06/1981', 'Nam', '(446)828-3146', 'Unit 3857 Box 9197, DPO AA 38753', '16/01/2021', 430707), ('DG014', 'Jonathan Palmer', '19/09/1964', 'Nữ', '5317523448', '03951 Douglas Isle, Vazquezfort, AZ 61519', '02/01/2024', 278536), ('DG015', 'Michael Bradley', '22/10/1947', 'Nam', '(656)990-1773', '08515 Johnson Unions, Marybury, MO 03628', '05/01/2021', 302857), ('DG016', 'Matthew Stevenson', '03/08/1946', 'Nữ', '762-446-3607x72467', '61005 King Ridges, Ortizton, RI 13622', '28/01/2023', 220774), ('DG017', 'Anna Coleman', '03/07/1940', 'Nữ', '8858364665', '47120 Young Burg, North Billyberg, GA 47105', '26/04/2021', 112494), ('DG018', 'Jill Romero', '21/02/1963', 'Nam', '001-325-987-5622x8571', '13761 Cameron Ranch, Noahton, NM 57307', '19/04/2022', 261933), ('DG019', 'Matthew Williams', '29/08/1976', 'Nam', '(826)570-5758x755', '4168 Patton Corners, Fullerstad, ME 88819', '30/07/2021', 52283), ('DG020', 'Nathan Jacobs', '23/12/1974', 'Nam', '+1-975-883-9438x829', '4790 Jeffrey Prairie Suite 185, Eileenland, RI 12192', '24/12/2020', 430823), ('DG021', 'Christopher Griffin', '22/09/1970', 'Nữ', '001-577-999-1041', '940 Anderson Turnpike Apt. 266, East Kimberlyborough, WV 57755', '28/05/2020', 120782), ('DG022', 'Kenneth Reynolds', '30/10/1961', 'Nam', '001-227-731-4224x79234', '82603 Delgado Lights, Davidborough, KS 49581', '29/10/2022', 369269), ('DG023', 'John Jenkins', '05/05/1979', 'Nam', '484.606.4808', '900 Christopher Route Suite 823, South Dorothyland, GA 68940', '04/06/2024', 250692), ('DG024', 'Dr. Brian Duncan', '05/05/2000', 'Nữ', '+1-739-710-2885x7773', '63952 Martin Track Suite 281, Perezchester, PW 12365', '08/07/2022', 353507), ('DG025', 'Elizabeth Romero', '22/03/1950', 'Nữ', '(378)406-5305', '62786 Evans Heights, Julieberg, AK 70951', '22/02/2023', 489377), ('DG026', 'Mark Harrell', '17/04/1955', 'Nữ', '001-865-201-4085x4355', '679 Joshua Forges Suite 071, Brianview, TN 13654', '01/09/2020', 405123), ('DG027', 'Wendy Grant', '01/05/1939', 'Nam', '258.264.9080x379', '41769 Hawkins Fork, Joshuachester, WY 13637', '23/03/2023', 109191), ('DG028', 'Cody Johnson', '24/07/1973', 'Nữ', '+1-925-574-0217x56647', '33909 Jessica Camp, Jamesport, OK 68585', '13/09/2020', 168782), ('DG029', 'Jessica Ford', '05/11/1997', 'Nữ', '+1-368-656-1311', '863 Christopher Walk Apt. 623, Port Margaret, ME 50465', '30/12/2021', 66626), ('DG030', 'George Mendoza', '21/10/1962', 'Nữ', '(244)253-8831x6557', '799 Kyle Rest, New James, AR 70020', '07/10/2024', 415362), ('DG031', 'Leon Davis', '23/02/1944', 'Nam', '(791)287-0542x035', '683 Christopher Shoal, East John, GU 18987', '19/12/2021', 196513), ('DG032', 'Mrs. Leah Perkins', '12/11/1989', 'Nam', '5403545539', '64174 Allison Pine Suite 846, Michaelchester, GA 99801', '16/03/2020', 419696), ('DG033', 'Nicole Moore', '16/03/1999', 'Nam', '+1-569-509-8249x4584', '9083 Rebecca Crossroad Suite 379, South Chasetown, WA 29730', '07/09/2020', 340714), ('DG034', 'Amber Kane', '29/07/1998', 'Nữ', '298-913-5157x879', '7203 Michael Cliff, Brentburgh, NC 76006', '28/02/2023', 439596), ('DG035', 'Pamela Delacruz', '10/10/1956', 'Nam', '619.904.8473x985', '47042 Kyle Extension, East Nicolemouth, TX 30279', '27/08/2022', 236087), ('DG036', 'Gary Mann', '12/07/1979', 'Nam', '001-919-876-6695x169', '8724 Frank Point, New Brookeside, WI 07743', '07/02/2020', 429058), ('DG037', 'Sherry Young', '25/12/1974', 'Nữ', '+1-700-736-4267', '269 Briggs Villages, Holtton, PW 03201', '16/05/2023', 70708), ('DG038', 'Jasmin Smith', '01/07/1968', 'Nam', '001-299-653-5629x82874', '6777 Norton Avenue, Lake Jeremyfurt, AZ 73995', '26/04/2020', 455588), ('DG039', 'Tiffany Hughes', '23/07/1948', 'Nữ', '843-229-1615x5410', '09735 Baird Causeway Suite 209, Beltranland, VA 56695', '18/11/2022', 238878), ('DG040', 'Jesse Martinez', '19/10/1978', 'Nữ', '001-964-447-9333x200', '5704 Diana Junction Suite 224, Dawnport, PA 13538', '24/05/2020', 393747), ('DG041', 'Tracy Adams', '04/06/1964', 'Nam', '+1-437-941-1943x471', '1012 Scott Keys Suite 930, Port Franklinland, MT 45477', '03/07/2020', 20324), ('DG042', 'Shawn Allen', '19/02/1962', 'Nữ', '(783)241-2837x6202', '206 Carter Canyon Apt. 690, East Juliatown, NV 02625', '17/06/2021', 105339), ('DG043', 'Charles Jones', '21/06/1993', 'Nam', '+1-561-478-4935x6790', '812 Waller Rapids, Stephenstown, NV 16522', '13/10/2020', 68870), ('DG044', 'Larry Cooper', '22/12/1956', 'Nam', '945-771-9030', '403 Petty Manor Suite 302, Lake Theresa, AL 53083', '18/07/2020', 411422), ('DG045', 'Michael Moses', '25/12/1965', 'Nữ', '960-209-1722', '7392 Stephanie Heights Suite 461, Marquezside, OH 57549', '12/02/2022', 145816), ('DG046', 'Kimberly Dominguez', '30/06/2000', 'Nam', '6964110504', '1018 Kimberly Summit, Jayhaven, GA 97036', '13/05/2023', 491905), ('DG047', 'Joshua Meyer', '20/05/1983', 'Nữ', '001-498-474-3267x2571', '46322 Shaw Stravenue Apt. 341, New Arianaton, MH 97501', '18/03/2022', 412596), ('DG048', 'Sara Hunter', '29/05/1954', 'Nam', '+1-659-578-5046x09689', 'Unit 4993 Box 4357, DPO AE 18693', '13/05/2020', 461422), ('DG049', 'Joshua Anderson', '16/10/1991', 'Nam', '(749)407-8717x602', '15341 Mullins Lane Apt. 853, Davidstad, FL 69462', '04/07/2024', 385456), ('DG050', 'Christina Stephens', '14/11/1991', 'Nữ', '856.675.6983x1271', '78764 Monica Knolls, Port Joshuaview, HI 90744', '07/04/2024', 196988), ('DG051', 'Samantha Vargas', '13/01/1951', 'Nữ', '001-538-521-5724x781', '88779 Snow Turnpike Suite 747, Stokesport, MS 42975', '29/04/2021', 341220), ('DG052', 'David Bates', '09/01/1975', 'Nam', '355.871.5233x600', '179 Matthew Valley, Schwartzview, SD 82459', '06/05/2020', 252369), ('DG053', 'Dr. Logan Miller', '16/07/1961', 'Nam', '001-380-847-7322x235', '1708 Barker Way Apt. 167, Stevenberg, NM 38493', '28/01/2023', 238024), ('DG054', 'Selena Evans', '13/03/1941', 'Nam', '8368215448', '72056 Tiffany Roads, West Jennifer, OK 67088', '21/09/2020', 115912), ('DG055', 'Sandra Frederick', '29/10/1937', 'Nam', '(956)232-9676x487', '89075 Shelton Overpass Apt. 385, Wilsonberg, NY 00546', '29/03/2024', 248691), ('DG056', 'Tommy Anderson', '27/02/1978', 'Nam', '397-851-0871x7687', '743 Holmes Square Suite 579, New Susanstad, DE 65754', '24/05/2022', 468126), ('DG057', 'Jennifer Clarke', '25/05/1956', 'Nữ', '(406)946-8121x3263', '4073 Espinoza Crossroad Apt. 578, Port Kathryn, DC 61096', '13/02/2022', 304268), ('DG058', 'Elizabeth Contreras', '16/10/1968', 'Nữ', '(820)587-6787x2103', 'Unit 8445 Box 5077, DPO AP 44330', '01/10/2024', 38036), ('DG059', 'Virginia Adams', '01/09/1977', 'Nam', '972.243.0106x12951', '960 Smith Isle, Sarahbury, MO 19090', '20/10/2023', 208606), ('DG060', 'Eric Quinn', '13/07/1956', 'Nam', '834.711.7786', '423 Warner Valleys Suite 279, Wrighthaven, NH 03025', '23/03/2024', 44286), ('DG061', 'Ashley Brown', '30/11/1940', 'Nam', '2194294241', '904 Amanda Coves Suite 094, East Andrew, MP 58311', '15/06/2021', 111255), ('DG062', 'Kevin Proctor', '04/05/1936', 'Nữ', '479.832.0443', '38335 Tapia Path, East Joseph, WV 93102', '06/04/2024', 441287), ('DG063', 'Ashlee Haas', '14/08/1970', 'Nữ', '836-656-0454', '759 Anthony Mission, West Meganfort, PR 20113', '09/09/2020', 469846), ('DG064', 'Michelle Moran', '02/07/1962', 'Nam', '307-381-9187x97583', '1798 Alvarez Cape, Joanton, PA 74314', '03/03/2021', 279549), ('DG065', 'Chris Morton', '16/04/2002', 'Nữ', '(820)985-5951x706', '532 Emily Stravenue Suite 403, Deborahmouth, IN 44260', '05/09/2022', 184358), ('DG066', 'Colleen Christensen', '19/02/1957', 'Nữ', '+1-449-524-2379', '31615 Bryant Loaf Apt. 840, New Heatherhaven, WY 94417', '02/05/2024', 208882), ('DG067', 'Leah Wheeler', '22/08/1976', 'Nữ', '(698)436-1272', '321 Anne Causeway, West Carrieland, MH 46078', '21/12/2021', 223596), ('DG068', 'George Hoffman', '18/08/1998', 'Nam', '695-327-6487', '9283 Gonzalez Island, New Virginiamouth, NE 18677', '01/05/2022', 316412), ('DG069', 'Eric Pittman', '07/04/1998', 'Nữ', '+1-936-239-8031', '9577 Page Trafficway Apt. 096, Deleonberg, RI 58393', '10/03/2022', 339313), ('DG070', 'Leslie Ramos', '21/01/1977', 'Nam', '465.489.2901x2136', '23211 Best Plaza Apt. 555, Gabrielafurt, MD 43860', '03/07/2023', 267296), ('DG071', 'Elizabeth Harper', '17/01/1967', 'Nữ', '2684152352', '1514 Donald Lakes, Simsfurt, AZ 91119', '26/04/2021', 5534), ('DG072', 'Paul Blair', '15/10/1988', 'Nam', '(245)720-0854', '2724 Gomez Parkways Suite 492, Markchester, NV 08195', '12/06/2021', 395478), ('DG073', 'Jessica Robertson', '02/03/1939', 'Nữ', '001-594-351-4711', '43110 Jason Extensions, Victoriaside, AR 55670', '09/10/2024', 307758), ('DG074', 'Lisa Smith', '25/01/1944', 'Nữ', '460.969.8689x1272', '247 Fowler Throughway, Port Aprilville, ID 07702', '28/08/2021', 159238), ('DG075', 'Jessica Carter', '09/07/1958', 'Nữ', '857.778.5145x1849', '29210 Garcia Rapid, South Wendyborough, IA 67918', '11/05/2024', 497183), ('DG076', 'Stephen Rodgers', '04/09/1981', 'Nữ', '001-545-388-6220x5187', '1959 Calvin Knoll, Port Thomaston, NM 31796', '29/04/2021', 464936), ('DG077', 'Michael Moore', '23/07/1998', 'Nam', '(305)334-2781x4913', 'USS Robinson, FPO AP 53373', '31/03/2022', 267598), ('DG078', 'Erik Schroeder', '06/09/2002', 'Nam', '(697)411-1064x52762', '414 Wright Stream Suite 491, South Brittanyberg, IN 06274', '29/09/2022', 222671), ('DG079', 'Matthew Stone', '22/11/1955', 'Nam', '4875235180', '7606 Jennifer Landing, Tammyport, ID 42805', '06/07/2021', 88908), ('DG080', 'Claire Mckay', '11/12/2001', 'Nam', '658-218-9817', '1754 Crawford Haven, New Yvonne, TX 40868', '27/11/2021', 224434), ('DG081', 'Deborah Hawkins', '06/09/1994', 'Nữ', '834.420.5823', '9411 Gonzalez Cliffs, Guerreroton, SD 60121', '18/04/2023', 406605), ('DG082', 'Melissa Terry', '12/05/1979', 'Nữ', '691.894.8626x316', '694 Torres Vista, Glennmouth, NY 69706', '02/03/2021', 413937), ('DG083', 'Jacqueline Kramer', '25/09/1965', 'Nữ', '(633)762-5225', '09762 Leah Inlet, Brandiborough, MN 31738', '02/04/2024', 279763), ('DG084', 'Mary Campos', '03/07/1950', 'Nữ', '367-433-9713', '79720 Cox Causeway Suite 025, North Kristen, MS 41721', '23/03/2024', 322764), ('DG085', 'Patricia Sanchez', '14/10/1970', 'Nam', '694-841-3235', '21504 Javier Fall Apt. 521, Thomasshire, GA 13776', '24/04/2022', 76932), ('DG086', 'Emily Martin', '20/06/1934', 'Nam', '(343)365-9422x408', '918 Miller Shoal Suite 765, West Andrewside, SD 98781', '17/02/2020', 10987), ('DG087', 'Sandra Taylor', '03/10/1957', 'Nữ', '(324)695-3986', '92348 Lee Circle Suite 314, Seanbury, AZ 01669', '23/02/2024', 437080), ('DG088', 'Felicia Acosta', '05/10/1998', 'Nữ', '539-881-2475x2315', '2518 Pamela Union, Kellyton, OR 49330', '19/04/2021', 309171), ('DG089', 'Melanie Ramirez', '10/01/1970', 'Nữ', '450.803.7757x62308', '2219 Vincent Burgs Suite 803, Lake Andrewside, PR 72951', '02/07/2023', 57173), ('DG090', 'Tiffany Hensley', '23/11/1949', 'Nam', '203.950.4979', '4053 Campos Overpass, East Timothybury, CA 23470', '20/03/2020', 41703), ('DG091', 'Stephanie Leon', '07/12/1942', 'Nam', '688.545.8168x73255', '3759 Morales Place Suite 974, Lake Johnchester, WI 82127', '14/03/2022', 483986), ('DG092', 'Kaitlyn Mccormick', '21/11/1963', 'Nữ', '(921)581-6153x9979', '03264 Lowe Causeway Apt. 682, East Josephview, IA 58505', '22/09/2023', 14437), ('DG093', 'Megan Ramirez', '12/01/1997', 'Nữ', '303.434.8269x03903', '5262 Vazquez Mountains Suite 123, Lake Gloriamouth, VI 77558', '19/01/2022', 67614), ('DG094', 'Helen Day', '04/09/1945', 'Nam', '405-691-9781', '951 Terry Spur Suite 859, Thompsonville, TX 54115', '21/11/2023', 28039), ('DG095', 'Andrew Flores', '08/07/1944', 'Nữ', '(462)984-9169', '3814 Audrey Trafficway Suite 364, Port Justinstad, SD 12353', '24/03/2024', 491562), ('DG096', 'Ann Ramos', '01/06/1951', 'Nam', '001-972-793-3941x301', '30959 Rodriguez Lights, Port Robertstad, PW 04166', '23/04/2022', 346055), ('DG097', 'Dr. Janet Rodriguez MD', '20/11/2000', 'Nữ', '2799886098', '62853 Noah Locks, Mooreville, AR 65152', '17/01/2021', 303068), ('DG098', 'Michael Patterson', '13/01/1937', 'Nam', '+1-469-206-3424', '96601 Vincent Knolls, Claudiatown, CT 10832', '18/04/2023', 201658), ('DG099', 'Brenda Shea', '21/03/1946', 'Nam', '001-847-961-9963x27669', '9812 Christina Ridge, East Cynthiaborough, SD 11943', '30/08/2022', 79520), ('DG100', 'Cynthia Rogers', '20/01/1957', 'Nam', '5404374725', '1758 Taylor Courts Apt. 472, Rodriguezbury, MO 28586', '11/12/2020', 338224), ('DG101', 'John Turner', '23/02/1973', 'Nữ', '+1-556-496-0168x836', '182 Ward Corners Apt. 686, Lake Dianeton, OR 32602', '11/07/2021', 216701), ('DG102', 'Matthew Hansen', '17/03/2000', 'Nam', '+1-320-504-6704x660', '5041 Villegas Mountain Suite 879, Sheltonton, LA 72327', '30/09/2024', 481015), ('DG103', 'Carlos Maldonado', '18/07/1981', 'Nữ', '(780)983-8164x50239', '3981 Ross Alley Apt. 361, Burgessstad, SD 14712', '12/11/2020', 4941), ('DG104', 'Robert Soto', '20/09/1946', 'Nam', '602.780.3809x3752', '1453 Gomez Bypass, New Kimberlyville, NJ 62832', '16/12/2023', 283246), ('DG105', 'Rebecca Perez', '27/11/1999', 'Nữ', '230-468-1225', '54381 Lee Trace, Shelbyshire, GA 99921', '25/04/2022', 126764), ('DG106', 'Tracy Mcdonald', '10/03/1978', 'Nam', '562.364.6634x8084', '10033 Timothy Burgs, Carlsonbury, DE 56810', '22/03/2022', 432327), ('DG107', 'Jeremy Fernandez', '14/06/1945', 'Nam', '4222924929', '1348 Emily Path, Jennifershire, DE 37193', '08/08/2024', 78427), ('DG108', 'Misty Jackson', '24/05/2002', 'Nữ', '599-680-1673', 'Unit 6620 Box 5306, DPO AP 11534', '11/12/2020', 351063), ('DG109', 'Anne Russo', '23/01/1963', 'Nữ', '594.625.6450', '989 Morgan Valley Suite 172, Lake Edgar, WI 62453', '29/04/2024', 35891), ('DG110', 'Andrea Kelley', '08/05/1952', 'Nữ', '001-973-615-6076x6712', '64370 Brittany Well, East Ryanborough, TN 62731', '23/04/2023', 335824), ('DG111', 'Lisa Ross', '18/10/1935', 'Nam', '632-220-0230x3292', 'Unit 0160 Box 1407, DPO AP 20617', '28/09/2022', 14830), ('DG112', 'Kayla Martin', '27/03/1953', 'Nam', '5995426332', '688 Michael Stravenue, Lisachester, NV 88622', '19/01/2021', 67544), ('DG113', 'Charles Farmer', '01/11/1999', 'Nữ', '(492)544-0836', '85864 Phillips Gardens, Lake Nathanstad, CA 10354', '16/09/2023', 492202), ('DG114', 'Michael Newton', '23/04/2002', 'Nam', '(266)378-5390x381', '6776 Alyssa Freeway, East Richard, TX 31483', '12/04/2021', 45742), ('DG115', 'Charlene Pacheco', '23/10/1933', 'Nữ', '(430)610-6258x2610', '4147 Ryan Fort, Medinafort, WV 74040', '03/05/2021', 454599), ('DG116', 'Jason Rivera', '25/09/1960', 'Nữ', '778-832-9275', '44211 Smith Village, New Jenniferport, PA 69245', '04/04/2021', 8073), ('DG117', 'Calvin Wise', '28/07/1966', 'Nam', '001-695-820-9490', '73458 Perez Walk Apt. 319, North Laura, PA 43290', '17/02/2022', 102729), ('DG118', 'Dustin Johnson', '04/02/1939', 'Nữ', '+1-735-461-8555', '0377 Dawson Isle Apt. 777, Beverlyborough, TN 19819', '22/05/2020', 406439), ('DG119', 'Brian Goodman', '30/10/1981', 'Nữ', '704-948-9958x605', '927 Jessica Streets, South Jaimeview, RI 68607', '12/01/2023', 161623), ('DG120', 'Richard Blankenship', '23/03/1944', 'Nam', '+1-860-965-8289x78580', '351 Cox Lake, South Keithland, HI 96838', '22/08/2023', 143953), ('DG121', 'Misty Key', '05/06/1969', 'Nam', '332-409-0890x351', '75181 Derrick Plain Apt. 331, West Josephshire, HI 07318', '06/06/2022', 190022), ('DG122', 'Julie Calhoun', '22/05/1972', 'Nam', '238.241.1986', 'PSC 9768, Box 2099, APO AP 67256', '01/12/2022', 486623), ('DG123', 'Todd Waters', '06/05/1967', 'Nữ', '338.828.4978x1386', '22239 Brendan Loaf, East Rachel, NJ 61992', '05/06/2021', 473328), ('DG124', 'Jessica Gonzalez', '26/07/1952', 'Nam', '+1-955-355-7818x89717', '94402 Kelly Roads, Robinsonfort, PR 30339', '21/09/2023', 197022), ('DG125', 'Steven Gonzales', '02/04/1981', 'Nữ', '001-600-913-5713x581', '988 Lawson Cliff Apt. 483, Duranview, OK 12346', '02/09/2021', 299627), ('DG126', 'Gregory Nichols', '24/10/1943', 'Nữ', '492-400-9204', '778 David Oval Apt. 419, Victoriahaven, MT 26627', '09/12/2023', 284023), ('DG127', 'Jessica Johnson', '17/02/1970', 'Nữ', '8315153163', '8911 Holland Bridge, Carolynfort, MN 42823', '29/10/2021', 47417), ('DG128', 'Dennis Lopez', '13/09/1942', 'Nam', '397-387-2055', '90252 Miranda Harbors Suite 860, Martinezland, WI 47689', '17/01/2023', 440719), ('DG129', 'Bernard Goodwin', '10/12/1945', 'Nữ', '+1-702-892-0867x4340', '9475 Michael Fork Apt. 766, Joanneberg, UT 80601', '30/08/2024', 134199), ('DG130', 'Andrea Wood', '27/06/1962', 'Nữ', '+1-544-279-1306x27469', '1524 Felicia Estates, Port Dillonstad, MN 44359', '13/05/2020', 292897), ('DG131', 'Amanda Garcia', '01/06/1942', 'Nữ', '(756)211-6456x068', '7598 Sanchez Gateway, Carrieland, VA 34772', '19/01/2020', 271935), ('DG132', 'Gary Terry', '01/07/1939', 'Nữ', '(510)809-2565x7852', '283 Reyes Alley Apt. 411, New Darlenemouth, AK 09057', '01/06/2022', 393439), ('DG133', 'Robert Hernandez', '07/01/1992', 'Nữ', '758.508.4743x4997', '6965 Jones Throughway Apt. 112, Wyattside, MT 14149', '25/01/2023', 146225), ('DG134', 'Rachel Leonard', '20/02/1987', 'Nữ', '(216)526-8443', '4252 Paul Court Apt. 957, Jamiemouth, MH 63649', '16/08/2023', 321589), ('DG135', 'Mark Fox', '15/11/1971', 'Nữ', '694-307-5112x297', '75353 Harris Isle, Port Brandon, OR 73555', '02/09/2024', 348309), ('DG136', 'William Anderson', '16/05/1939', 'Nữ', '+1-689-760-3223x0333', '1216 Stephen Prairie, North Timothymouth, DE 04355', '12/02/2021', 360456), ('DG137', 'Shannon Rose', '29/07/1981', 'Nữ', '(386)953-0882x5965', '70552 Amy Parkways Apt. 281, Ruizburgh, MP 46849', '27/02/2021', 234302), ('DG138', 'Jeffery Hawkins', '28/04/1969', 'Nữ', '(658)311-1009x377', '06944 Keller Mount Apt. 072, New Autumn, MT 07339', '30/06/2024', 15860), ('DG139', 'Louis Fowler', '19/09/2005', 'Nữ', '258-234-8073x5937', '875 Thompson Loaf Suite 838, Port Kenneth, VI 14476', '24/12/2022', 338290), ('DG140', 'Michelle Garcia', '18/02/1973', 'Nữ', '7302572963', '332 Moore Cliffs Suite 568, New Kyleview, IL 35042', '08/08/2024', 400039), ('DG141', 'Douglas Woods', '25/10/1992', 'Nam', '+1-793-744-4736x4108', '283 Faith Hollow, North Matthewstad, KS 35453', '18/06/2024', 305365), ('DG142', 'Johnny Brown', '01/10/1984', 'Nữ', '(403)706-8765x304', '1115 Amanda Hollow, Port Williamview, SD 36179', '17/04/2021', 199669), ('DG143', 'Daniel Cox', '06/12/1986', 'Nam', '792.935.8299x53358', '105 Garcia Squares Suite 529, East Norman, VI 15702', '09/09/2024', 310198), ('DG144', 'Roberto Ewing', '24/04/1989', 'Nữ', '727.861.4269x2032', '606 Linda Loaf, North Justin, DE 98807', '02/10/2020', 292290), ('DG145', 'Sara Brown', '13/02/2000', 'Nam', '+1-632-447-8470x01054', '405 Crystal Meadows Suite 913, North Lori, LA 81195', '19/12/2022', 459104), ('DG146', 'Justin Howard', '30/01/1953', 'Nam', '440.517.2011', '69592 Hannah Road Suite 854, Jonesshire, AL 12209', '13/02/2022', 55655), ('DG147', 'Jessica Andrews', '17/05/1987', 'Nam', '9353909791', '18906 Morgan Prairie Apt. 092, Lake Barry, CT 75709', '09/12/2023', 55471), ('DG148', 'Tamara Reyes', '12/06/1994', 'Nam', '951.837.2779x977', '4852 Lisa Heights Suite 477, Tinaburgh, AK 46050', '23/07/2024', 315635), ('DG149', 'Emily Young', '13/07/1998', 'Nam', '599.687.2078x7326', '94835 Wood Center Apt. 830, Johnfurt, MH 44082', '31/10/2021', 312514), ('DG150', 'Kelly Jones', '11/03/1983', 'Nam', '280-219-3095', '13016 Elizabeth Corners Apt. 904, Lake Suzanne, NE 37238', '24/06/2020', 458449), ('DG151', 'Emily Becker', '18/12/1953', 'Nữ', '(573)404-6483x60011', '11888 Teresa Lock, Saraview, NV 15606', '17/05/2024', 425804), ('DG152', 'Christina Johnson', '21/07/1995', 'Nam', '001-324-883-8084x010', '908 Fox Glens Apt. 471, Davidborough, OK 04181', '30/03/2022', 209175), ('DG153', 'Matthew Mendoza', '03/11/1955', 'Nữ', '703.843.3511x52099', 'USS Ochoa, FPO AP 06809', '24/10/2021', 26065), ('DG154', 'John Powell', '25/08/1945', 'Nữ', '386-575-8963x8662', '385 Booth Inlet Apt. 096, Roweland, LA 09893', '16/08/2022', 356144), ('DG155', 'Kathy Clark', '20/02/1970', 'Nữ', '(796)694-0557x122', '65933 Wilson Prairie, Carrland, WI 11096', '23/03/2023', 243398), ('DG156', 'John Mckee', '05/07/1947', 'Nữ', '240-531-2756', '31741 Kevin Inlet Suite 625, East Melvin, IN 97950', '24/01/2022', 475970), ('DG157', 'Katherine Fletcher', '21/10/1979', 'Nữ', '276-402-9770x1740', '95198 Mercer Locks, Galvanview, MA 30852', '06/08/2022', 95564), ('DG158', 'Amanda Jackson', '18/04/1985', 'Nam', '+1-944-912-5671x0991', '49936 Mcdaniel Lodge, Heatherville, AL 75207', '17/04/2023', 391631), ('DG159', 'Shawn Jensen', '07/05/1973', 'Nam', '(432)652-8409', '25892 Kim Causeway, Samuelland, NV 35925', '11/02/2022', 327069), ('DG160', 'Aaron Miller', '22/07/1981', 'Nam', '366-641-8534', '64344 Jessica Grove Suite 334, South Heatherfort, VI 14961', '10/06/2021', 386455), ('DG161', 'Todd Stewart', '14/02/1999', 'Nữ', '693.752.1698x630', '80319 Nicholas Center, Port Amandatown, KS 18531', '27/11/2021', 485722), ('DG162', 'Thomas Gould', '21/02/1994', 'Nữ', '+1-688-399-6936x282', 'USCGC Hamilton, FPO AP 31779', '07/07/2024', 326027), ('DG163', 'Brenda James', '02/07/1967', 'Nữ', '2257780389', 'USCGC Khan, FPO AE 91569', '06/10/2023', 136256), ('DG164', 'Brian Rodriguez', '29/02/1948', 'Nam', '482-220-4156', '62064 Nguyen Field Apt. 016, Port Julia, NE 01870', '09/04/2023', 250178), ('DG165', 'Christina Hull', '09/05/1946', 'Nữ', '(765)484-5379', '889 Harris Valleys Suite 241, Rubenfurt, AL 01740', '22/04/2023', 422493), ('DG166', 'Jennifer Wood', '26/03/1970', 'Nam', '869-693-8557x15109', '8413 Christopher Shoals, West Ronaldton, MI 91312', '12/06/2023', 95194), ('DG167', 'Alex Johnson', '07/06/1997', 'Nam', '(752)228-0359x4283', '4564 Knight Fort, Port Monica, MS 86613', '25/08/2023', 19452), ('DG168', 'Joanne Mendoza', '17/02/1935', 'Nữ', '(708)410-0734', '807 Flores Center, Clarkborough, LA 92347', '31/05/2020', 455464), ('DG169', 'Kristin Raymond', '16/02/1969', 'Nữ', '+1-892-908-3048x467', '87128 Carlos Rest, Michaelfort, MN 37003', '01/04/2023', 49076), ('DG170', 'Michele Lam', '07/12/1934', 'Nam', '620.475.0502x8894', '081 Johnson Mountain, Lake William, CO 30399', '08/01/2022', 171448), ('DG171', 'Nancy Scott', '05/07/1997', 'Nam', '(904)924-6564x0654', '71383 Jefferson Forks, Josephberg, MS 92355', '10/08/2023', 39997), ('DG172', 'Marcus Drake', '24/05/1944', 'Nữ', '480.903.4758x11196', '64853 Dunn Crescent Apt. 324, Laurafurt, MD 29765', '28/04/2024', 230392), ('DG173', 'Tiffany Thomas', '07/08/1969', 'Nam', '+1-226-990-1211x9706', '86977 Ross Heights, Port Beth, ID 38235', '17/07/2021', 185374), ('DG174', 'Jason Jordan', '10/04/1936', 'Nữ', '001-978-484-5283x383', '933 Jennings Rapids, Kevinhaven, NV 55160', '11/10/2022', 53907), ('DG175', 'Brenda Hull', '30/09/1993', 'Nam', '336.418.4564x1864', 'Unit 7062 Box 5961, DPO AE 81353', '26/05/2022', 369270), ('DG176', 'Jeremy Hancock', '27/03/1979', 'Nữ', '(933)979-2374x710', '3708 Powers Junctions, East Tyler, CO 83589', '30/08/2020', 498373), ('DG177', 'Chad West', '09/07/1935', 'Nữ', '(272)914-1574', '3833 Richardson Island, Millerfurt, KS 27606', '15/12/2020', 29295), ('DG178', 'Melissa Tran', '25/08/1979', 'Nam', '750-815-3013', '99573 Stephanie Mills, Brendashire, UT 03283', '06/09/2022', 430517), ('DG179', 'Debra Gonzalez', '30/07/1955', 'Nam', '+1-682-333-8760x7344', 'PSC 6565, Box 0284, APO AA 65977', '25/05/2020', 122570), ('DG180', 'Neil Mcbride', '22/04/1967', 'Nam', '(805)941-5852x082', '55114 Ashley Lock Apt. 918, Jamesport, HI 01403', '11/06/2020', 215494), ('DG181', 'Dr. Gregory Patterson IV', '03/01/1966', 'Nam', '001-365-484-0005x13504', '381 Jacqueline Burg Apt. 793, Lindafurt, ID 68386', '27/03/2023', 228195), ('DG182', 'Alyssa Robinson', '01/09/1938', 'Nam', '506.798.5360', '0418 Martinez Hills, Barnesburgh, KY 72724', '08/10/2023', 431770), ('DG183', 'Gwendolyn Grant', '26/02/1952', 'Nữ', '716-369-2666x6988', '09582 Michael Hill Apt. 645, Rogerstown, MD 84340', '26/07/2023', 223621), ('DG184', 'Sean Estrada', '23/06/1964', 'Nam', '(825)249-4757', '0133 Pamela Stravenue Suite 014, New Stacey, SC 47783', '23/06/2020', 325337), ('DG185', 'Francisco Young', '12/12/2000', 'Nữ', '001-976-360-8063', '06946 Holmes Row, Lake Benjamin, NC 97432', '06/10/2022', 425215), ('DG186', 'Lauren Mason', '08/02/1940', 'Nam', '662-341-9908x3470', 'USNV Patterson, FPO AA 43774', '15/07/2021', 180131), ('DG187', 'Brandon Mahoney', '17/03/1962', 'Nữ', '(967)579-3687', '9006 Mack Summit, South Shannon, VA 57106', '04/12/2022', 282462), ('DG188', 'Michelle Montgomery', '18/03/1990', 'Nữ', '(585)522-3356', '572 Jenna Views, North Kristiberg, OR 17274', '16/09/2023', 247270), ('DG189', 'Christina Haas', '30/04/1978', 'Nam', '946.779.5139', '668 Garza Well Apt. 735, Allisonport, AS 88117', '13/06/2024', 190898), ('DG190', 'Robert Tanner', '03/05/1998', 'Nữ', '(718)647-9473x4750', '8212 Daniel Shoal Apt. 362, Port Edward, NM 86035', '07/11/2022', 262085), ('DG191', 'Gene Peterson', '20/09/2004', 'Nữ', '9662739875', '3292 Watson Shoal, Lake Angie, MS 52894', '22/07/2022', 360941), ('DG192', 'Sarah Mckinney', '13/09/1945', 'Nữ', '(246)234-3186', '94155 Kylie Shores Apt. 505, Rachelhaven, VI 57250', '13/05/2023', 375525), ('DG193', 'David Valdez', '31/05/1994', 'Nam', '001-716-865-4094x24193', '66995 Anthony Expressway, New Matthewberg, NJ 01627', '12/05/2021', 4382), ('DG194', 'Rachel Landry', '15/08/1935', 'Nữ', '+1-560-799-2374x95776', '64008 Michele Estates, Sarahland, SC 48093', '22/07/2020', 82487), ('DG195', 'Sarah Romero', '23/11/1975', 'Nam', '355.962.2761x11269', '95050 Sara Mount Suite 039, North Joseph, WA 35042', '26/08/2021', 271216), ('DG196', 'Darren Gordon', '30/12/1957', 'Nam', '+1-537-364-1422x45098', '83215 Debbie Passage, West Philip, CT 08420', '16/04/2024', 445609), ('DG197', 'Kevin Manning', '15/10/1945', 'Nữ', '210-403-5845', '49336 Johnson Camp, South Kevinmouth, ID 49168', '22/11/2023', 262778), ('DG198', 'Russell Vargas', '12/02/1944', 'Nam', '5086940229', '281 Gonzales Drive Apt. 470, New Antonio, IL 77663', '16/05/2021', 117053), ('DG199', 'Alexander Griffin', '04/06/1955', 'Nam', '2514893224', '724 Soto View Suite 058, Lake Paul, KY 16991', '29/11/2023', 52011), ('DG200', 'David Adams', '30/11/1982', 'Nam', '+1-985-540-0310', '2529 Everett Groves Apt. 063, East Jonathanville, NH 87080', '27/11/2020', 485676)]
    print(len(Reader))
    # Tạo các label cố định cho danh sách
    list_of_labels = []
    for i in range(9): 
        labels = [tk.Label(Root, font=("Arial", 10), bg="white") for _ in range(8)]
        for j, label in enumerate(labels):
            label.place(x=placeOfLabel[j][0], y=138 + i * 44)
        list_of_labels.append(labels)

    # Tính năng cuộn
    global scroll_index
    scroll_index = 0  # Để lưu chỉ số của sách hiện tại

    # Hàm cập nhật label
    def update_labels():
        for i in range(9):  
            if scroll_index + i < len(Reader):
                for j, data in enumerate(Reader[scroll_index + i]):
                    list_of_labels[i][j].config(text=data) 
            else:
                for j in range(9):
                    list_of_labels[i][j].config(text="") 

    def mouse_scroll(event):
        global scroll_index
        if event.delta > 0:  # Cuộn lên
            scroll_index = max(scroll_index - 1, 0)
        elif event.delta < 0:  # Cuộn xuống
            scroll_index = min(scroll_index + 1, len(Reader) - 9)

        update_labels()  # Cập nhật nội dung của các label
    
    def scroll_up(event):
        global scroll_index
        scroll_index = max(scroll_index - 50, 0)  # Nhảy 50 cuốn sách lên
        update_labels()

    def scroll_down(event):
        global scroll_index
        scroll_index = min(scroll_index + 50, len(Reader) - 9)  # Nhảy 50 cuốn sách xuống
        update_labels()

    update_labels()

    # Liên kết sự kiện cuộn chuột
    root.bind("<MouseWheel>", mouse_scroll)
    # Liên kết phím tắt Ctrl + mũi tên chỉ lên và xuống
    root.bind("<Control-Up>", scroll_up)
    root.bind("<Control-Down>", scroll_down)
    root.update_idletasks()
    root.mainloop()