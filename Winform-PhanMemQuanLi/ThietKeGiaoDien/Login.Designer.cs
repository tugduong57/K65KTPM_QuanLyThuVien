namespace ThietKeGiaoDien
{
    partial class Login
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btLogin = new System.Windows.Forms.Button();
            this.lbLogin = new System.Windows.Forms.Label();
            this.tbUser = new System.Windows.Forms.TextBox();
            this.pnl_SignIn = new System.Windows.Forms.Panel();
            this.tbPassword = new System.Windows.Forms.TextBox();
            this.btnShowPassword = new System.Windows.Forms.Button();
            this.pnl_SignIn.SuspendLayout();
            this.SuspendLayout();
            // 
            // btLogin
            // 
            this.btLogin.BackColor = System.Drawing.Color.ForestGreen;
            this.btLogin.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btLogin.Font = new System.Drawing.Font("Arial", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btLogin.ForeColor = System.Drawing.SystemColors.Control;
            this.btLogin.Location = new System.Drawing.Point(62, 246);
            this.btLogin.Name = "btLogin";
            this.btLogin.Size = new System.Drawing.Size(270, 43);
            this.btLogin.TabIndex = 0;
            this.btLogin.Text = "Đăng Nhập";
            this.btLogin.UseVisualStyleBackColor = false;
            this.btLogin.Click += new System.EventHandler(this.btLogin_Click);
            // 
            // lbLogin
            // 
            this.lbLogin.AutoSize = true;
            this.lbLogin.Font = new System.Drawing.Font("Arial", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbLogin.Location = new System.Drawing.Point(134, 23);
            this.lbLogin.Name = "lbLogin";
            this.lbLogin.Size = new System.Drawing.Size(138, 29);
            this.lbLogin.TabIndex = 1;
            this.lbLogin.Text = "Đăng nhập";
            // 
            // tbUser
            // 
            this.tbUser.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.tbUser.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbUser.Location = new System.Drawing.Point(62, 103);
            this.tbUser.Name = "tbUser";
            this.tbUser.Size = new System.Drawing.Size(270, 26);
            this.tbUser.TabIndex = 2;
            this.tbUser.Text = "Username";
            this.tbUser.MouseDown += new System.Windows.Forms.MouseEventHandler(this.tbUser_MouseDown);
            // 
            // pnl_SignIn
            // 
            this.pnl_SignIn.BackColor = System.Drawing.SystemColors.InactiveBorder;
            this.pnl_SignIn.Controls.Add(this.btnShowPassword);
            this.pnl_SignIn.Controls.Add(this.tbPassword);
            this.pnl_SignIn.Controls.Add(this.lbLogin);
            this.pnl_SignIn.Controls.Add(this.btLogin);
            this.pnl_SignIn.Controls.Add(this.tbUser);
            this.pnl_SignIn.Location = new System.Drawing.Point(136, 12);
            this.pnl_SignIn.Name = "pnl_SignIn";
            this.pnl_SignIn.Size = new System.Drawing.Size(423, 473);
            this.pnl_SignIn.TabIndex = 4;
            // 
            // tbPassword
            // 
            this.tbPassword.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.tbPassword.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbPassword.Location = new System.Drawing.Point(62, 162);
            this.tbPassword.Name = "tbPassword";
            this.tbPassword.Size = new System.Drawing.Size(270, 26);
            this.tbPassword.TabIndex = 3;
            this.tbPassword.Text = "Password";
            this.tbPassword.MouseDown += new System.Windows.Forms.MouseEventHandler(this.tbPassword_MouseDown);
            // 
            // btnShowPassword
            // 
            this.btnShowPassword.Location = new System.Drawing.Point(304, 162);
            this.btnShowPassword.Name = "btnShowPassword";
            this.btnShowPassword.Size = new System.Drawing.Size(28, 26);
            this.btnShowPassword.TabIndex = 4;
            this.btnShowPassword.Text = "👁️";
            this.btnShowPassword.UseVisualStyleBackColor = true;
            this.btnShowPassword.Click += new System.EventHandler(this.btnShowPassword_Click);
            // 
            // Login
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(684, 497);
            this.Controls.Add(this.pnl_SignIn);
            this.Name = "Login";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Login";
            this.pnl_SignIn.ResumeLayout(false);
            this.pnl_SignIn.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btLogin;
        private System.Windows.Forms.Label lbLogin;
        private System.Windows.Forms.TextBox tbUser;
        private System.Windows.Forms.Panel pnl_SignIn;
        private System.Windows.Forms.TextBox tbPassword;
        private System.Windows.Forms.Button btnShowPassword;
    }
}