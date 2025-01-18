// See https://aka.ms/new-console-template for more information
// Programa en C# para evaluar si un número ingresado por el usuario es positivo, negativo o cero

using System; // Espacio de nombres necesario para utilizar funcionalidades básicas como la consola

class EvaluarNumero // Nombre de la clase que contiene el programa principal
{
    static void Main()
    {
        // Solicita al usuario que ingrese un número
        Console.WriteLine("Por favor, ingrese un número:");

        // Intentamos leer la entrada del usuario y convertirla en un número entero
        string input = Console.ReadLine(); // Lee la entrada del usuario como una cadena de texto

        // Intentamos convertir la cadena de texto a un número entero
        int numero;

        // Validación de entrada: verificamos si la conversión es exitosa
        if (int.TryParse(input, out numero)) // Si la conversión es exitosa, continuamos
        {
            // Evaluamos si el número es positivo, negativo o cero
            if (numero > 0) // Si el número es mayor que 0
            {
                Console.WriteLine("El número es positivo.");
            }
            else if (numero < 0) // Si el número es menor que 0
            {
                Console.WriteLine("El número es negativo.");
            }
            else // Si el número es igual a 0
            {
                Console.WriteLine("El número es cero.");
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
