using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Formularios
{
    public partial class Persona : Form
    {
        Crud crud = new Crud();
        public Persona()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            //recuperando el nombre del usuario
            string nombre = cualquiernombre1.Text;
            //recuperando la edad del usuario
            int edad = int.Parse(cualquiernombredelavariable2.Text);

            CualquierNombreClase p = new CualquierNombreClase(nombre, edad);
            //Crud crud = new Crud();
            crud.agregarObjeto(p);
            MessageBox.Show("Registro Correcto");

        }

        private void btnMostrarLista_Click(object sender, EventArgs e)
        {
            Crud crud = new Crud();
            foreach (var p in crud.lista)
            {
                MessageBox.Show(p.nombre);
            }
        }
    }
}
