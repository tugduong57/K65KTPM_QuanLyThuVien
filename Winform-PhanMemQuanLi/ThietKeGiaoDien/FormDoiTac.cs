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
    public partial class FormDoiTac : Form
    {
        private FormDoiTac_KH fDT_KH;
        private FormDoiTac_NCC fDT_NCC;
        public SqlConnection connOfDoiTac;

        public FormDoiTac()
        {
            InitializeComponent();
        }

        private void btnKH_Click(object sender, EventArgs e)
        {
            if (fDT_KH == null)
            {
                fDT_KH = new FormDoiTac_KH();
                fDT_KH.TopLevel = false;
            }
            fDT_KH.bienconnect = connOfDoiTac;
            pnl_DoiTac.Controls.Clear();
            pnl_DoiTac.Controls.Add(fDT_KH);
            fDT_KH.Dock = DockStyle.Fill;
            fDT_KH.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (fDT_NCC == null)
            {
                fDT_NCC = new FormDoiTac_NCC();
                fDT_NCC.TopLevel = false;
            }
            fDT_NCC.bienconnect = connOfDoiTac;
            pnl_DoiTac.Controls.Clear();
            pnl_DoiTac.Controls.Add(fDT_NCC);
            fDT_NCC.Dock = DockStyle.Fill;
            fDT_NCC.Show();
            
        }
    }
}
