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
    public partial class FormChiTietHoaDon : Form
    {
        public SqlConnection BienConnect;
        private string maHD;
        public FormChiTietHoaDon(string maHD)
        {
            InitializeComponent();
            this.maHD = maHD;
        }
        private void FormChiTietHoaDon_Load(object sender, EventArgs e)
        {
            LoadChiTietHoaDon();
        }

        private void LoadChiTietHoaDon()
        {
            try
            {
                string lenhSQL = "select * from ChiTietHoaDon where [Mã Hóa Đơn] = @maHD";
                SqlDataAdapter adapter = new SqlDataAdapter(lenhSQL, BienConnect);
                adapter.SelectCommand.Parameters.AddWithValue("@maHD", maHD);
                DataTable dt = new DataTable();
                adapter.Fill(dt);
                dgvChiTietHoaDon.DataSource = dt;
            }
            catch(Exception ex)
            {
                MessageBox.Show("Lỗi khi tải chi tiết hóa đơn: " + ex.Message);
            }
        }
    }
}
