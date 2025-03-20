# Phần Mềm Quản Lý Thư Viện

## Tổng Quan
Đây là một **phần mềm quản lý thư viện** được xây dựng bằng **Python**, với giao diện đồ họa (GUI) sử dụng **Tkinter** và quản lý cơ sở dữ liệu bằng **SQL Server**. Phần mềm được thiết kế theo mô hình **Model-View-Controller (MVC)** để đảm bảo tính mô-đun, khả năng mở rộng và dễ bảo trì.

## Tính Năng
- 🔹 **Giao diện thân thiện**: Phát triển bằng Tkinter, dễ sử dụng và trực quan.
- 🔹 **Quản lý cơ sở dữ liệu**: Sử dụng SQL Server để lưu trữ và truy xuất dữ liệu hiệu quả.
- 🔹 **Mô hình MVC**: Tách biệt giữa **Mô hình (Model)**, **Giao diện (View)** và **Điều khiển (Controller)** giúp tổ chức mã nguồn tốt hơn.
- 🔹 **Quản lý sách**: Thêm, cập nhật, xóa và tìm kiếm sách trong thư viện.
- 🔹 **Quản lý người dùng**: Theo dõi thành viên thư viện và trạng thái mượn sách.
- 🔹 **Quản lý giao dịch**: Ghi nhận lịch sử mượn và trả sách.

## Công Nghệ Sử Dụng
- ✅ **Python** *(Ngôn ngữ lập trình chính)*
- ✅ **Tkinter** *(Phát triển giao diện GUI)*
- ✅ **SQL Server** *(Quản lý cơ sở dữ liệu)*
- ✅ **Pyodbc** *(Kết nối cơ sở dữ liệu)*

## Hướng Dẫn Cài Đặt
1. **Clone kho lưu trữ:**
   ```sh
   git clone https://github.com/your-username/library-management.git
   ```
2. **Cài đặt các thư viện cần thiết:**
   ```sh
   pip install pyodbc
   ```
3. **Cấu hình kết nối cơ sở dữ liệu** trong tập tin cấu hình của ứng dụng.
4. **Chạy phần mềm:**
   ```sh
   python main.py
   ```
