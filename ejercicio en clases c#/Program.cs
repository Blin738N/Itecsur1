using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tareaenclase1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Ingresa el radio de un circulo");
            double radio = Convert.ToDouble(Console.ReadLine());
            double area = AreaCirculo(radio);

            Console.WriteLine($"El area del circulo es: {area}");

        }

        static double AreaCirculo(double radio)
        {
            double area = 3.14 * radio * radio;
            return area;
        }

    }
}