using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Formularios
{
    internal interface Operacion
    {
        int Sumar(int a, int b);
        int Restar(int a, int b);
        int Multiplicar(int a, int b);
        int Modulo(int a, int b);
        double Dividir(int a, int b);
    }

    internal class Matematica : Operacion
    {
        private int num1;
        private int num2;

        public Matematica(int a, int b)
        {
            num1 = a;
            num2 = b;
        }

        public int Sumar()
        {
            return num1 + num2;
        }

        public int Restar()
        {
            return num1 - num2;
        }

        public int Multiplicar()
        {
            return num1 * num2;
        }

        public int Modulo()
        {
            return num1 % num2;
        }

        public double Dividir()
        {
            if (num2 == 0)
            {
                throw new DivideByZeroException("No se puede dividir por cero.");
            }
            return (double)num1 / num2;
        }
    }
}
