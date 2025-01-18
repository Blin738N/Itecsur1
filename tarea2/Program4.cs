// See https://aka.ms/new-console-template for more information
// Programa en C# que solicita un número entre 1 y 7 y muestra el día de la semana correspondiente

using System; // Espacio de nombres necesario para usar funcionalidades básicas como la consola

class DiaDeLaSemana // Nombre de la clase que contiene el programa principal
{
    static void Main()
    {
        // Solicita al usuario que ingrese un número entre 1 y 7
        Console.WriteLine("Por favor, ingrese un número del 1 al 7:");

        // Lee la entrada del usuario como una cadena de texto
        string input = Console.ReadLine(); // La entrada se almacena como una cadena

        // Intentamos convertir la cadena de texto a un número entero
        int numero;

        // Validación de entrada: verificamos si la conversión es exitosa
        if (int.TryParse(input, out numero)) // Si la conversión es exitosa, continuamos
        {
            // Evaluamos el número y mostramos el día correspondiente
            switch (numero) // Utilizamos una estructura "switch" para comparar el número
            {
                case 1:
                    Console.WriteLine("Lunes");
                    break;
                case 2:
                    Console.WriteLine("Martes");
                    break;
                case 3:
                    Console.WriteLine("Miércoles");
                    break;
                case 4:
                    Console.WriteLine("Jueves");
                    break;
                case 5:
                    Console.WriteLine("Viernes");
                    break;
                case 6:
                    Console.WriteLine("Sábado");
                    break;
                case 7:
                    Console.WriteLine("Domingo");
                    break;
                default: // Si el número no está entre 1 y 7
                    Console.WriteLine("Número fuera de rango. Por favor, ingrese un número entre 1 y 7.");
                    break;
            }
        }
        else // Si la conversión no es exitosa, significa que la entrada no es un número válido
        {
            Console.WriteLine("Por favor, ingrese un número válido.");
        }

        // Pausa opcional para mantener la consola abierta y permitir visualizar el resultado
        Console.ReadLine();
    }
}
