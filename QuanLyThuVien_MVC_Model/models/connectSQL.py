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
				ma_sach char(4) not null primary key,
				ten_sach nvarchar(30),
				the_loai nvarchar(20),
				tac_gia nvarchar(30),
				nha_xuat_ban nvarchar(30),
				ngay_xuat_ban nvarchar(12),
				tong_so_luong int,
				gia_sach int
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
				ho_ten nvarchar(30),
				ngay_sinh nvarchar(30),
				gioi_tinh nvarchar(30),
				so_dien_thoai varchar(15),
				dia_chi nvarchar(30),
				ngay_tao nvarchar(30),
				trang_thai nvarchar(30)
			)
		end
	'''

	cursor.execute(create_doc_gia)

	# Tạo bảng độc giả
	create_phieu_muon = '''
		if not exists ( select * from sysobjects where name = 'phieu_muon' and xtype = 'U')
		begin
			create table phieu_muon(
				ma_phieu_muon char(20) not null primary key,
				ma_doc_gia nvarchar(30),
				ngay_muon nvarchar(30),
				han_tra_sach nvarchar(30),
				thu_thu_da_Tao nvarchar(30)
			)
		end
	'''

	cursor.execute(create_phieu_muon)

	# Tạo bảng độc giả
	create_danh_sach_muon = '''
		if not exists ( select * from sysobjects where name = 'danh_sach_muon' and xtype = 'U')
		begin
			create table danh_sach_muon(
				ma_phieu_muon char(20) not null primary key,
				ma_sach nvarchar(30)
			)
		end
	'''

	cursor.execute(create_danh_sach_muon)
