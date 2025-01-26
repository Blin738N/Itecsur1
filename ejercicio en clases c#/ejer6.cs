// See https://aka.ms/new-console-template for more information

using System;

class ProgramaDeterminarSiPuedeVotar
{
    static void Main(string[] args)
    {
        // Declaración de la variable para almacenar la edad ingresada por el usuario
        int edad;

        // Mostrar mensaje de bienvenida al programa
        Console.WriteLine("Programa para determinar si tienes la edad suficiente para votar.");

        // Solicitar al usuario que introduzca su edad
        Console.Write("Por favor, introduce tu edad: ");

        // Validar si la entrada del usuario es un número entero válido
        if (int.TryParse(Console.ReadLine(), out edad))
        {
            // Verificar si la edad es mayor o igual a 18
            if (edad >= 18)
            {
                // Si la edad es suficiente, mostrar mensaje indicando que puede votar
                Console.WriteLine("Tienes la edad suficiente para votar. ¡Puedes votar!");
            }
            else
            {
                // Si la edad es menor a 18, mostrar mensaje indicando que no puede votar
                Console.WriteLine("No tienes la edad suficiente para votar. Debes tener al menos 18 años.");
            }
        }
        else
        {
            // Manejar el caso en el que la entrada no sea un número entero válido
            Console.WriteLine("Error: Por favor, introduce un número entero válido para tu edad.");
        }

    }
}

