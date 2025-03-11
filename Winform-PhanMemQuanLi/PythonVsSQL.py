import pyodbc
def C_database():
	conn_string = (
	    "DRIVER={ODBC Driver 17 for SQL Server};"
	    "SERVER=localhost;"  		
	    "DATABASE=master;"  
	    "Trusted_Connection=yes;"  	
	)

	conn = pyodbc.connect(conn_string, autocommit=True)	

	# Tạo con trỏ để thực hiện các câu lệnh SQL
	cursor = conn.cursor()								

	database_name = 'dataForProject'			

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

	# Sử dụng cơ sở dữ liệu vừa tạo
	use_db = f'USE {database_name}'
	cursor.execute(use_db)

	# Tạo bảng Sản Phẩm
	create_SanPham = '''
		if not exists ( select * from sysobjects where name = 'SanPham' and xtype = 'U')
		begin
			create table SanPham (
				[Mã sản phẩm] varchar(10) not null primary key,
				[Tên sản phẩm] nvarchar(MAX) not null,
				Hãng nvarchar(10) not null,
				[Phân loại] nvarchar(20) not null,
				[Đơn vị tính] nvarchar(10) not null,
				[Số lượng] smallint not null,
				[Giá nhập trung bình] decimal(18,2) not null,
				[Đơn giá] decimal(18,2) not null,
				[Ghi chú] nvarchar(MAX)
			)
		end
	'''

	cursor.execute(create_SanPham)

	# Tạo bảng Đối tác
	create_DoiTac = '''
		if not exists ( select * from sysobjects where name = 'DoiTac' and xtype = 'U')
		begin
			create table DoiTac (
				[Mã đối tác] varchar(10) not null primary key,
				[Tên đối tác] nvarchar(MAX) not null,
				Tuổi tinyint not null,
				[Địa chỉ] nvarchar(MAX) not null,
				[Số điện thoại] varchar(12) not null,
				[Ghi chú] nvarchar(MAX)
			)
		end
	'''

	cursor.execute(create_DoiTac)

	# Tạo bảng Người dùng
	create_NguoiDung = '''
		if not exists ( select * from sysobjects where name = 'NguoiDung' and xtype = 'U')
		begin
			create table NguoiDung (
				[Tài khoản] varchar(20) not null primary key,
				[Mật khẩu] nvarchar(15) not null,
				[Tên người dùng] nvarchar(20),
				[Ghi chú] nvarchar(MAX)
			)
		end
	'''

	cursor.execute(create_NguoiDung)

	# Tạo bảng Hóa đơn
	create_HoaDon = '''
		if not exists ( select * from sysobjects where name = 'HoaDon' and xtype = 'U')
		begin
			create table HoaDon (
				[Mã hóa đơn] varchar(10) not null primary key,
				[Mã đối tác] varchar(10) not null,
				[Mã người bán] varchar(20) not null,
				[Ngày tạo] datetime not null,
				[Loại hóa đơn] nvarchar(5) not null,
				[Tổng tiền] decimal(18,2) not null,
				[Ghi chú] nvarchar(MAX),
				CONSTRAINT FK_HoaDon_DoiTac FOREIGN KEY ([Mã đối tác])
					REFERENCES DoiTac([Mã đối tác]) ON DELETE CASCADE,
				CONSTRAINT FK_HoaDon_NguoiDung FOREIGN KEY ([Mã người bán])
					REFERENCES NguoiDung([Tài khoản]) ON DELETE CASCADE
			)
		end
	'''

	cursor.execute(create_HoaDon)

	'''
		Foregin key: Rằng buộc khóa ngoại, ON Delete cascde: xóa các dòng khóa ngoại khi thông tin gốc bị xóa
		ON Update Cascade: cập nhật khi mã References cập nhật ?
	'''

	# Tạo bảng Chi tiết Hóa đơn
	create_ChiTietHoaDon = '''
		if not exists ( select * from sysobjects where name = 'ChiTietHoaDon' and xtype = 'U')
		begin
			create table ChiTietHoaDon (
				[Mã hóa đơn] varchar(10) not null,
				[Mã sản phẩm] varchar(10) not null,
				[Số lượng] smallint not null,
				[Đơn giá] decimal(18,2) not null,
				PRIMARY KEY ([Mã hóa đơn], [Mã sản phẩm]),
				CONSTRAINT FK_ChiTietHoaDon_HoaDon FOREIGN KEY ([Mã hóa đơn])
					REFERENCES HoaDon([Mã hóa đơn]) ON DELETE CASCADE,
				CONSTRAINT FK_ChiTietHoaDon_SanPham FOREIGN KEY ([Mã sản phẩm])
					REFERENCES SanPham([Mã sản phẩm]) ON DELETE CASCADE
			)
		end
	'''

	cursor.execute(create_ChiTietHoaDon)

	print("Done!")

	cursor.close()

def Delete_database():
    conn_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"  		
        "DATABASE=master;"  
        "Trusted_Connection=yes;"  	
    )

    conn = pyodbc.connect(conn_string, autocommit=True)	
    cursor = conn.cursor()								

    database_name = 'dataForProject'

    # Kiểm tra xem database có tồn tại không, nếu có thì xóa
    drop_db_query = f'''
        IF EXISTS (SELECT * FROM sys.databases WHERE name = '{database_name}')
        BEGIN
            ALTER DATABASE [{database_name}] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
            DROP DATABASE [{database_name}];
        END
    '''
    
    try:
        cursor.execute(drop_db_query)
        print(f"Database '{database_name}' đã bị xóa thành công!")
    except Exception as e:
        print(f"Lỗi khi xóa database: {e}")

    cursor.close()
    conn.close()


# Tạo database
C_database()

# Xóa database
# Delete_database()






