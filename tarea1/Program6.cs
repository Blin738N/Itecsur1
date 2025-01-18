// See https://aka.ms/new-console-template for more information
// Programa en C# para imprimir los números pares dentro de los primeros 100 números enteros utilizando un bucle "while"

using System; // Espacio de nombres necesario para usar la consola

class EvenNumbers // Nombre de la clase que contiene el programa principal
{
    static void Main()
    {
        // Declaración de la variable para controlar el bucle
        int numero = 1; // Inicializamos "numero" en 1, el primer número de la secuencia

        // Bucle "while" que se ejecutará mientras el número sea menor o igual a 100
        while (numero <= 100) // Condición para iterar hasta 100
        {
            // Verifica si el número es par (divisible por 2)
            if (numero % 2 == 0) // La condición comprueba si el número es divisible entre 2 sin residuo
            {
                // Si es par, imprime el número en la consola
                Console.WriteLine(numero); // Muestra el número en la consola
            }

            // Incrementa el número para pasar al siguiente
            numero++; // Aumenta "numero" en 1 en cada iteración
        }

        // Pausa opcional para mantener la consola abierta y permitir visualizar el resultado
        Console.ReadLine();
    }
}
