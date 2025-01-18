// See https://aka.ms/new-console-template for more information
// Programa en C# que crea una clase "Punto" que representa un punto en el plano cartesiano

using System; // Espacio de nombres necesario para usar funcionalidades básicas como la consola

// Definición de la clase "Punto"
class Punto
{
    // Atributos de la clase (coordenadas del punto en el plano cartesiano)
    private double x;
    private double y;

    // Constructor para inicializar los valores de las coordenadas x y y
    public Punto(double x, double y)
    {
        this.x = x;  // Asigna el valor del parámetro 'x' al atributo 'x'
        this.y = y;  // Asigna el valor del parámetro 'y' al atributo 'y'
    }

    // Método para obtener el valor de la coordenada 'x'
    public double ObtenerX()
    {
        return x;
    }

    // Método para establecer el valor de la coordenada 'x'
    public void EstablecerX(double nuevaX)
    {
        x = nuevaX;
    }

    // Método para obtener el valor de la coordenada 'y'
    public double ObtenerY()
    {
        return y;
    }

    // Método para establecer el valor de la coordenada 'y'
    public void EstablecerY(double nuevaY)
    {
        y = nuevaY;
    }

    // Método para mostrar las coordenadas del punto
    public void MostrarCoordenadas()
    {
        Console.WriteLine($"El punto tiene las coordenadas: ({x}, {y})");
    }
}

// Programa principal
class Program
{
    static void Main()
    {
        // Solicitar al usuario que ingrese las coordenadas del punto
        Console.WriteLine("Por favor, ingrese la coordenada x del punto:");
        double x = Convert.ToDouble(Console.ReadLine());  // Leer la coordenada x y convertirla a tipo double

        Console.WriteLine("Por favor, ingrese la coordenada y del punto:");
        double y = Convert.ToDouble(Console.ReadLine());  // Leer la coordenada y y convertirla a tipo double

        // Crear una instancia de la clase Punto con las coordenadas ingresadas
        Punto punto1 = new Punto(x, y);

        // Mostrar las coordenadas del punto
        punto1.MostrarCoordenadas();

        // Cambiar las coordenadas utilizando los métodos setters
        Console.WriteLine("\nModificando las coordenadas del punto...");

        Console.WriteLine("Ingrese una nueva coordenada x:");
        double nuevaX = Convert.ToDouble(Console.ReadLine());
        punto1.EstablecerX(nuevaX);

        Console.WriteLine("Ingrese una nueva coordenada y:");
        double nuevaY = Convert.ToDouble(Console.ReadLine());
        punto1.EstablecerY(nuevaY);

        // Mostrar las nuevas coordenadas del punto
        Console.WriteLine("\nLas nuevas coordenadas del punto son:");
        punto1.MostrarCoordenadas();

        // Pausa para mantener la consola abierta
        Console.ReadLine();
    }
}
