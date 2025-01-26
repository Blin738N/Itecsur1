// See https://aka.ms/new-console-template for more information


using System;

class ProgramaEdadParaVotar
{
    static void Main(string[] args)
    {
        // Declaración de la variable para almacenar la edad del usuario
        int edad;

        // Mensaje de bienvenida al programa
        Console.WriteLine("Programa para determinar si puedes votar.");

        // Solicitar al usuario que introduzca su edad
        Console.Write("Por favor, introduce tu edad: ");

        // Validar si la entrada es un número entero válido
        if (int.TryParse(Console.ReadLine(), out edad))
        {
            // Verificar si la edad es mayor o igual a 18
            if (edad >= 18)
            {
                // Si la edad es suficiente, informar que puede votar
                Console.WriteLine("¡Tienes derecho a votar!");
            }
            else
            {
                // Si la edad es menor, informar que no puede votar
                Console.WriteLine("No puedes votar, debes tener al menos 18 años.");
            }
        }
        else
        {
            // Manejar la entrada no válida del usuario
            Console.WriteLine("Entrada no válida. Por favor, introduce un número entero para tu edad.");
        }

        // Mensaje de despedida
        Console.WriteLine("Gracias por usar el programa. ¡Hasta luego!");
    }
}

