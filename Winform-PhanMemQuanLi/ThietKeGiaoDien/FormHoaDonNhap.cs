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
    public partial class FormHoaDonNhap : Form
    {
        public SqlConnection BienConnect;
        public FormHoaDonNhap()
        {
            InitializeComponent();
        }
        private void FormNhap_Load(object sender, EventArgs e)
        {
            try
            {
                string lenhSQL = "SELECT [Mã Đối Tác], [Tên Đối Tác], [Địa Chỉ], [Số Điện Thoại] FROM DoiTac " +
                                 "WHERE [Phân loại] = N'Nhà cung cấp'";

                SqlDataAdapter adapter = new SqlDataAdapter(lenhSQL, BienConnect);
                DataTable dt = new DataTable();
                adapter.Fill(dt);
                
                cbb_NCC.DataSource = dt;
                cbb_NCC.DisplayMember = "Tên Đối Tác";
                cbb_NCC.ValueMember = "Mã Đối Tác";

                cbb_NCC.Tag = dt;
                cbb_NCC.SelectedIndex = -1;
                tb_DiaChi.Text = "";
                tb_SDT.Text = "";
                
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi tải khách hàng: " + ex.Message);
            }
        }

        private string GenerateNewMaDoiTac()
        {
            string newMaDoiTac = "DT01"; 

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


        private void cbb_NCC_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (cbb_NCC.SelectedIndex != -1)
            {
                DataTable dt = (DataTable)cbb_NCC.Tag;
                DataRowView row = cbb_NCC.SelectedItem as DataRowView;
                tb_DiaChi.Text = row["Địa Chỉ"].ToString();
                tb_SDT.Text = row["Số Điện Thoại"].ToString();
            }
            else
            {
                tb_DiaChi.Text = "";
                tb_SDT.Text = "";
            }
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            string tenNCC = cbb_NCC.Text.Trim();
            string diaChi = tb_DiaChi.Text.Trim();
            string soDienThoai = tb_SDT.Text.Trim();

            if (string.IsNullOrEmpty(tenNCC) || string.IsNullOrEmpty(diaChi) || string.IsNullOrEmpty(soDienThoai))
            {
                MessageBox.Show("Vui lòng nhập đầy đủ thông tin!", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            try
            {
                // Kiểm tra khách hàng đã tồn tại chưa
                string checkQuery = "SELECT COUNT(*) FROM DoiTac WHERE [Tên Đối Tác] = @tenNCC";
                SqlCommand checkCmd = new SqlCommand(checkQuery, BienConnect);
                checkCmd.Parameters.AddWithValue("@tenNCC", tenNCC);

                int count = (int)checkCmd.ExecuteScalar();
                if (count > 0)
                {
                    MessageBox.Show("Nhà cung cấp đã tồn tại!", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }

                // **Tạo mã đối tác tự động**
                string newMaDoiTac = GenerateNewMaDoiTac();

                // **Thêm khách hàng mới**
                string insertQuery = "INSERT INTO DoiTac ([Mã Đối Tác], [Tên Đối Tác], [Địa Chỉ], [Số Điện Thoại], [Phân loại]) " +
                                     "VALUES (@MaDT, @Ten, @DiaChi, @SoDT, 'Nhà cung cấp')";
                SqlCommand cmd = new SqlCommand(insertQuery, BienConnect);
                cmd.Parameters.AddWithValue("@MaDT", newMaDoiTac);
                cmd.Parameters.AddWithValue("@Ten", tenNCC);
                cmd.Parameters.AddWithValue("@DiaChi", diaChi);
                cmd.Parameters.AddWithValue("@SoDT", soDienThoai);

                cmd.ExecuteNonQuery();
                MessageBox.Show("Thêm nhà cung cấp thành công!", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Information);

                // Cập nhật lại danh sách khách hàng
                FormNhap_Load(sender, e);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi khi thêm khách hàng: " + ex.Message);
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("Bạn có chắc muốn hủy hóa đơn?", "Xác Nhận",
               MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                cbb_NCC.SelectedIndex = -1;
                tb_DiaChi.Text = "";
                tb_SDT.Text = "";
            }
        }
    }
}
