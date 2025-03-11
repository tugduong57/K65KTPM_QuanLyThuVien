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
    public partial class FormHangHoa : Form
    {
        public FormHangHoa()
        {
            InitializeComponent();
        }

        public SqlConnection connOfHangHoa;

        private void FormHangHoa_Load(object sender, EventArgs e)
        {

            string lenhTruyVanSQL = "Select [Tên sản phẩm], Hãng, [Phân loại], [Ghi chú] from SanPham";
            SqlDataAdapter bienSQLDataAdapter = new SqlDataAdapter(lenhTruyVanSQL, connOfHangHoa);

            DataTable bienDataTable = new DataTable();

            bienSQLDataAdapter.Fill(bienDataTable);

            dgvHangHoa.DataSource = bienDataTable;


            foreach (DataGridViewColumn dataGridViewColumn in dgvHangHoa.Columns)
            {
                dataGridViewColumn.AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
                dataGridViewColumn.MinimumWidth = 50;
            }
            dgvHangHoa.Columns[0].MinimumWidth = 20;

        }
    }
}
