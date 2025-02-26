using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Formularios
{
    class Matematica : Operacion
    {
        private int num1;
        private int num2;

        public Matematica(int num1, int num2)
        {
            this.num1 = num1;
            this.num2 = num2;
        }
        public int sumar()
        {
            return num1 + num2;
        }
        public int restar()
        {
            return num1 - num2:
        }
        public int multiplicar()
        {
            return num1 * num2:

        }
        public int modulo()
        {
            return num1 % num2;
        }
        public double dividir()

        {
            if (num2 == 0)
            {
                throw new DivideByZeroException("No se puede dividir por cero");
            }
            return (double)num1 / num2;
        }
    }
}
