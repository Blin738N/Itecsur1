// See https://aka.ms/new-console-template for more information
// Programa en C# que solicita al usuario ingresar una calificación y muestra un mensaje según la calificación

using System; // Espacio de nombres necesario para usar funcionalidades básicas como la consola

class Calificacion // Nombre de la clase que contiene el programa principal
{
    static void Main()
    {
        // Solicita al usuario que ingrese una calificación
        Console.WriteLine("Por favor, ingrese su calificación:");

        // Lee la entrada del usuario como una cadena de texto
        string input = Console.ReadLine(); // La entrada se almacena como una cadena

        // Intentamos convertir la cadena de texto a un número de tipo float (para permitir decimales)
        float calificacion;

        // Validación de entrada: verificamos si la conversión es exitosa
        if (float.TryParse(input, out calificacion)) // Si la conversión es exitosa, continuamos
        {
            // Evaluamos la calificación y mostramos el mensaje correspondiente
            if (calificacion >= 60) // Si la calificación es mayor o igual a 60
            {
                Console.WriteLine("Aprobado"); // Muestra "Aprobado" si cumple la condición
            }
            else // Si la calificación es menor a 60
            {
                Console.WriteLine("Reprobado"); // Muestra "Reprobado" si cumple la condición
            }
        }
        else // Si la conversión no es exitosa, significa que la entrada no es un número válido
        {
            Console.WriteLine("Por favor, ingrese una calificación válida."); // Mensaje de error si la entrada no es válida
        }

        // Pausa opcional para mantener la consola abierta y permitir visualizar el resultado
        Console.ReadLine();
    }
}
