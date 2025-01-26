// See https://aka.ms/new-console-template for more information


using System;

class ProgramaConversionCalificacion
{
    static void Main(string[] args)
    {
        // Variable para almacenar la calificación numérica ingresada por el usuario
        int calificacion;

        // Mostrar un mensaje de bienvenida
        Console.WriteLine("Programa para convertir una calificación numérica (0-100) a una letra.");

        // Solicitar al usuario que introduzca una calificación
        Console.Write("Por favor, introduce una calificación numérica: ");

        // Validar si la entrada del usuario es un número válido
        if (int.TryParse(Console.ReadLine(), out calificacion))
        {
            // Verificar si la calificación está dentro del rango permitido (0-100)
            if (calificacion >= 0 && calificacion <= 100)
            {
                // Determinar la calificación en letra según el rango numérico
                if (calificacion >= 90)
                {
                    // Si la calificación está entre 90 y 100, asignar letra A
                    Console.WriteLine("La calificación en letra es: A");
                }
                else if (calificacion >= 80)
                {
                    // Si la calificación está entre 80 y 89, asignar letra B
                    Console.WriteLine("La calificación en letra es: B");
                }
                else if (calificacion >= 70)
                {
                    // Si la calificación está entre 70 y 79, asignar letra C
                    Console.WriteLine("La calificación en letra es: C");
                }
                else if (calificacion >= 60)
                {
                    // Si la calificación está entre 60 y 69, asignar letra D
                    Console.WriteLine("La calificación en letra es: D");
                }
                else
                {
                    // Si la calificación está entre 0 y 59, asignar letra F
                    Console.WriteLine("La calificación en letra es: F");
                }
            }
            else
            {
                // Mensaje de error si la calificación está fuera del rango permitido
                Console.WriteLine("Error: La calificación debe estar entre 0 y 100.");
            }
        }
        else
        {
            // Mensaje de error si la entrada no es un número válido
            Console.WriteLine("Error: Por favor, introduce un número entero válido.");
        }

        // Mensaje de despedida
        Console.WriteLine("Gracias por usar el programa. ¡Hasta luego!");
    }
}

