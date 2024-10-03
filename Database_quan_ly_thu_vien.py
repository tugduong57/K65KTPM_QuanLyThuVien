import pyodbc

# Thông tin kết nối
driver = 'ODBC Driver 17 for SQL Server'  # Hoặc 'ODBC Driver 18 for SQL Server'
server = r'NGOCLUONG\SQLEXPRESS'

username = 'quanlythuvien'
password = '123'

# Chuỗi kết nối
conn_string = f'DRIVER={{{driver}}};SERVER={server};UID={username};PWD={password}'


# Kết nối đến SQL Server
conn = pyodbc.connect(conn_string, autocommit=True)


# Tạo con trỏ để thực hiện các câu lệnh SQL
cursor = conn.cursor()

# Tạo database
database_name = 'Quan_Ly_Thu_Vien'

create_db = f''' 
	IF NOT EXISTS (
    	SELECT name 
   		FROM sys.databases 
   		WHERE name = '{database_name}'
	)
	BEGIN 
   		CREATE DATABASE {database_name}; 
	END
'''

cursor.execute(create_db)

# Sử dụng cơ sở dữ liệu Quan_Ly_Thu_Vien
use_db = f'USE {database_name}'
cursor.execute(use_db)

# Tạo bảng admin
create_admin = '''
	if not exists ( select * from sysobjects where name = 'admin' and xtype = 'U')
	begin
		create table admin (
			tai_khoan varchar(20) not null primary key,
			mat_khau varchar(20) not null
		)
	end
'''

cursor.execute(create_admin)

# Tạo bảng sách
create_sach = '''
	if not exists ( select * from sysobjects where name = 'sach' and xtype = 'U')
	begin
		create table sach (
			ma_sach char(20) not null primary key,
			ten_sach nchar(30),
			the_loai nchar(20),
			ngay_xuat_ban date,
			nha_xuat_ban nchar(30),
			tac_gia nchar(30),
			gia_sach int,
			tong_so_luong int
		)
	end
'''

cursor.execute(create_sach)

# Tạo bảng độc giả
create_doc_gia = '''
	if not exists ( select * from sysobjects where name = 'doc_gia' and xtype = 'U')
	begin
		create table doc_gia (
			ma_doc_gia char(20) not null primary key,
			ho_ten nchar(30),
			so_DT varchar(15),
			trang_thai nchar(30)
		)
	end
'''

cursor.execute(create_doc_gia)

# Tạo bảng phiếu mượn
create_phieu_muon = '''
	if not exists ( select * from sysobjects where name = 'phieu_muon' and xtype = 'U')
	begin
		create table phieu_muon (
			ma_phieu char(20) not null primary key,
			ma_doc_gia char(20),
			ngay_muon date,
			han_tra_sach date,
			ma_sach char(20),
			foreign key (ma_sach) references sach(ma_sach),
			foreign key (ma_doc_gia) references doc_gia(ma_doc_gia)
		)
	end
'''

cursor.execute(create_phieu_muon)

# Tạo bảng danh sách mượn
create_DS_muon = '''
	if not exists ( select * from sysobjects where name = 'danh_sach_muon' and xtype = 'U')
	begin
		create table danh_sach_muon (
			ma_phieu char(20) not null,
			ma_sach char(20) not null,
			primary key (ma_phieu, ma_sach),
			foreign key (ma_phieu) references phieu_muon(ma_phieu)
		)
	end
'''

cursor.execute(create_DS_muon)




############################### INSERT ###############################
### thêm giá trị cho bảng admin
tai_khoan = input("TK : ")
mat_khau = input("MK : ")
insert_admin = f'''
	insert into admin values ('{tai_khoan}', '{mat_khau}')
'''

cursor.execute(insert_admin)

# ##### thêm giá trị cho bảng sách
# ma_sach =  input("Ma sach : ")
# ten_sach = input("Ten sach : ")
# the_loai = input("The loai : ")
# ngay_xuat_ban = input("Ngay xuat ban : ")
# nha_xuat_ban = input("Nha xuat ban : ")
# tac_gia = input("Tac gia : ")
# gia_sach = int(input("Gia sach : "))
# tong_so_luong = int(input("tong_so_luong : "))

# insert_sach = f'''
# 	insert into sach 
# 	values ('{ma_sach}', N'{ten_sach}', N'{the_loai}', '{ngay_xuat_ban}', N'{nha_xuat_ban}', N'{tac_gia}', '{gia_sach}', '{tong_so_luong}')
# '''

# cursor.execute(insert_sach)
# #### thêm giá trị cho bảng độc giả
# ma_doc_gia = input("ma_doc_gia : ")
# ho_ten = input("ho_ten : ")
# so_DT = input("so_DT : ")
# trang_thai = input("trang_thai : ")

# insert_doc_gia = f'''
# 	insert into doc_gia 
# 	values ('{ma_doc_gia}', N'{ho_ten}', '{so_DT}', N'{trang_thai}')
# '''

# cursor.execute(insert_doc_gia)


# #### thêm giá trị cho bảng phiếu mượn
# ma_phieu = input("ma_phieu : ")
# ma_doc_gia = input("ma_doc_gia : ")
# ngay_muon = input("ngay_muon : ")
# han_tra_sach = input("han_tra_sach : ")
# ma_sach = input("ma_sach : ")

# insert_phieu_muon = f'''
# 	insert into phieu_muon 
# 	values ('{ma_phieu}', '{ma_doc_gia}', '{ngay_muon}', '{han_tra_sach}', '{ma_sach}')
# '''

# cursor.execute(insert_phieu_muon)

# #### thêm giá trị cho bảng danh sách mượn
# ma_phieu = input("ma_phieu : ")
# ma_sach = input("ma_sach : ")

# insert_DS_muon = f'''
# 	insert into danh_sach_muon
# 	values ('{ma_phieu}', '{ma_sach}')
# '''

# cursor.execute(insert_DS_muon)


############################### DELETE ###############################

# delete_ban_ghi = '''
# 	delete from <table_name> 
# 	where <----> 
# '''

# cursor.execute(delete_ban_ghi)

############################### UPDATE ###############################

# update_ban_ghi = '''
# 	update <table_name> set <---------> where <------>
# '''
# cursor.execute(update_ban_ghi)

############################### SELECT ###############################

# ma_doc_gia = input("ma_doc_gia : ")




# Đóng kết nối
conn.close()
print()