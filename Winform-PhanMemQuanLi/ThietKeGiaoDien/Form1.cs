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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        SqlConnection bienConnect = null;
        private string ConnectString = "Data Source=DESKTOP-73HD43G\\SQLEXPRESS" +
                "; Initial Catalog=dataForProject" +
                "; Integrated Security=True";
        private void Form1_Load(object sender, EventArgs e)
        {
            bienConnect = new SqlConnection(ConnectString);
            bienConnect.Open();
        }

        // = false khi form đó đã được mở 1 lần
        public bool fHangHoa = true, fDoiTac = true, fHoaDon = true, 
            fThongKe = true, fBangGia = true, fTaiKhoan = true;

        FormHangHoa childHangHoa; 

        private void btnHangHoa_Click(object sender, EventArgs e)
        {
            if (fHangHoa)
            {
                childHangHoa = new FormHangHoa();
                childHangHoa.connOfHangHoa = bienConnect;
                fHangHoa = false; childHangHoa.TopLevel = false;
            }
            pnlChinh.Controls.Clear(); pnlChinh.Controls.Add(childHangHoa);
            childHangHoa.Dock = DockStyle.Fill;
            childHangHoa.Show();
        }

        FormDoiTac childDoiTac;
        private void btnDoiTac_Click(object sender, EventArgs e)
        {
            if (fDoiTac)
            {
                childDoiTac = new FormDoiTac();
                childDoiTac.connOfDoiTac = bienConnect; 
                fDoiTac = false; childDoiTac.TopLevel = false;
            }
            pnlChinh.Controls.Clear(); pnlChinh.Controls.Add(childDoiTac);
            childDoiTac.Dock = DockStyle.Fill;
            childDoiTac.Show();
        }

        FormHoaDon childHoaDon;
        private void btnHoaDon_Click(object sender, EventArgs e)
        {
            if (fHoaDon)
            {
                childHoaDon = new FormHoaDon();
                childHoaDon.conofHoaDon = bienConnect;
                fHoaDon = false; childHoaDon.TopLevel = false;
            }
            pnlChinh.Controls.Clear(); pnlChinh.Controls.Add(childHoaDon);
            childHoaDon.Dock = DockStyle.Fill;
            childHoaDon.Show();
        }

        FormThongKe childThongKe;

        private void btnX_MouseEnter(object sender, EventArgs e)
        {
            Button buttonX = (Button)sender;
            buttonX.BackColor = Color.Gray;
        }

        private void btnX_MouseLeave(object sender, EventArgs e)
        {
            Button buttonX = (Button)sender;
            buttonX.BackColor = Color.White;
        }


        private void btnThongKe_Click(object sender, EventArgs e)
        {
            if (fThongKe)
            {
                childThongKe = new FormThongKe();
                childThongKe.connOfThongKe = bienConnect;
                fThongKe = false; childThongKe.TopLevel = false;
            }
            pnlChinh.Controls.Clear(); pnlChinh.Controls.Add(childThongKe);
            childThongKe.Dock = DockStyle.Fill;
            childThongKe.Show();
        }
        
        FormBangGia childBangGia;
        private void btnBangGia_Click(object sender, EventArgs e)
        {
            if (fBangGia)
            {
                childBangGia = new FormBangGia();
                fBangGia = false; childBangGia.TopLevel = false;
            }
            pnlChinh.Controls.Clear(); pnlChinh.Controls.Add(childBangGia);
            childBangGia.Dock = DockStyle.Fill;
            childBangGia.Show();
        }

        FormTaiKhoan childTaiKhoan;
        private void btnTaiKhoan_Click(object sender, EventArgs e)
        {
            if (fTaiKhoan)
            {
                childTaiKhoan = new FormTaiKhoan();
                fTaiKhoan = false; childTaiKhoan.TopLevel = false;
            }
            pnlChinh.Controls.Clear(); pnlChinh.Controls.Add(childTaiKhoan);
            childTaiKhoan.Dock = DockStyle.Fill;
            childTaiKhoan.Show();
        }

    }
}
