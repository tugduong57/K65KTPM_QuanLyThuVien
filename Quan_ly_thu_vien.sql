create database Quan_Ly_Thu_Vien;

-- tạo bảng admin
create table admin (
	tai_khoan varchar(20) not null primary key,
	mat_khau varchar(20) not null
);

-- Tạo bảng sách
create table sach (
	ma_sach char(20) not null primary key,
	ten_sach nchar(30),
	the_loai nchar(20),
	ngay_xuat_ban date,
	nha_xuat_ban nchar(30),
	tac_gia nchar(30),
	gia_sach int,
	tong_so_luong int
);


-- Tạo bảng độc giả
create table doc_gia (
	ma_doc_gia char(20) not null primary key,
	ho_ten nchar(30),
	so_DT varchar(15),
	trang_thai nchar(30)
);


-- Tạo bảng phiếu mượn
create table phieu_muon (
	ma_phieu char(20) not null primary key,
	ma_doc_gia char(20),
	ngay_muon date,
	han_tra_sach date,
	ma_sach char(20),
	foreign key (ma_sach) references sach(ma_sach),
	foreign key (ma_doc_gia) references doc_gia(ma_doc_gia)
);


-- Tạo bảng danh sách mượn
create table danh_sach_muon (
	ma_phieu char(20) not null,
	ma_sach char(20) not null,
	primary key (ma_phieu, ma_sach),
	foreign key (ma_phieu) references phieu_muon(ma_phieu)
);

