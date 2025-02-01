using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace area
{
    /* 
    * Crea una función que calcule el área de un círculo dado su radio.
    * La fórmula para calcular el área es A = π × r^2, donde r es el radio.
    */

    internal class Program
    {
        private static int sumaTotal = 0;

        static void Main(string[] args)
        {
            Console.WriteLine("Elija una opción:");
            Console.WriteLine("1. Calcular el área de un círculo");
            Console.WriteLine("2. Sumar números hasta ingresar 0");
            Console.WriteLine("3. Salir");

            int opcion;
            if (!int.TryParse(Console.ReadLine(), out opcion) || opcion < 1 || opcion > 3)
            {
                Console.WriteLine("Opción no válida. Finalizando el programa.");
                return;
            }

            switch (opcion)
            {
                case 1:
                    ejercicio1();
                    break;
                case 2:
                    ejercicio2();
                    break;
                case 3:
                    Console.WriteLine("Programa finalizado.");
                    return;
            }

            Console.WriteLine("Presione cualquier tecla para salir...");
            Console.ReadKey();
        }

        static void ejercicio2()
        {
            Console.WriteLine("Ingrese números para sumar. Ingrese 0 para finalizar.");

            while (true)
            {
                Console.Write("Ingrese un número: ");
                if (int.TryParse(Console.ReadLine(), out int numeroIngresado))
                {
                    if (numeroIngresado == 0) break;
                    agregarNumero(numeroIngresado);
                }
                else
                {
                    Console.WriteLine("Entrada inválida. Intente nuevamente.");
                }
            }

            Console.WriteLine($"La suma total es: {sumaTotal}");
        }

        static void agregarNumero(int numero)
        {
            sumaTotal += numero;
        }

        static double calcularAreaCirculo(float radio)
        {
            return Math.PI * Math.Pow(radio, 2);
        }

        public static void ejercicio1()
        {
            Console.WriteLine("Calcula el área de un círculo");
            Console.Write("Ingrese el radio: ");

            if (float.TryParse(Console.ReadLine(), out float radio) && radio > 0)
            {
                double area = calcularAreaCirculo(radio);
                Console.WriteLine($"El área del círculo es: {area}");
            }
            else
            {
                Console.WriteLine("Entrada inválida. Asegúrese de ingresar un número positivo.");
            }
        }
    }
}