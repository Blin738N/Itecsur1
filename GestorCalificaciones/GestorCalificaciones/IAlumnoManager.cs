using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GestorCalificaciones
{
    internal interface IAlumnoManager
    {
        void AgregarAlumno(Alumno alumno);
        void EliminarAlumno(string dni);
        Alumno ConsultarAlumno(string dni);
        void ModificarNota(string dni, double nuevaNota);
        List<Alumno> ObtenerAlumnos(bool aprobados);
        List<Alumno> ObtenerCandidatosMH();
    }
}
    

