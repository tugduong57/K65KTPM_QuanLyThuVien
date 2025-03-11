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
    public partial class FormHoaDonLichSu : Form
    {
        public SqlConnection BienConnect;
        public FormHoaDonLichSu()
        {
            InitializeComponent();
        }

        private void FormHoaDonLichSu_Load(object sender, EventArgs e)
        {
            LoadDuLieu();

            if(!dgvHDLichSu.Columns.Contains("btnChiTiet"))
            {
                DataGridViewButtonColumn btnColumn = new DataGridViewButtonColumn();
                btnColumn.Name = "btnChiTiet";
                btnColumn.HeaderText = "Chi tiết";
                btnColumn.Text = "Xem";
                btnColumn.UseColumnTextForButtonValue = true;
                dgvHDLichSu.Columns.Add(btnColumn);
            }
        }
        private void LoadDuLieu()
        {
            try
            {
                string lenhSQl = "select * from HoaDon";
                SqlDataAdapter adapter = new SqlDataAdapter(lenhSQl, BienConnect);
                DataTable dt = new DataTable();
                adapter.Fill(dt);
                dgvHDLichSu.DataSource = dt;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi khi tải lịch sử hóa đơn: "+ ex.Message);
            }
        }

        private void dgvHDLichSu_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            if(dgvHDLichSu.Columns[e.ColumnIndex].Name == "btnChiTiet" && e.RowIndex >= 0)
            {
                string maHD = dgvHDLichSu.Rows[e.RowIndex].Cells["Mã Hóa Đơn"].Value.ToString();
                FormChiTietHoaDon f = new FormChiTietHoaDon(maHD);
                f.BienConnect = BienConnect;
                f.ShowDialog();

            }
        }

    }
}
