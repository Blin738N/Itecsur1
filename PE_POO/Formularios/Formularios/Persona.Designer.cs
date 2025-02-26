namespace Formularios
{
    partial class Persona
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
            label1 = new Label();
            label2 = new Label();
            cualquiernombre1 = new TextBox();
            cualquiernombredelavariable2 = new TextBox();
            button1 = new Button();
            btnMostrarLista = new Button();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(44, 32);
            label1.Name = "label1";
            label1.Size = new Size(105, 15);
            label1.TabIndex = 0;
            label1.Text = "Ingrese su nombre";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(44, 113);
            label2.Name = "label2";
            label2.Size = new Size(89, 15);
            label2.TabIndex = 1;
            label2.Text = "Ingrese su edad";
            // 
            // cualquiernombre1
            // 
            cualquiernombre1.Location = new Point(44, 66);
            cualquiernombre1.Name = "cualquiernombre1";
            cualquiernombre1.Size = new Size(100, 23);
            cualquiernombre1.TabIndex = 5;
            // 
            // cualquiernombredelavariable2
            // 
            cualquiernombredelavariable2.Location = new Point(44, 142);
            cualquiernombredelavariable2.Name = "cualquiernombredelavariable2";
            cualquiernombredelavariable2.Size = new Size(100, 23);
            cualquiernombredelavariable2.TabIndex = 6;
            // 
            // button1
            // 
            button1.Location = new Point(51, 204);
            button1.Name = "button1";
            button1.Size = new Size(106, 29);
            button1.TabIndex = 7;
            button1.Text = "Registrar";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // btnMostrarLista
            // 
            btnMostrarLista.Location = new Point(51, 250);
            btnMostrarLista.Name = "btnMostrarLista";
            btnMostrarLista.Size = new Size(104, 31);
            btnMostrarLista.TabIndex = 8;
            btnMostrarLista.Text = "mostrar lista";
            btnMostrarLista.UseVisualStyleBackColor = true;
            btnMostrarLista.Click += btnMostrarLista_Click;
            // 
            // Persona
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(480, 450);
            Controls.Add(btnMostrarLista);
            Controls.Add(button1);
            Controls.Add(cualquiernombredelavariable2);
            Controls.Add(cualquiernombre1);
            Controls.Add(label2);
            Controls.Add(label1);
            Name = "Persona";
            Text = "Persona";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private TextBox cualquiernombre1;
        private TextBox cualquiernombredelavariable2;
        private Button button1;
        private Button btnMostrarLista;
    }
}