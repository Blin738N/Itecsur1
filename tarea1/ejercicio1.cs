// See https://aka.ms/new-console-template for more information


using System;

class Program
{
    static void Main()
    {
        // Variable única para recorrer y controlar los números
        int numero;

        // Bucle para iterar desde 2 hasta 100 con incrementos de 2 (solo números pares)
        for (numero = 2; numero <= 100; numero += 2) // Incremento de 2 en cada iteración
        {
            Console.WriteLine(numero); // Imprime el número actual
        }

        // Pausa opcional para ver el resultado en consola (opcional)
        Console.ReadLine();
    }
}

