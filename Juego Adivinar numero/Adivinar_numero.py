import tkinter as tk
import random

# Función para iniciar un nuevo juego
def start_new_game():
    global number_to_guess, attempts_left
    number_to_guess = random.randint(1, 100)  # Número aleatorio entre 1 y 100
    attempts_left = 10  # Número máximo de intentos
    attempts_label.config(text=f"Intentos restantes: {attempts_left}")
    feedback_label.config(text="¡Adivina el número!", fg="black")
    guess_entry.delete(0, tk.END)  # Limpiar el campo de entrada
    guess_button.config(state=tk.NORMAL)  # Habilitar el botón de adivinación

# Función para manejar el intento del jugador
def make_guess():
    global attempts_left
    try:
        user_guess = int(guess_entry.get())
    except ValueError:
        feedback_label.config(text="Por favor ingresa un número válido.", fg="red")
        return

    if user_guess < 1 or user_guess > 100:
        feedback_label.config(text="El número debe estar entre 1 y 100.", fg="red")
        return

    attempts_left -= 1
    attempts_label.config(text=f"Intentos restantes: {attempts_left}")

    if user_guess == number_to_guess:
        feedback_label.config(text="¡Correcto! Has adivinado el número.", fg="green")
        guess_button.config(state=tk.DISABLED)
    elif user_guess < number_to_guess:
        feedback_label.config(text="Demasiado bajo. Intenta con un número más alto.", fg="blue")
    else:
        feedback_label.config(text="Demasiado alto. Intenta con un número más bajo.", fg="blue")

    if attempts_left == 0:
        feedback_label.config(text=f"Has perdido. El número correcto era {number_to_guess}.", fg="red")
        guess_button.config(state=tk.DISABLED)

# Crear la ventana principal
root = tk.Tk()
root.title("Juego Adivinar el Número")
root.geometry("400x350")
root.configure(bg="#f0f8ff")

# Crear un marco para centrar los elementos
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(expand=True)

# Etiquetas y campos de entrada
title_label = tk.Label(frame, text="¡Bienvenido al juego de adivinar el número!", font=("Arial", 16), bg="#f0f8ff", fg="#333")
title_label.pack(pady=10)

instructions_label = tk.Label(frame, text="Adivina un número entre 1 y 100:", font=("Arial", 12), bg="#f0f8ff")
instructions_label.pack(pady=5)

guess_entry = tk.Entry(frame, font=("Arial", 14), justify="center")
guess_entry.pack(pady=10)

feedback_label = tk.Label(frame, text="¡Adivina el número!", font=("Arial", 12), bg="#f0f8ff", fg="black")
feedback_label.pack(pady=10)

attempts_label = tk.Label(frame, text="Intentos restantes: 10", font=("Arial", 12), bg="#f0f8ff", fg="#333")
attempts_label.pack(pady=5)

# Botón para hacer un intento
guess_button = tk.Button(frame, text="Adivinar", font=("Arial", 12), bg="#87ceeb", fg="white", command=make_guess)
guess_button.pack(pady=10)

# Botón para reiniciar el juego
restart_button = tk.Button(frame, text="Reiniciar Juego", font=("Arial", 12), bg="#ffa07a", fg="white", command=start_new_game)
restart_button.pack(pady=10)

# Iniciar el juego
start_new_game()

# Ejecutar la aplicación
root.mainloop()
