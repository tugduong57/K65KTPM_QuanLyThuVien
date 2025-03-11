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
    public partial class FormDoiTac_NCC : Form
    {
        public SqlConnection bienconnect;
        public FormDoiTac_NCC()
        {
            InitializeComponent();
        }

        private void FormDoiTac_NCC_Load(object sender, EventArgs e)
        {
            string lenhSQl = "select * from Doitac where [Phân loại] = N'Nhà cung cấp'";
            SqlDataAdapter ada = new SqlDataAdapter(lenhSQl, bienconnect);
            DataTable dt = new DataTable();
            ada.Fill(dt);
            dgvNCC.DataSource = dt;
        }
    }
}
