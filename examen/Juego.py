import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
screen = pygame.display.set_mode((800, 600))  # Tamaño de la ventana
pygame.display.set_caption("Efecto de gravedad dinámico By: Roberto Constante")  # Mensaje en la ventana

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Constantes globales
COEF_RESTITUTION = 0.85  # Factor de rebote
VELOCITY_THRESHOLD = 0.1  # Velocidad mínima para detener la pelota
FRAME_DELAY = 20  # Tiempo entre cuadros en milisegundos
NUM_BOLAS = 11  # Número inicial de pelotas
SPACING = 75  # Espaciado entre pelotas

# Clase principal del juego
class ObjMain:
    def __init__(self, x, y, radius=10):
        # Inicialización de las propiedades de la pelota
        self.x = x
        self.y = y
        self.radius = radius
        self.fy = random.uniform(-1, 1)  # Velocidad inicial aleatoria
        self.gravity = random.uniform(0.05, 0.15)  # Gravedad única para cada pelota
        self.stopped = False  # Indica si la pelota está detenida

    def step(self):
        if self.stopped:
            return  # Si está detenida, no actualizar

        # Aplicar gravedad a la velocidad vertical
        self.fy += self.gravity

        # Actualizar posición vertical
        self.y += self.fy

        # Rebotar al tocar el borde inferior
        if self.y + self.radius >= screen.get_height():
            self.y = screen.get_height() - self.radius  # Asegurar que no pase el borde
            self.fy = -self.fy * COEF_RESTITUTION  # Invertir y reducir velocidad

            # Detener la pelota si la velocidad es menor al umbral
            if abs(self.fy) < VELOCITY_THRESHOLD:
                self.fy = 0
                self.stopped = True  # Marcar como detenida

    def draw(self, screen):
        # Dibujar la pelota en pantalla
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

# Función para generar un nuevo conjunto de pelotas
def generar_pelotas():
    centro_x = screen.get_width() // 2  # Coordenada X central
    centro_y = screen.get_height() // 4  # Coordenada Y inicial (más arriba)
    return [
        ObjMain(
            centro_x - (NUM_BOLAS // 2) * SPACING + i * SPACING,  # Posición X
            centro_y  # Posición Y inicial
        )
        for i in range(NUM_BOLAS)
    ]

# Generar el primer conjunto de pelotas
pelotas = generar_pelotas()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Cerrar la ventana
            running = False

    # Actualizar lógica de cada pelota
    for pelota in pelotas:
        pelota.step()

    # Verificar si todas las pelotas están detenidas
    if all(pelota.stopped for pelota in pelotas):
        pelotas = generar_pelotas()  # Generar nuevas pelotas cuando todas estén detenidas

    # Dibujar en pantalla
    screen.fill(BLACK)  # Limpiar pantalla con color negro
    for pelota in pelotas:
        pelota.draw(screen)  # Dibujar cada pelota

    pygame.display.flip()  # Actualizar pantalla

    # Ralentizar el juego agregando un retraso por cuadro
    pygame.time.delay(FRAME_DELAY)

# Salir del programa
pygame.quit()
sys.exit()
