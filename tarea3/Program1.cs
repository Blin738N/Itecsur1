// See https://aka.ms/new-console-template for more information
// Programa en C# que crea una clase "Persona" con atributos y permite al usuario ingresar los valores

using System; // Espacio de nombres necesario para usar funcionalidades básicas como la consola

// Definición de la clase "Persona"
class Persona
{
    // Atributos de la clase
    private string nombre;
    private int edad;
    private string dni;

    // Constructor para inicializar los atributos de la persona
    public Persona(string nombre, int edad, string dni)
    {
        this.nombre = nombre;
        this.edad = edad;
        this.dni = dni;
    }

    // Método para obtener el valor del atributo 'nombre'
    public string ObtenerNombre()
    {
        return nombre;
    }

    // Método para establecer el valor del atributo 'nombre'
    public void EstablecerNombre(string nuevoNombre)
    {
        nombre = nuevoNombre;
    }

    // Método para obtener el valor del atributo 'edad'
    public int ObtenerEdad()
    {
        return edad;
    }

    // Método para establecer el valor del atributo 'edad'
    public void EstablecerEdad(int nuevaEdad)
    {
        edad = nuevaEdad;
    }

    // Método para obtener el valor del atributo 'dni'
    public string ObtenerDNI()
    {
        return dni;
    }

    // Método para establecer el valor del atributo 'dni'
    public void EstablecerDNI(string nuevoDNI)
    {
        dni = nuevoDNI;
    }

    // Método para mostrar la información de la persona
    public void MostrarInformacion()
    {
        Console.WriteLine("Nombre: " + nombre);
        Console.WriteLine("Edad: " + edad);
        Console.WriteLine("DNI: " + dni);
    }
}

// Programa principal
class Program
{
    static void Main()
    {
        // Solicitar al usuario que ingrese los datos
        Console.WriteLine("Por favor, ingrese el nombre de la persona:");
        string nombre = Console.ReadLine();

        Console.WriteLine("Por favor, ingrese la edad de la persona:");
        int edad;
        while (!int.TryParse(Console.ReadLine(), out edad)) // Validar que la edad sea un número entero
        {
            Console.WriteLine("Entrada no válida. Por favor, ingrese una edad válida (número entero):");
        }

        Console.WriteLine("Por favor, ingrese el DNI de la persona:");
        string dni = Console.ReadLine();

        // Crear una instancia de la clase Persona con los valores ingresados por el usuario
        Persona persona1 = new Persona(nombre, edad, dni);

        // Mostrar la información de la persona
        persona1.MostrarInformacion();

        // Pausa para visualizar los resultados
        Console.ReadLine();
    }
}
