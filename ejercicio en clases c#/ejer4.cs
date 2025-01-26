// See https://aka.ms/new-console-template for more information

using System;

class ProgramaParOImpar
{
    static void Main(string[] args)
    {
        // Declaración de la variable para almacenar el número ingresado por el usuario
        int numero;

        // Mostrar mensaje de bienvenida al programa
        Console.WriteLine("Programa para determinar si un número entero es par o impar.");

        // Solicitar al usuario que introduzca un número entero
        Console.Write("Por favor, introduce un número entero: ");

        // Validar si la entrada del usuario es un número entero válido
        if (int.TryParse(Console.ReadLine(), out numero))
        {
            // Verificar si el número es par utilizando el operador de módulo (%)
            if (numero % 2 == 0)
            {
                // Si el residuo de la división entre 2 es 0, el número es par
                Console.WriteLine("El número " + numero + " es par.");
            }
            else
            {
                // Si el residuo de la división entre 2 no es 0, el número es impar
                Console.WriteLine("El número " + numero + " es impar.");
            }
        }
        else
        {
            // Manejar el caso en el que la entrada no sea un número entero válido
            Console.WriteLine("Error: Por favor, introduce un número entero válido.");
        }

        // Mensaje de despedida
        Console.WriteLine("Gracias por usar el programa. ¡Hasta luego!");
    }
}

