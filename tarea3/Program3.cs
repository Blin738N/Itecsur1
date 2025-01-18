// See https://aka.ms/new-console-template for more information
// Programa en C# que crea una clase "Circulo" que representa un círculo en el plano cartesiano

using System; // Espacio de nombres necesario para usar funcionalidades básicas como la consola

// Definición de la clase "Circulo"
class Circulo
{
    // Atributos de la clase
    private double x;       // Coordenada x del centro del círculo
    private double y;       // Coordenada y del centro del círculo
    private double radio;   // Radio del círculo

    // Constructor para inicializar las coordenadas del centro y el radio
    public Circulo(double x, double y, double radio)
    {
        this.x = x;       // Asigna el valor del parámetro 'x' al atributo 'x'
        this.y = y;       // Asigna el valor del parámetro 'y' al atributo 'y'
        this.radio = radio;  // Asigna el valor del parámetro 'radio' al atributo 'radio'
    }

    // Método para obtener la coordenada 'x' del centro del círculo
    public double ObtenerX()
    {
        return x;
    }

    // Método para establecer la coordenada 'x' del centro del círculo
    public void EstablecerX(double nuevaX)
    {
        x = nuevaX;
    }

    // Método para obtener la coordenada 'y' del centro del círculo
    public double ObtenerY()
    {
        return y;
    }

    // Método para establecer la coordenada 'y' del centro del círculo
    public void EstablecerY(double nuevaY)
    {
        y = nuevaY;
    }

    // Método para obtener el valor del radio del círculo
    public double ObtenerRadio()
    {
        return radio;
    }

    // Método para establecer el valor del radio del círculo
    public void EstablecerRadio(double nuevoRadio)
    {
        radio = nuevoRadio;
    }

    // Método para calcular el área del círculo (Área = π * radio^2)
    public double CalcularArea()
    {
        return Math.PI * Math.Pow(radio, 2);  // Utiliza Math.PI para obtener el valor de π
    }

    // Método para mostrar la información del círculo
    public void MostrarInformacion()
    {
        Console.WriteLine($"Centro del círculo: ({x}, {y})");
        Console.WriteLine($"Radio: {radio}");
        Console.WriteLine($"Área del círculo: {CalcularArea()}");
    }
}

// Programa principal
class Program
{
    static void Main()
    {
        // Solicitar al usuario que ingrese las coordenadas del centro y el radio
        Console.WriteLine("Por favor, ingrese la coordenada x del centro del círculo:");
        double x = Convert.ToDouble(Console.ReadLine());  // Leer la coordenada x y convertirla a tipo double

        Console.WriteLine("Por favor, ingrese la coordenada y del centro del círculo:");
        double y = Convert.ToDouble(Console.ReadLine());  // Leer la coordenada y y convertirla a tipo double

        Console.WriteLine("Por favor, ingrese el radio del círculo:");
        double radio = Convert.ToDouble(Console.ReadLine());  // Leer el radio y convertirlo a tipo double

        // Crear una instancia de la clase Circulo con los valores ingresados
        Circulo circulo1 = new Circulo(x, y, radio);

        // Mostrar la información del círculo
        circulo1.MostrarInformacion();

        // Pausa para mantener la consola abierta
        Console.ReadLine();
    }
}
