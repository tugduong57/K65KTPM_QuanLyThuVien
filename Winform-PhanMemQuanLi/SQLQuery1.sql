CREATE DATABASE QuanLyKhoHang;
USE QuanLyKhoHang;

-- Bảng người dùng (tạo trước để HoaDon có thể tham chiếu)
CREATE TABLE NguoiDung (
    ID_NgBan VARCHAR(100) PRIMARY KEY NOT NULL,
    MatKhau VARCHAR(100),
    Ten_NguoiDung NVARCHAR(100),
    Vai_Tro NVARCHAR(100),
    Ghi_Chu NVARCHAR(100)
);

-- Bảng đối tác
CREATE TABLE DoiTac (
    ID_DoiTac VARCHAR(100) PRIMARY KEY NOT NULL,
    Phan_Loai NVARCHAR(100),
    Ten NVARCHAR(100),
    Tuoi NVARCHAR(100),
    Dia_Chi NVARCHAR(100),
    SDT VARCHAR(100),
    Ghi_Chu NVARCHAR(100)
);

-- Bảng sản phẩm
CREATE TABLE SanPham (
    ID_SanPham VARCHAR(100) PRIMARY KEY NOT NULL,
    Ten_SanPham NVARCHAR(100),
    Hang NVARCHAR(100),
    Phan_Loai NVARCHAR(100),
    Don_ViTinh NVARCHAR(100),
    So_Luong INT CHECK (So_Luong >= 0),
    Gia_NhapTrungBinh MONEY,
    Gia_BanHienTai MONEY,
    Ghi_Chu NVARCHAR(100)
);

-- Bảng hóa đơn
CREATE TABLE HoaDon (
    ID_HoaDon VARCHAR(100) PRIMARY KEY NOT NULL,
    ID_DoiTac VARCHAR(100),
    ID_NgBan VARCHAR(100),
    NgayTao DATETIME DEFAULT GETDATE(),
    Loai_HoaDon VARCHAR(100),
    TongTien MONEY DEFAULT 0,
    FOREIGN KEY (ID_DoiTac) REFERENCES DoiTac(ID_DoiTac) ON DELETE CASCADE,
    FOREIGN KEY (ID_NgBan) REFERENCES NguoiDung(ID_NgBan) ON DELETE CASCADE
);

-- Bảng chi tiết hóa đơn
CREATE TABLE ChiTietHoaDon (
    ID_HoaDon VARCHAR(100),
    ID_SanPham VARCHAR(100),
    SoLuongBan INT CHECK (SoLuongBan > 0), -- Số hộp bán ra
    DonGia MONEY NOT NULL,
    ThanhTien AS (SoLuongBan * DonGia), -- Tính tổng tiền tự động
    PRIMARY KEY (ID_HoaDon, ID_SanPham),
    FOREIGN KEY (ID_HoaDon) REFERENCES HoaDon(ID_HoaDon) ON DELETE CASCADE,
    FOREIGN KEY (ID_SanPham) REFERENCES SanPham(ID_SanPham) ON DELETE CASCADE
);
