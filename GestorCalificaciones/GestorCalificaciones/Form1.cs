
using System;
using System.Windows.Forms;

namespace GestorCalificaciones
{
    public class Form1Base : Form
    {
        public Form1Base()
        {
            InitializeBaseComponents();
        }

        protected virtual void InitializeBaseComponents()
        {
            this.Text = "Gestión de Calificaciones";
            this.Size = new System.Drawing.Size(500, 450);
        }
    }
}
