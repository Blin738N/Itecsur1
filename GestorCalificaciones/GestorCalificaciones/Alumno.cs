using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GestorCalificaciones
{
    public class Alumno : Persona
    {
        public double Nota { get; private set; }
        public string Calificacion { get; private set; }

        public Alumno(string dni, string apellidos, string nombre, double nota)
        {
            DNI = dni;
            Apellidos = apellidos;
            Nombre = nombre;
            Nota = nota;
            Calificacion = CalcularCalificacion(nota);
        }

        public Alumno(double nota, string calificacion)
        {
            Nota = nota;
            Calificacion = calificacion ?? throw new ArgumentNullException(nameof(calificacion));
        }

        public void ModificarNota(double nuevaNota)
        {
            Nota = nuevaNota;
            Calificacion = CalcularCalificacion(nuevaNota);
        }

        public void ModificarCalificacion(string nuevaCalificacion)
        {
            Calificacion = nuevaCalificacion;
        }

        private string CalcularCalificacion(double nota)
        {
            if (nota < 5) return "SS";
            if (nota < 7) return "AP";
            if (nota < 9) return "NT";
            return "SB";
        }

        public override bool Equals(object? obj)
        {
            return base.Equals(obj);
        }

        public override int GetHashCode()
        {
            return base.GetHashCode();
        }

        public override string? ToString()
        {
            return base.ToString();
        }
    }
}