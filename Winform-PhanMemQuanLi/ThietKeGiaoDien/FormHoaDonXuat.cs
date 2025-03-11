using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ThietKeGiaoDien
{


    public partial class FormHoaDonXuat : Form
    {
        public SqlConnection BienConnect;
        public FormHoaDonXuat()
        {
            InitializeComponent();
        }
        private void FormXuat_Load(object sender, EventArgs e)
        {
            try
            {
                string lenhSQL = "SELECT [Mã Đối Tác], [Tên Đối Tác], [Địa Chỉ], [Số Điện Thoại] FROM DoiTac " +
                                 "WHERE [Phân loại] = 'Khách Hàng'";

                SqlDataAdapter adapter = new SqlDataAdapter(lenhSQL, BienConnect);
                DataTable dt = new DataTable();
                adapter.Fill(dt);

                cbb_KhachHang.DataSource = dt;
                cbb_KhachHang.DisplayMember = "Tên Đối Tác";
                cbb_KhachHang.ValueMember = "Mã Đối Tác";

                // Đặt mặc định là không chọn gì
                cbb_KhachHang.SelectedIndex = -1;
                tb_DiaChi.Text = "";
                tb_SDT.Text = "";
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi tải khách hàng: " + ex.Message);
            }
        }
        private void cbb_KhachHang_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (cbb_KhachHang.SelectedIndex != -1)
            {
                DataTable dt = (DataTable)cbb_KhachHang.Tag;
                DataRowView row = cbb_KhachHang.SelectedItem as DataRowView;
                tb_DiaChi.Text = row["Địa Chỉ"].ToString();
                tb_SDT.Text = row["Số Điện Thoại"].ToString();
            }
            else
            {
                tb_DiaChi.Text = "";
                tb_SDT.Text = "";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string tenKhachHang = cbb_KhachHang.Text.Trim();
            string diaChi = tb_DiaChi.Text.Trim();
            string soDienThoai = tb_SDT.Text.Trim();

            if (string.IsNullOrEmpty(tenKhachHang) || string.IsNullOrEmpty(diaChi) || string.IsNullOrEmpty(soDienThoai))
            {
                MessageBox.Show("Vui lòng nhập đầy đủ thông tin!", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            try
            {
                // Kiểm tra khách hàng đã tồn tại chưa
                string checkQuery = "SELECT COUNT(*) FROM DoiTac WHERE [Tên Đối Tác] = @TenKhachHang";
                SqlCommand checkCmd = new SqlCommand(checkQuery, BienConnect);
                checkCmd.Parameters.AddWithValue("@TenKhachHang", tenKhachHang);

                int count = (int)checkCmd.ExecuteScalar();
                if (count > 0)
                {
                    MessageBox.Show("Khách hàng đã tồn tại!", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }

                // **Tạo mã đối tác tự động**
                string newMaDoiTac = GenerateNewMaDoiTac();

                // **Thêm khách hàng mới**
                string insertQuery = "INSERT INTO DoiTac ([Mã Đối Tác], [Tên Đối Tác], [Địa Chỉ], [Số Điện Thoại], [Phân loại]) " +
                                     "VALUES (@MaDT, @Ten, @DiaChi, @SoDT, 'Khách Hàng')";
                SqlCommand cmd = new SqlCommand(insertQuery, BienConnect);
                cmd.Parameters.AddWithValue("@MaDT", newMaDoiTac);
                cmd.Parameters.AddWithValue("@Ten", tenKhachHang);
                cmd.Parameters.AddWithValue("@DiaChi", diaChi);
                cmd.Parameters.AddWithValue("@SoDT", soDienThoai);

                cmd.ExecuteNonQuery();
                MessageBox.Show("Thêm khách hàng thành công!", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Information);

                // Cập nhật lại danh sách khách hàng
                FormXuat_Load(sender, e);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi khi thêm khách hàng: " + ex.Message);
            }

        }
        private string GenerateNewMaDoiTac()
        {
            string newMaDoiTac = "DT01"; // Giá trị mặc định nếu chưa có dữ liệu

            try
            {
                string query = "SELECT MAX(CAST(SUBSTRING([Mã Đối Tác], 3, LEN([Mã Đối Tác]) - 2) AS INT)) FROM DoiTac";
                SqlCommand cmd = new SqlCommand(query, BienConnect);
                object result = cmd.ExecuteScalar();

                if (result != DBNull.Value && result != null)
                {
                    int maxNumber = Convert.ToInt32(result);
                    maxNumber++;
                    newMaDoiTac = "DT" + maxNumber.ToString();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi tạo mã đối tác: " + ex.Message);
            }

            return newMaDoiTac;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            DialogResult result  = MessageBox.Show("Bạn có chắc muốn hủy hóa đơn?", "Xác Nhận",
                MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                cbb_KhachHang.SelectedIndex = -1;
                tb_DiaChi.Text = "";
                tb_SDT.Text = "";
            }
        }

        private void dgvHoaDonXuat_CellEndEdit(object sender, DataGridViewCellEventArgs e)
        {
           
        }
    }
}
