using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GestorCalificaciones
{
    public class AlumnoManager : IAlumnoManager
    {
        private List<Alumno> alumnos = new List<Alumno>();

        public void AgregarAlumno(Alumno alumno)
        {
            if (!alumnos.Any(a => a.DNI == alumno.DNI))
                alumnos.Add(alumno);
            else
                throw new Exception("El alumno con este DNI ya existe.");
        }

        public void EliminarAlumno(string dni)
        {
            var alumno = alumnos.FirstOrDefault(a => a.DNI == dni);
            if (alumno != null) alumnos.Remove(alumno);
        }

        public Alumno ConsultarAlumno(string dni)
        {
            return alumnos.FirstOrDefault(a => a.DNI == dni);
        }

        public void ModificarNota(string dni, double nuevaNota)
        {
            var alumno = ConsultarAlumno(dni);
            alumno?.ModificarNota(nuevaNota);
        }

        public List<Alumno> ObtenerAlumnos(bool aprobados)
        {
            return aprobados ? alumnos.Where(a => a.Nota >= 5).ToList() : alumnos.Where(a => a.Nota < 5).ToList();
        }

        public List<Alumno> ObtenerCandidatosMH()
        {
            return alumnos.Where(a => a.Nota == 10).ToList();
        }
    }
}