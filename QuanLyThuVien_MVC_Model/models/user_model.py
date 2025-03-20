import pyodbc

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
	# Đóng kết nối
	cursor.close()
	conn.close()
	if res :
		return True
	else :
		return False

# Check đăng kí
def check_sign_up_model(username) :

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

