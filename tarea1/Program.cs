// See https://aka.ms/new-console-template for more information
// Programa en C# para imprimir los números pares dentro de los 100 primeros números enteros

using System; // Espacio de nombres que proporciona acceso a funcionalidades básicas como la consola

class Program
{
    static void Main()
    {
        // Declaración de una variable para controlar el recorrido de los números
        int numero;

        // Bucle que comienza desde 1 y recorre hasta 100
        for (numero = 1; numero <= 100; numero++) // Incremento de 1 en cada iteración
        {
            // Verifica si el número actual es divisible entre 2, es decir, si es par
            if (numero % 2 == 0) // La condición verifica que el resto de la división sea 0
            {
                // Imprime el número en la consola si es par
                Console.WriteLine(numero);
            }
        }

        // Pausa opcional para mantener la consola abierta y permitir visualizar la salida
        Console.ReadLine();
    }
}
