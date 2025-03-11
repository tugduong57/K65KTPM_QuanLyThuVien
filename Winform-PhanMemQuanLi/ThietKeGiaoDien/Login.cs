using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ThietKeGiaoDien
{
    public partial class Login : Form
    {
        public Login()
        {
            InitializeComponent();
        }

        private void btnShowPassword_Click(object sender, EventArgs e)
        {
            if (tbPassword.UseSystemPasswordChar)
            {
                tbPassword.UseSystemPasswordChar = false; 
                btnShowPassword.Text = "👁️";
            }
            else
            {
                tbPassword.UseSystemPasswordChar = true;
                btnShowPassword.Text = "🙈";
            }
        }

        private void tbPassword_MouseDown(object sender, MouseEventArgs e)
        {
            if (tbPassword.Text == "Password")
            {
                tbPassword.Text = "";
                tbPassword.UseSystemPasswordChar = true;
            }
        }
        private void tbUser_MouseDown(object sender, MouseEventArgs e)
        {
            if(tbUser.Text == "Username")
            {
                tbUser.Text = "";
            }
        }

        private void btLogin_Click(object sender, EventArgs e)
        {
            string user = tbUser.Text;
            string password = tbPassword.Text;
            if (user == "admin" && password == "admin")
            {
                this.Hide();
                Form1 form1 = new Form1();
                form1.ShowDialog();
                this.Close();
            }
            else
            {
                MessageBox.Show("Sai tên đăng nhập hoặc mật khẩu");
            }
        }
    }
}
