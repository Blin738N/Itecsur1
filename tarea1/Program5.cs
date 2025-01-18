// See https://aka.ms/new-console-template for more information
// Programa en C# para calcular la suma de los primeros 100 números enteros utilizando un bucle "while"

using System; // Espacio de nombres necesario para usar la consola

class SumFirst100Numbers // Nombre de la clase que contiene el programa principal
{
    static void Main()
    {
        // Declaración de las variables
        int numero = 1; // Inicialización de la variable en 1, que es el primer número a sumar
        int suma = 0;   // Variable para almacenar la suma total, comenzando en 0

        // Bucle "while" que se ejecutará mientras "numero" sea menor o igual a 100
        while (numero <= 100) // La condición asegura que el bucle recorra desde 1 hasta 100
        {
            // Sumar el número actual al total acumulado en "suma"
            suma += numero; // Es equivalente a: suma = suma + numero;

            // Incrementar el número para avanzar al siguiente número
            numero++; // Aumenta en 1 para pasar al siguiente número en la secuencia
        }

        // Imprime la suma total de los primeros 100 números
        Console.WriteLine("La suma de los primeros 100 números enteros es: " + suma);

        // Pausa opcional para mantener la consola abierta y permitir visualizar el resultado
        Console.ReadLine();
    }
}
