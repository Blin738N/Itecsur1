// See https://aka.ms/new-console-template for more information
using System;

class Program
{
    static void Main()
    {
        // Variable para almacenar el número ingresado por el usuario
        double numero;

        // Solicitar al usuario que ingrese un número
        Console.WriteLine("Por favor, ingresa un número:");

        // Intentamos leer la entrada del usuario y convertirla a un número
        bool esNumeroValido = double.TryParse(Console.ReadLine(), out numero);

        // Verificamos si la conversión fue exitosa
        if (esNumeroValido)
        {
            // Comprobamos en qué rango se encuentra el número
            if (numero < 10)
            {
                Console.WriteLine("El número es menor que 10.");
            }
            else if (numero >= 10 && numero <= 20)
            {
                Console.WriteLine("El número está entre 10 y 20.");
            }
            else
            {
                Console.WriteLine("El número es mayor que 20.");
            }
        }
        else
        {
            // Si la entrada no es un número válido, mostramos un mensaje de error
            Console.WriteLine("Error: Por favor ingresa un número válido.");
        }

        // Pausa para visualizar el resultado (opcional)
        Console.ReadLine();
    }
}
