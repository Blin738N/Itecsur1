// See https://aka.ms/new-console-template for more information

using System;

class Program
{
    static void Main()
    {
        // Solicitar al usuario que ingrese un número que representa el día de la semana
        Console.WriteLine("Ingresa un número del 1 al 7 para representar un día de la semana.");

        // Leer el número ingresado por el usuario y convertirlo a entero
        int dia = int.Parse(Console.ReadLine());

        // Usar la sentencia switch para determinar el nombre del día
        switch (dia)
        {
            // Si el número es 1, mostrar "Lunes"
            case 1:
                Console.WriteLine("Lunes");
                break;

            // Si el número es 2, mostrar "Martes"
            case 2:
                Console.WriteLine("Martes");
                break;

            // Si el número es 3, mostrar "Miércoles"
            case 3:
                Console.WriteLine("Miércoles");
                break;

            // Si el número es 4, mostrar "Jueves"
            case 4:
                Console.WriteLine("Jueves");
                break;

            // Si el número es 5, mostrar "Viernes"
            case 5:
                Console.WriteLine("Viernes");
                break;

            // Si el número es 6, mostrar "Sábado"
            case 6:
                Console.WriteLine("Sábado");
                break;

            // Si el número es 7, mostrar "Domingo"
            case 7:
                Console.WriteLine("Domingo");
                break;

            // Si el número no es del 1 al 7, mostrar un mensaje de error
            default:
                Console.WriteLine("Número inválido. Debes ingresar un número entre 1 y 7.");
                break;
        }
    }
}

