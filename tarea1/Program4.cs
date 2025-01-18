// See https://aka.ms/new-console-template for more information
// Programa en C# para imprimir los números del 1 al 10 utilizando un bucle "while"

using System; // Espacio de nombres necesario para usar la consola

class WhileLoopExample // Nombre de la clase principal del programa
{
    static void Main()
    {
        // Declaración de una variable para controlar el bucle
        int numero = 1; // Inicialización de la variable en 1, que es el valor inicial

        // Bucle "while" que se ejecutará mientras el número sea menor o igual a 10
        while (numero <= 10) // Condición para que el bucle continúe ejecutándose
        {
            // Imprime el valor actual de la variable "numero"
            Console.WriteLine(numero);

            // Incrementa el valor de la variable "numero" en 1 para avanzar al siguiente número
            numero++;
        }

        // Pausa opcional para mantener la consola abierta y permitir visualizar la salida
        Console.ReadLine();
    }
}
