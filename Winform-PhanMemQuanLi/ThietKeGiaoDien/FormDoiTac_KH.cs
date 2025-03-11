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
    public partial class FormDoiTac_KH : Form
    {
        public SqlConnection bienconnect;
        public FormDoiTac_KH()
        {
            InitializeComponent();
        }

        private void FormDoiTac_KH_Load(object sender, EventArgs e)
        {
            string lenhSQL = "select * from DoiTac";
            SqlDataAdapter ada = new SqlDataAdapter(lenhSQL, bienconnect);
            DataTable dt = new DataTable();
            ada.Fill(dt);
            dgvKhachHang.DataSource = dt;
        }
    }
}
