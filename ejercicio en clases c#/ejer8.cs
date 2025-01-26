// See https://aka.ms/new-console-template for more information

using System;

class Program
{
    static void Main()
    {
        // Solicitar la calificación numérica al usuario
        Console.Write("Ingrese la calificación numérica del estudiante: ");
        string input = Console.ReadLine();

        // Intentar convertir la entrada a un número
        if (double.TryParse(input, out double calificacion))
        {
            // Determinar la letra equivalente usando switch
            char letraCalificacion;

            switch (calificacion)
            {
                case double n when (n >= 90 && n <= 100):
                    letraCalificacion = 'A';
                    break;
                case double n when (n >= 80 && n < 90):
                    letraCalificacion = 'B';
                    break;
                case double n when (n >= 70 && n < 80):
                    letraCalificacion = 'C';
                    break;
                case double n when (n >= 60 && n < 70):
                    letraCalificacion = 'D';
                    break;
                case double n when (n < 60 && n >= 0):
                    letraCalificacion = 'F';
                    break;
                default:
                    Console.WriteLine("La calificación ingresada no es válida. Debe estar entre 0 y 100.");
                    return; // Termina el programa si la calificación es inválida
            }

            // Mostrar el resultado
            Console.WriteLine($"La calificación equivalente es: {letraCalificacion}");
        }
        else
        {
            Console.WriteLine("Entrada no válida. Por favor, ingrese un número.");
        }
    }
}

