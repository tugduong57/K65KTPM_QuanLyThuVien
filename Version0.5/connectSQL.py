# First: Create/Connect database 
import pyodbc
def C_database():
	conn_string = (
	    "DRIVER={ODBC Driver 17 for SQL Server};"
	    "SERVER=localhost;"  		# hoặc tên máy chủ 
	    "DATABASE=master;"  
	    "Trusted_Connection=yes;"  	# Sử dụng Windows Authentication
	)

	conn = pyodbc.connect(conn_string, autocommit=True)	# Kết nối đến SQL Server
	cursor = conn.cursor()								# Tạo con trỏ để thực hiện các câu lệnh SQL

	database_name = 'Quan_Ly_Thu_Vien'			# Tạo database

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

	# Đóng kết nối
	cursor.close()
	conn.close()

	print("Kết nối thành công")

