using System;
using System.Windows.Forms;

namespace GestorCalificaciones
{
    static class Program
    {
        [STAThread]
        static void Main(Form1 form1)
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

#if NET6_0_OR_GREATER
            ApplicationConfiguration.Initialize();
#endif

            Application.Run(form1); // Corrección: Sin el punto antes de Form1()
        }
    }
}