namespace GestorCalificaciones
{
    internal class Form
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        
        
        private Label lblDNI;

        private Label lblApellido;

        private Label lblNombre;

        private Label lblNota;

        private TextBox textBox1;

        private TextBox textBox2;

        private TextBox textBox3;

        private TextBox textBox4;

        private Button tbnAgregar;

        private Button btnEliminar;

        private Button btnConsultar;

        private Button btnModificarNota;

        private Button btnMostarAprobados;

        private Button btnMostrarSuspenso;

        private Button btnCandidatosMH;

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

        
        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lblDNI = new Label();
            lblApellido = new Label();
            lblNombre = new Label();
            lblNota = new Label();
            textBox1 = new TextBox();
            textBox2 = new TextBox();
            textBox3 = new TextBox();
            textBox4 = new TextBox();
            tbnAgregar = new Button();
            btnEliminar = new Button();
            btnConsultar = new Button();
            btnModificarNota = new Button();
            btnMostarAprobados = new Button();
            btnMostrarSuspenso = new Button();
            btnCandidatosMH = new Button();
          
            // 
            // lblDNI
            // 
            lblDNI.AutoSize = true;
            lblDNI.Location = new Point(43, 30);
            lblDNI.Name = "lblDNI";
            lblDNI.Size = new Size(27, 15);
            lblDNI.TabIndex = 0;
            lblDNI.Text = "DNI";
            // 
            // lblApellido
            // 
            lblApellido.AutoSize = true;
            lblApellido.Location = new Point(43, 72);
            lblApellido.Name = "lblApellido";
            lblApellido.Size = new Size(51, 15);
            lblApellido.TabIndex = 1;
            lblApellido.Text = "Apellido";
            // 
            // lblNombre
            // 
            lblNombre.AutoSize = true;
            lblNombre.Location = new Point(43, 110);
            lblNombre.Name = "lblNombre";
            lblNombre.Size = new Size(51, 15);
            lblNombre.TabIndex = 2;
            lblNombre.Text = "Nombre";
            // 
            // lblNota
            // 
            lblNota.AutoSize = true;
            lblNota.Location = new Point(43, 144);
            lblNota.Name = "lblNota";
            lblNota.Size = new Size(33, 15);
            lblNota.TabIndex = 3;
            lblNota.Text = "Nota";
            // 
            // textBox1
            // 
            textBox1.Location = new Point(137, 33);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(123, 23);
            textBox1.TabIndex = 4;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(137, 72);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(123, 23);
            textBox2.TabIndex = 5;
            // 
            // textBox3
            // 
            textBox3.Location = new Point(137, 110);
            textBox3.Name = "textBox3";
            textBox3.Size = new Size(123, 23);
            textBox3.TabIndex = 6;
            // 
            // textBox4
            // 
            textBox4.Location = new Point(137, 153);
            textBox4.Name = "textBox4";
            textBox4.Size = new Size(123, 23);
            textBox4.TabIndex = 7;
            // 
            // tbnAgregar
            // 
            tbnAgregar.Location = new Point(35, 223);
            tbnAgregar.Name = "tbnAgregar";
            tbnAgregar.Size = new Size(98, 25);
            tbnAgregar.TabIndex = 8;
            tbnAgregar.Text = "Agregar";
            tbnAgregar.UseVisualStyleBackColor = true;
            // 
            // btnEliminar
            // 
            btnEliminar.Location = new Point(162, 223);
            btnEliminar.Name = "btnEliminar";
            btnEliminar.Size = new Size(98, 25);
            btnEliminar.TabIndex = 9;
            btnEliminar.Text = "Eliminar";
            btnEliminar.UseVisualStyleBackColor = true;
            // 
            // btnConsultar
            // 
            btnConsultar.Location = new Point(282, 223);
            btnConsultar.Name = "btnConsultar";
            btnConsultar.Size = new Size(98, 25);
            btnConsultar.TabIndex = 10;
            btnConsultar.Text = "Consultar";
            btnConsultar.UseVisualStyleBackColor = true;
            // 
            // btnModificarNota
            // 
            btnModificarNota.Location = new Point(406, 223);
            btnModificarNota.Name = "btnModificarNota";
            btnModificarNota.Size = new Size(98, 25);
            btnModificarNota.TabIndex = 11;
            btnModificarNota.Text = "Modificar Nota";
            btnModificarNota.UseVisualStyleBackColor = true;
            // 
            // btnMostarAprobados
            // 
            btnMostarAprobados.Location = new Point(529, 223);
            btnMostarAprobados.Name = "btnMostarAprobados";
            btnMostarAprobados.Size = new Size(130, 25);
            btnMostarAprobados.TabIndex = 12;
            btnMostarAprobados.Text = "Mostar Aprobados";
            btnMostarAprobados.UseVisualStyleBackColor = true;
            // 
            // btnMostrarSuspenso
            // 
            btnMostrarSuspenso.Location = new Point(63, 284);
            btnMostrarSuspenso.Name = "btnMostrarSuspenso";
            btnMostrarSuspenso.Size = new Size(138, 25);
            btnMostrarSuspenso.TabIndex = 13;
            btnMostrarSuspenso.Text = "Mostrar Suspenso";
            btnMostrarSuspenso.UseVisualStyleBackColor = true;
            // 
            // btnCandidatosMH
            // 
            btnCandidatosMH.Location = new Point(235, 284);
            btnCandidatosMH.Name = "btnCandidatosMH";
            btnCandidatosMH.Size = new Size(98, 25);
            btnCandidatosMH.TabIndex = 14;
            btnCandidatosMH.Text = "CandidatosMH";
            btnCandidatosMH.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
           
        }
    }
}