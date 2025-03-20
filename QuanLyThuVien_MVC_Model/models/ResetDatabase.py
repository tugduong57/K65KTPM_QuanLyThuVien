import pyodbc

def delete_database(database_name):
    try:
        # Chuỗi kết nối đến cơ sở dữ liệu master để xóa database
        conn_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"      # Đổi 'localhost' thành tên máy chủ SQL Server của bạn nếu cần
            "DATABASE=master;"        # Kết nối tới database master
            "Trusted_Connection=yes;" # Sử dụng Windows Authentication
        )
        
        # Kết nối tới SQL Server, tắt autocommit để tránh vấn đề giao dịch
        conn = pyodbc.connect(conn_string, autocommit=True)
        cursor = conn.cursor()

        # Lệnh SQL để xóa cơ sở dữ liệu
        drop_db_query = f"DROP DATABASE IF EXISTS {database_name};"

        # Thực thi lệnh xóa cơ sở dữ liệu
        cursor.execute(drop_db_query)

        print(f"Cơ sở dữ liệu '{database_name}' đã được xóa thành công.")

        # Đóng kết nối
        cursor.close()
        conn.close()
    
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Gọi hàm để xóa cơ sở dữ liệu
delete_database('Quan_Ly_Thu_Vien')
