// See https://aka.ms/new-console-template for more information

using System;

class ProgramaAdivinaNumero
{
    static void Main(string[] args)
    {
        // Crear una instancia de la clase Random para generar números aleatorios
        Random generador = new Random();

        // Generar un número aleatorio entre 1 y 100
        int numeroAleatorio = generador.Next(1, 101);

        // Variable para almacenar la suposición del usuario
        int suposicion = 0;

        // Imprimir mensaje de bienvenida
        Console.WriteLine("¡Bienvenido al juego de adivinar el número!");
        Console.WriteLine("He generado un número aleatorio entre 1 y 100.");
        Console.WriteLine("¡Intenta adivinarlo!");

        // Ciclo que continuará hasta que el usuario adivine el número
        while (suposicion != numeroAleatorio)
        {
            // Pedir al usuario que introduzca un número
            Console.Write("Introduce tu suposición: ");

            // Validar si la entrada del usuario es un número válido
            if (int.TryParse(Console.ReadLine(), out suposicion))
            {
                // Comparar la suposición del usuario con el número aleatorio
                if (suposicion < numeroAleatorio)
                {
                    // Si la suposición es menor, dar una pista
                    Console.WriteLine("El número es mayor que tu suposición.");
                }
                else if (suposicion > numeroAleatorio)
                {
                    // Si la suposición es mayor, dar una pista
                    Console.WriteLine("El número es menor que tu suposición.");
                }
                else
                {
                    // Si la suposición es igual, el usuario ha ganado
                    Console.WriteLine("¡Felicidades! Has adivinado el número.");
                }
            }
            else
            {
                // Manejar la entrada inválida del usuario
                Console.WriteLine("Por favor, introduce un número válido.");
            }
        }

        // Mensaje de despedida
        Console.WriteLine("Gracias por jugar. ¡Hasta la próxima!");
    }
}

