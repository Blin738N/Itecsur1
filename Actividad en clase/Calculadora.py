

import tkinter as tk
from tkinter import messagebox

def click_boton(valor):
    entrada.insert(tk.END, valor)

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        expresion = entrada.get() # Obtiene la expresion matematica escrita en el campo de entrada
        resultado = eval(expresion)  # Evalúa la expresión matemática
        limpiar() # Limpia el campo de entrada
        entrada.insert(tk.END, str(resultado)) # Muestra el resultado
    except Exception as e:
        messagebox.showerror("Error", "Expresión inválida") # Muestra un mensaje de error

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Crear el campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 20), bd=5, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de la calculadora
botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

fila = 1
columna = 0

for boton in botones:
    if boton == "=":
        b = tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                      bg="#4CAF50", fg="white", command=calcular)
    elif boton == "C":
        b = tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                      bg="#f44336", fg="white", command=limpiar)
    else:
        b = tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                      command=lambda valor=boton: click_boton(valor))
    
    b.grid(row=fila, column=columna, padx=5, pady=5)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Iniciar la aplicación
ventana.mainloop()
