// See https://aka.ms/new-console-template for more information
// Programa en C# para imprimir los números del 1 al 50 con reglas específicas:
// - "Fizz" para números divisibles por 3
// - "Buzz" para números divisibles por 5
// - "FizzBuzz" para números divisibles por 3 y 5
// - El número mismo para todos los demás casos

using System; // Espacio de nombres necesario para utilizar la consola

class FizzBuzz // Nombre de la clase que contiene el programa principal
{
    static void Main()
    {
        // Bucle para iterar desde 1 hasta 50
        for (int numero = 1; numero <= 50; numero++) // Comienza en 1 y termina en 50
        {
            // Verifica si el número es divisible entre 3 y 5 (15)
            if (numero % 3 == 0 && numero % 5 == 0)
            {
                Console.WriteLine("FizzBuzz"); // Imprime "FizzBuzz" si cumple la condición
            }
            // Verifica si el número es divisible únicamente entre 3
            else if (numero % 3 == 0)
            {
                Console.WriteLine("Fizz"); // Imprime "Fizz" si cumple la condición
            }
            // Verifica si el número es divisible únicamente entre 5
            else if (numero % 5 == 0)
            {
                Console.WriteLine("Buzz"); // Imprime "Buzz" si cumple la condición
            }
            // Si no cumple ninguna de las condiciones anteriores
            else
            {
                Console.WriteLine(numero); // Imprime el número actual
            }
        }

        // Pausa opcional para mantener la consola abierta y visualizar la salida
        Console.ReadLine();
    }
}
