// See https://aka.ms/new-console-template for more information
// Programa en C# que solicita dos números y una operación para realizarla con la sentencia switch

using System; // Espacio de nombres necesario para usar funcionalidades básicas como la consola

class Operaciones // Nombre de la clase que contiene el programa principal
{
    static void Main()
    {
        // Solicita al usuario que ingrese el primer número
        Console.WriteLine("Por favor, ingrese el primer número:");
        string input1 = Console.ReadLine(); // Lee la entrada del primer número como cadena
        double numero1; // Variable para almacenar el primer número

        // Solicita al usuario que ingrese el segundo número
        Console.WriteLine("Por favor, ingrese el segundo número:");
        string input2 = Console.ReadLine(); // Lee la entrada del segundo número como cadena
        double numero2; // Variable para almacenar el segundo número

        // Intentamos convertir las cadenas de texto a números decimales
        if (double.TryParse(input1, out numero1) && double.TryParse(input2, out numero2)) // Si ambas conversiones son exitosas
        {
            // Solicita al usuario que ingrese la operación a realizar (+, -, *, /)
            Console.WriteLine("Por favor, ingrese la operación (+, -, *, /):");
            string operacion = Console.ReadLine(); // Lee la operación como cadena

            // Evaluamos la operación utilizando un "switch"
            switch (operacion)
            {
                case "+":
                    // Realiza la suma y muestra el resultado
                    Console.WriteLine("El resultado de la suma es: " + (numero1 + numero2));
                    break;
                case "-":
                    // Realiza la resta y muestra el resultado
                    Console.WriteLine("El resultado de la resta es: " + (numero1 - numero2));
                    break;
                case "*":
                    // Realiza la multiplicación y muestra el resultado
                    Console.WriteLine("El resultado de la multiplicación es: " + (numero1 * numero2));
                    break;
                case "/":
                    // Verifica si el segundo número no es 0 para evitar división por cero
                    if (numero2 != 0)
                    {
                        // Realiza la división y muestra el resultado
                        Console.WriteLine("El resultado de la división es: " + (numero1 / numero2));
                    }
                    else
                    {
                        // Si el segundo número es 0, muestra un mensaje de error
                        Console.WriteLine("Error: No se puede dividir entre cero.");
                    }
                    break;
                default:
                    // Si la operación no es válida, muestra un mensaje de error
                    Console.WriteLine("Operación no válida. Por favor, ingrese una operación válida (+, -, *, /).");
                    break;
            }
        }
        else
        {
            // Si no se pudieron convertir los números, muestra un mensaje de error
            Console.WriteLine("Por favor, ingrese números válidos.");
        }

        // Pausa opcional para mantener la consola abierta y permitir visualizar el resultado
        Console.ReadLine();
    }
}
