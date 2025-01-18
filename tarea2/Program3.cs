// See https://aka.ms/new-console-template for more information
// Programa en C# que solicita un número y determina en qué rango se encuentra

using System; // Espacio de nombres necesario para usar funcionalidades básicas como la consola

class RangoNumero // Nombre de la clase que contiene el programa principal
{
    static void Main()
    {
        // Solicita al usuario que ingrese un número
        Console.WriteLine("Por favor, ingrese un número:");

        // Lee la entrada del usuario como una cadena de texto
        string input = Console.ReadLine(); // La entrada se almacena como una cadena

        // Intentamos convertir la cadena de texto a un número entero
        int numero;

        // Validación de entrada: verificamos si la conversión es exitosa
        if (int.TryParse(input, out numero)) // Si la conversión es exitosa, continuamos
        {
            // Evaluamos el rango del número ingresado
            if (numero < 10) // Si el número es menor que 10
            {
                Console.WriteLine("El número es menor que 10.");
            }
            else if (numero >= 10 && numero <= 20) // Si el número está entre 10 y 20 (inclusive)
            {
                Console.WriteLine("El número está entre 10 y 20.");
            }
            else // Si el número es mayor que 20
            {
                Console.WriteLine("El número es mayor que 20.");
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
