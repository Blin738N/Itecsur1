using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Formularios
{
    public class Crud
    {
        public List<CualquierNombreClase> lista = new List<CualquierNombreClase>();

        public void agregarObjeto(CualquierNombreClase p)
        {
            lista.Add(p);
        }
        
    }
}
