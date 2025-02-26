namespace Formularios
{
    public partial class Form1 : Form
    {
        //Objeto de la clase matematica declarado
        Matematica mat;
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void btnCalcular_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(tbNum1.Text);
            int num2 = int.Parse(tbNum2.Text);
            calcularOperacion();
            mat = new Matematica(num1, num2);

            //Matematica mat = new Matematica(num1, num2);
            //int suma = num1 + num2;

            //MessageBox.Show("La suma es: " + mat.sumar());
            //result.Text = mat.sumar().ToString();
        }

        private void calcularOperacion()
        {
            if (sumar.Checked)
            {
                MessageBox.Show("La suma es: " + mat.sumar());
                result.Text = mat.sumar().ToString();
                mat.sumar();
                //return 1;
            }
            if (restar.Checked)
            {
                //return 2;   
            }
            //return 0;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Persona p = new Persona();
            p.Show();
        }
    }
}
