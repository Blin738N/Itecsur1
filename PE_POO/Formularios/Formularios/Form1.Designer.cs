namespace Formularios
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            tbNum1 = new TextBox();
            tbNum2 = new TextBox();
            btnCalcular = new Button();
            label3 = new Label();
            result = new Label();
            sumar = new CheckBox();
            restar = new CheckBox();
            dividir = new CheckBox();
            multiplicar = new CheckBox();
            button1 = new Button();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(65, 57);
            label1.Name = "label1";
            label1.Size = new Size(78, 36);
            label1.TabIndex = 0;
            label1.Text = "numero 1";
            label1.Click += label1_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(65, 143);
            label2.Name = "label2";
            label2.Size = new Size(81, 36);
            label2.TabIndex = 1;
            label2.Text = "numero 2";
            // 
            // tbNum1
            // 
            tbNum1.Location = new Point(69, 96);
            tbNum1.Name = "tbNum1";
            tbNum1.Size = new Size(154, 44);
            tbNum1.TabIndex = 3;
            // 
            // tbNum2
            // 
            tbNum2.Location = new Point(69, 193);
            tbNum2.Name = "tbNum2";
            tbNum2.Size = new Size(150, 44);
            tbNum2.TabIndex = 4;
            // 
            // btnCalcular
            // 
            btnCalcular.Location = new Point(43, 334);
            btnCalcular.Name = "btnCalcular";
            btnCalcular.Size = new Size(123, 39);
            btnCalcular.TabIndex = 5;
            btnCalcular.Text = "Calcular";
            btnCalcular.UseVisualStyleBackColor = true;
            btnCalcular.Click += btnCalcular_Click;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(69, 21);
            label3.Name = "label3";
            label3.Size = new Size(159, 36);
            label3.TabIndex = 6;
            label3.Text = "Operaciones Básicas";
            // 
            // result
            // 
            result.AutoSize = true;
            result.Location = new Point(43, 376);
            result.Name = "result";
            result.Size = new Size(86, 36);
            result.TabIndex = 7;
            result.Text = "Resultado";
            // 
            // sumar
            // 
            sumar.AutoSize = true;
            sumar.Location = new Point(67, 279);
            sumar.Name = "sumar";
            sumar.Size = new Size(43, 40);
            sumar.TabIndex = 8;
            sumar.Text = "+";
            sumar.UseVisualStyleBackColor = true;
            // 
            // restar
            // 
            restar.AutoSize = true;
            restar.Location = new Point(116, 279);
            restar.Name = "restar";
            restar.Size = new Size(40, 40);
            restar.TabIndex = 9;
            restar.Text = "-";
            restar.UseVisualStyleBackColor = true;
            // 
            // dividir
            // 
            dividir.AutoSize = true;
            dividir.Location = new Point(211, 279);
            dividir.Name = "dividir";
            dividir.Size = new Size(39, 40);
            dividir.TabIndex = 11;
            dividir.Text = "/";
            dividir.UseVisualStyleBackColor = true;
            // 
            // multiplicar
            // 
            multiplicar.AutoSize = true;
            multiplicar.Location = new Point(162, 279);
            multiplicar.Name = "multiplicar";
            multiplicar.Size = new Size(42, 40);
            multiplicar.TabIndex = 10;
            multiplicar.Text = "*";
            multiplicar.UseVisualStyleBackColor = true;
            // 
            // button1
            // 
            button1.Location = new Point(193, 334);
            button1.Name = "button1";
            button1.Size = new Size(180, 39);
            button1.TabIndex = 12;
            button1.Text = "Ir Nueva Pantalla";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(9F, 36F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.FromArgb(224, 224, 224);
            ClientSize = new Size(1029, 749);
            Controls.Add(button1);
            Controls.Add(dividir);
            Controls.Add(multiplicar);
            Controls.Add(restar);
            Controls.Add(sumar);
            Controls.Add(result);
            Controls.Add(label3);
            Controls.Add(btnCalcular);
            Controls.Add(tbNum2);
            Controls.Add(tbNum1);
            Controls.Add(label2);
            Controls.Add(label1);
            Font = new Font("Javanese Text", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            Margin = new Padding(4, 7, 4, 7);
            MaximizeBox = false;
            Name = "Form1";
            Text = "Controles";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private TextBox tbNum1;
        private TextBox tbNum2;
        private Button btnCalcular;
        private Label label3;
        private Label result;
        private CheckBox sumar;
        private CheckBox restar;
        private CheckBox dividir;
        private CheckBox multiplicar;
        private Button button1;
    }
}
