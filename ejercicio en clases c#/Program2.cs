using System;

namespace piepapeltijera
{
    internal class Program
    {
        static int vidasUsuario = 3;
        static int vidasPc = 3;
        static Random random = new Random(); // Instancia única de Random

        static void Main(string[] args)
        {
            ejercicio();
            mostrarGanador();
        }

        private static void ejercicio()
        {
            /* 1.- Mostrar menú de opciones al jugador.
             * 2.- Recuperar la opción del jugador.
             * 3.- Generar número aleatorio entre 1 y 3 para la PC.
             * 4.- Comparar y determinar el ganador de la ronda.
             */

            do
            {
                int opcionUsuario = menuOpciones();
                int opcionPc = random.Next(1, 4);
                logicaJuego(opcionUsuario, opcionPc);

                if (vidasUsuario == 0 || vidasPc == 0)
                {
                    break;
                }

            } while (true);
        }

        private static int menuOpciones()
        {
            int opcion;
            do
            {
                Console.WriteLine("Elige una opción:\n" +
                                  "1. Piedra\n" +
                                  "2. Papel\n" +
                                  "3. Tijera");

                if (int.TryParse(Console.ReadLine(), out opcion) && opcion >= 1 && opcion <= 3)
                {
                    return opcion;
                }
                else
                {
                    Console.WriteLine("Entrada no válida. Por favor, ingresa 1, 2 o 3.");
                }

            } while (true);
        }

        private static void logicaJuego(int a, int b)
        {
            // Mapeo de opciones para mostrar los nombres
            string[] opciones = { "Piedra", "Papel", "Tijera" };
            Console.WriteLine($"Usuario eligió: {opciones[a - 1]}");
            Console.WriteLine($"PC eligió: {opciones[b - 1]}");

            string resultado;

            if ((a == 1 && b == 3) || (a == 2 && b == 1) || (a == 3 && b == 2))
            {
                resultado = "¡Usuario gana esta ronda!";
                vidasPc--;
            }
            else if (a == b)
            {
                resultado = "¡Empate!";
            }
            else
            {
                resultado = "¡PC gana esta ronda!";
                vidasUsuario--;
            }

            Console.WriteLine(resultado);
            Console.WriteLine($"Vidas restantes - Usuario: {vidasUsuario} | PC: {vidasPc}\n");
        }

        private static void mostrarGanador()
        {
            Console.WriteLine(vidasUsuario == 0 ? "¡PC ha ganado la partida!" : "¡Usuario ha ganado la partida!");
        }
    }
}
