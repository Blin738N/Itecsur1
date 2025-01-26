// See https://aka.ms/new-console-template for more information

using System;

class ProgramaDeterminarMayor
{
    static void Main(string[] args)
    {
        // Declaración de variables para almacenar los dos números ingresados por el usuario
        int num1, num2;

        // Mostrar un mensaje de bienvenida al programa
        Console.WriteLine("Programa para determinar cuál de dos números es mayor.");

        // Solicitar al usuario que introduzca el primer número
        Console.Write("Por favor, introduce el primer número: ");

        // Validar si la entrada es un número entero válido
        if (int.TryParse(Console.ReadLine(), out num1))
        {
            // Solicitar al usuario que introduzca el segundo número
            Console.Write("Por favor, introduce el segundo número: ");

            // Validar si la segunda entrada es un número entero válido
            if (int.TryParse(Console.ReadLine(), out num2))
            {
                // Comparar los dos números para determinar cuál es mayor
                if (num1 > num2)
                {
                    // Si el primer número es mayor
                    Console.WriteLine("El número mayor es: " + num1);
                }
                else if (num2 > num1)
                {
                    // Si el segundo número es mayor
                    Console.WriteLine("El número mayor es: " + num2);
                }
                else
                {
                    // Si ambos números son iguales
                    Console.WriteLine("Ambos números son iguales.");
                }
            }
            else
            {
                // Mensaje de error si el segundo valor ingresado no es un número entero válido
                Console.WriteLine("Error: El segundo valor ingresado no es un número entero válido.");
            }
        }
        else
        {
            // Mensaje de error si el primer valor ingresado no es un número entero válido
            Console.WriteLine("Error: El primer valor ingresado no es un número entero válido.");
        }

    }
}

