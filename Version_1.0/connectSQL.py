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
				so_DT varchar(15),
				trang_thai nvarchar(30)
			)
		end
	'''

	cursor.execute(create_doc_gia)


# Check đăng nhập
def check_sign_in(username, password_input) :

	conn_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=Quan_Ly_Thu_Vien;"  # Kết nối với database đã tạo
        "Trusted_Connection=yes;"
    )
	conn = pyodbc.connect(conn_string, autocommit=True)	# Kết nối đến SQL Server
	cursor = conn.cursor()				# Tạo con trỏ để thực hiện các câu lệnh SQL

	query = f"SELECT tai_khoan, mat_khau FROM admin WHERE tai_khoan = '{username}' AND mat_khau = '{password_input}'"
	cursor.execute(query)
	res = cursor.fetchone()
	if res :
		return True
	else :
		return False


	# Đóng kết nối
	cursor.close()
	conn.close()

# Check đăng kí
def check_sign_up(username) :

	conn_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=Quan_Ly_Thu_Vien;"  # Kết nối với database đã tạo
        "Trusted_Connection=yes;"
    )
	conn = pyodbc.connect(conn_string, autocommit=True)	# Kết nối đến SQL Server
	cursor = conn.cursor()				# Tạo con trỏ để thực hiện các câu lệnh SQL

	query = f"SELECT tai_khoan, mat_khau FROM admin WHERE tai_khoan = '{username}'"
	cursor.execute(query)
	res = cursor.fetchone()
	if res :
		return True
	else :
		return False


	# Đóng kết nối
	cursor.close()
	conn.close()

# Thêm giá trị vào bảng Admin
def Insert_admin(tai_khoan, mat_khau) :
	conn_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=Quan_Ly_Thu_Vien;"  # Kết nối với database đã tạo
        "Trusted_Connection=yes;"
    )

	conn = pyodbc.connect(conn_string, autocommit=True)	# Kết nối đến SQL Server
	cursor = conn.cursor()				# Tạo con trỏ để thực hiện các câu lệnh SQL

	insert_values = f'''
		insert into admin (tai_khoan, mat_khau)
		values ('{tai_khoan}', '{mat_khau}');
	'''
	cursor.execute(insert_values)

	# Đóng kết nối
	cursor.close()
	conn.close()
	print(f"Đã chèn tài khoản {tai_khoan} thành công!")



# Thêm giá trị vào bảng sach
def Insert_sach(ma_sach, ten_sach, the_loai, tac_gia, nha_xuat_ban, ngay_xuat_ban, tong_so_luong, gia_sach) :
	conn_string = (
	    "DRIVER={ODBC Driver 17 for SQL Server};"
	    "SERVER=localhost;"
	    "DATABASE=Quan_Ly_Thu_Vien;"  # Kết nối với database đã tạo
	    "Trusted_Connection=yes;"
	)

	conn = pyodbc.connect(conn_string, autocommit=True)	# Kết nối đến SQL Server
	cursor = conn.cursor()								# Tạo con trỏ để thực hiện các câu lệnh SQL

	insert_values = f'''
		insert into sach (ma_sach, ten_sach, the_loai, tac_gia, nha_xuat_ban, ngay_xuat_ban, tong_so_luong, gia_sach)
		values ('{ma_sach}', N'{ten_sach}', N'{the_loai}', N'{tac_gia}', N'{nha_xuat_ban}', N'{ngay_xuat_ban}', {tong_so_luong}, {gia_sach});
	'''

	cursor.execute(insert_values)
	# Đóng kết nối
	cursor.close()
	conn.close()

def update_sach(ma_sach, ten_sach, the_loai, tac_gia, nha_xuat_ban, ngay_xuat_ban, tong_so_luong,   gia_sach ) :
	conn_string = (
	    "DRIVER={ODBC Driver 17 for SQL Server};"
	    "SERVER=localhost;"
	    "DATABASE=Quan_Ly_Thu_Vien;"  # Kết nối với database đã tạo
	    "Trusted_Connection=yes;"
	)

	conn = pyodbc.connect(conn_string, autocommit=True)	# Kết nối đến SQL Server
	cursor = conn.cursor()								# Tạo con trỏ để thực hiện các câu lệnh SQL

	print(189, ma_sach, ten_sach, the_loai, tac_gia, nha_xuat_ban, ngay_xuat_ban, tong_so_luong,   gia_sach)
	update_query = f'''
	    UPDATE sach 
	    SET ten_sach = N'{ten_sach}', the_loai = N'{the_loai}', tac_gia = N'{tac_gia}', nha_xuat_ban = N'{nha_xuat_ban}', ngay_xuat_ban = N'{ngay_xuat_ban}', tong_so_luong = {tong_so_luong}, gia_sach = {gia_sach}
	    WHERE ma_sach = '{ma_sach}'
    '''
	cursor.execute(update_query)
	# Đóng kết nối
	cursor.close()
	conn.close()

def delete_sach(ma_sach) :
	conn_string = (
	    "DRIVER={ODBC Driver 17 for SQL Server};"
	    "SERVER=localhost;"
	    "DATABASE=Quan_Ly_Thu_Vien;"  # Kết nối với database đã tạo
	    "Trusted_Connection=yes;"
	)

	conn = pyodbc.connect(conn_string, autocommit=True)	# Kết nối đến SQL Server
	cursor = conn.cursor()								# Tạo con trỏ để thực hiện các câu lệnh SQL

	query = f'''
		DELETE FROM sach WHERE ma_sach = '{ma_sach}'
	'''

	cursor.execute(query)
	# Đóng kết nối
	cursor.close()
	conn.close()


# Tìm kiếm
def find_sach(ma_timkiem, value) :
	conn_string = (
		"DRIVER={ODBC Driver 17 for SQL Server};"
		"SERVER=localhost;"
		"DATABASE=Quan_Ly_Thu_Vien;"  # Kết nối với database đã tạo
		"Trusted_Connection=yes;"
	)

	conn = pyodbc.connect(conn_string, autocommit=True)	# Kết nối đến SQL Server
	cursor = conn.cursor()								# Tạo con trỏ để thực hiện các câu lệnh SQL


	if ma_timkiem == "Mã sách":
	    query = f"SELECT ma_sach, ten_sach, the_loai, tac_gia, nha_xuat_ban, ngay_xuat_ban, tong_so_luong, gia_sach FROM sach WHERE ma_sach = '{value}'"
	elif ma_timkiem == "Tên sách":
	    query = f"SELECT * FROM sach WHERE ten_sach LIKE N'%{value}%'"
	elif ma_timkiem == "Thể loại":
	    query = f"SELECT * FROM sach WHERE the_loai LIKE N'%{value}%'"
	elif ma_timkiem == "Tên tác giả":
	    query = f"SELECT * FROM sach WHERE tac_gia LIKE N'%{value}%'"

	cursor.execute(query)
	book = cursor.fetchall()
	print(244, book)

	# Đóng kết nối
	cursor.close()
	conn.close()

	return book

def show_sach() :
	conn_string = (
		"DRIVER={ODBC Driver 17 for SQL Server};"
		"SERVER=localhost;"
		"DATABASE=Quan_Ly_Thu_Vien;"  # Kết nối với database đã tạo
		"Trusted_Connection=yes;"
	)

	conn = pyodbc.connect(conn_string, autocommit=True)	# Kết nối đến SQL Server
	cursor = conn.cursor()								# Tạo con trỏ để thực hiện các câu lệnh SQL

	query = f"SELECT ma_sach, ten_sach, the_loai, tac_gia, nha_xuat_ban, ngay_xuat_ban, tong_so_luong, gia_sach FROM sach "
	
	cursor.execute(query)
	book = cursor.fetchall()

	# Đóng kết nối
	cursor.close()
	conn.close()

	return book