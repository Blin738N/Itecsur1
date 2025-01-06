# Efecto de Gravedad Dinámico en Pygame 🎮⚡
 
Simulación de pelotas cayendo bajo la gravedad con rebotes dinámicos en **Pygame**. ¡Disfruta viendo cómo las pelotas interactúan con la física y la gravedad!

---

## 🌟 **Características Principales**

- **Gravedad Variable:** Cada pelota tiene su propia gravedad aleatoria que afecta su caída.  
- **Rebote Realista:** Las pelotas rebotan sobre el borde inferior con un coeficiente de restitución ajustable.  
- **Generación Dinámica:** Cuando todas las pelotas se detienen, se genera un nuevo conjunto de pelotas con posiciones aleatorias.  
- **Detención Automática:** Las pelotas se detienen cuando su velocidad cae por debajo de un umbral predefinido.  

---

## 🖥️ **Vista Previa del Proyecto**

*Simulación en acción: Pelotas cayendo y rebotando con efectos realistas.*

---

## ⚙️ **Tecnologías Usadas**

- **Python 3.x** – Lenguaje de programación principal.
- **Pygame** – Librería para crear videojuegos.

---

## 📝 **Descripción Técnica**

Este proyecto simula pelotas que caen bajo la influencia de la gravedad. Cada pelota tiene su propia velocidad y gravedad, lo que genera un comportamiento único para cada una. Además, las pelotas rebotan sobre el borde inferior con una física realista.

### `ObjMain` (Clase Principal de Pelota)
- **`__init__(self, x, y, radius=10)`**: Inicializa las pelotas con su posición y propiedades físicas.
- **`step(self)`**: Actualiza la física de la pelota, aplica la gravedad y maneja el rebote.
- **`draw(self, screen)`**: Dibuja la pelota en la pantalla.

### `generar_pelotas()`
Genera pelotas distribuidas uniformemente por la pantalla, cada una con propiedades físicas únicas.

---

## 🛠 **Parámetros de Configuración**

| Parámetro                  | Descripción                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `COEF_RESTITUTION = 0.85`   | Factor de rebote (0 = no rebote, 1 = rebote perfecto).                     |
| `VELOCITY_THRESHOLD = 0.1`  | Velocidad mínima para que la pelota se detenga.                           |
| `FRAME_DELAY = 20`          | Tiempo entre cuadros en milisegundos.                                      |
| `NUM_BOLAS = 11`            | Número de pelotas iniciales.                                               |
| `SPACING = 75`              | Espaciado entre las pelotas generadas.                                     |

---

## 💡 **Personalización**

¡Puedes ajustar la simulación! Cambia los parámetros para personalizar cómo se comportan las pelotas en el juego:

- **`NUM_BOLAS`**: Modifica el número de pelotas iniciales.
- **`SPACING`**: Cambia el espacio entre las pelotas generadas.
- **`COEF_RESTITUTION`**: Ajusta el rebote de las pelotas.
- **`VELOCITY_THRESHOLD`**: Cambia la velocidad mínima para la detención de las pelotas.

---

## 🤝 **Contribuciones**

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, por favor sigue estos pasos:

1. Haz un **fork** del repositorio.
2. Crea una nueva rama con tus cambios: `git checkout -b mi-cambio`.
3. Realiza tus cambios y haz un **commit**: `git commit -am 'Añadir mejoras'`.
4. Haz un **push** a tu rama: `git push origin mi-cambio`.
5. Envía un **pull request** con una descripción detallada.

---

## 📧 **Contacto**

Si tienes preguntas, sugerencias o deseas discutir alguna mejora, no dudes en contactarme:

- Correo: [daves-73@hotmail.com](mailto:daves-73@hotmail.com)
- Twitter: [@Caleb8607](https://twitter.com/@Caleb8607)
- GitHub: [@Blin738N](https://github.com/Blin738N)

---


## 🚀 **¡Que Empiece la Simulación!**

Disfruta viendo las pelotas rebotar y experimenta con diferentes configuraciones de gravedad y rebote.

---

