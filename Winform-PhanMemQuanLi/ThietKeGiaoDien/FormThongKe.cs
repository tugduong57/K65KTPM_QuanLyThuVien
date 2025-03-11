using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using System.Windows.Forms;

namespace ThietKeGiaoDien
{
    public partial class FormThongKe : Form
    {
        public FormThongKe()
        {
            InitializeComponent();
        }

        public SqlConnection connOfThongKe;

        private void FormThongKe_Load(object sender, EventArgs e)
        {
            string lenhTruyVanSQL = "Select [Ngày tạo], [Mã đối tác], [Tổng tiền] from HoaDon";
            SqlDataAdapter bienSQLDataAdapter = new SqlDataAdapter(lenhTruyVanSQL, connOfThongKe);

            DataTable bienDataTable = new DataTable();

            bienSQLDataAdapter.Fill(bienDataTable);

            dgvThongKe.DataSource = bienDataTable;

            foreach (DataGridViewColumn dataGridViewColumn in dgvThongKe.Columns)
            {
                dataGridViewColumn.AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
                dataGridViewColumn.MinimumWidth = 50;
            }
            dgvThongKe.Columns[0].MinimumWidth = 20;

        }




        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void tableLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

    }
}
