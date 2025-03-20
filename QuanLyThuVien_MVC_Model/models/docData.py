import pyodbc

def read_all_records():
    try:
        conn_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=Quan_Ly_Thu_Vien;"  # Thay đổi thành tên cơ sở dữ liệu của bạn
            "Trusted_Connection=yes;"
        )

        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()

        # Danh sách các bảng cần truy vấn
        tables = ['admin', 'sach', 'doc_gia', 'phieu_muon', 'danh_sach_muon']

        for table in tables:
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            records = cursor.fetchall()
            #print(records)
            print(f"Bảng {table}:")
            for row in records:
                print(row)
            print("\n")  # Thêm một dòng trống giữa các bảng

        # Đóng kết nối
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Gọi hàm để đọc tất cả bản ghi
read_all_records()