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
    public partial class FormHoaDon : Form
    {
        public SqlConnection conofHoaDon;

        private FormHoaDonXuat fXuat;
        private FormHoaDonNhap fNhap;
        private FormHoaDonLichSu fLichSu;
        public FormHoaDon()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(fXuat == null)
            {
                fXuat = new FormHoaDonXuat();
                fXuat.TopLevel = false;
            }
                fXuat.BienConnect = conofHoaDon;
                pnl_hoadon.Controls.Clear();
                pnl_hoadon.Controls.Add(fXuat);
                fXuat.Dock = DockStyle.Fill;
                fXuat.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(fNhap == null)
            {
                fNhap = new FormHoaDonNhap();
                fNhap.TopLevel = false;
            }
                fNhap.BienConnect = conofHoaDon;
                pnl_hoadon.Controls.Clear();
                pnl_hoadon.Controls.Add(fNhap);
                fNhap.Dock = DockStyle.Fill;
                fNhap.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if(fLichSu == null)
            {
                fLichSu = new FormHoaDonLichSu();
                fLichSu.TopLevel = false;
            }
            fLichSu.BienConnect = conofHoaDon;
            pnl_hoadon.Controls.Clear();
            pnl_hoadon.Controls.Add(fLichSu);
            fLichSu.Dock = DockStyle.Fill;
            fLichSu.Show();
        }
    }
}
