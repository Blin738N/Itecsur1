import tkinter as tk
from tkinter import messagebox, Text


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Mejorada")
        self.root.geometry("400x500")
        self.create_ui()

    def create_ui(self):
        # Entrada para el resultado
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), justify='right', bg="#f4f4f4")
        self.result_entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

        # Caja de historial
        self.history_text = Text(self.root, height=5, bg="#e0e0e0", state='disabled', font=("Arial", 14))
        self.history_text.grid(row=1, column=0, columnspan=4, pady=5, padx=10, sticky="nsew")

        # Botones
        buttons = [
            '7', '8', '9', '/',  # Fila 1
            '4', '5', '6', '*',  # Fila 2
            '1', '2', '3', '-',  # Fila 3
            'C', '0', '=', '+',  # Fila 4
            'AC'                 # Fila 5
        ]

        # Colores para los botones
        colors = {
            "number": "#ffffff",
            "operator": "#f4a261",
            "equals": "#2a9d8f",
            "clear": "#e63946"
        }

        for i, button in enumerate(buttons):
            row = (i // 4) + 2
            col = i % 4
            bg_color = (
                colors["number"] if button.isdigit() else
                colors["operator"] if button in "+-*/" else
                colors["equals"] if button == "=" else
                colors["clear"]
            )
            b = tk.Button(
                self.root,
                text=button,
                font=("Arial", 18, "bold"),
                bg=bg_color,
                fg="black",
                width=4,
                height=2,
                command=lambda b=button: self.on_button_click(b)
            )
            b.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Ajustar el tamaño de las filas y columnas
        for i in range(6):  # 6 filas (0-5)
            self.root.rowconfigure(i, weight=1)
        for j in range(4):  # 4 columnas (0-3)
            self.root.columnconfigure(j, weight=1)

    def on_button_click(self, button):
        if button in '0123456789':  # Números
            self.result_var.set(self.result_var.get() + button)
        elif button in '+-*/':  # Operadores
            if not self.result_var.get().endswith(tuple('+-*/')):  # Evitar operadores consecutivos
                self.result_var.set(self.result_var.get() + button)
        elif button == 'C':  # Limpiar solo la entrada actual
            self.clear_entry()
        elif button == 'AC':  # Limpiar todo
            self.clear_all()
        elif button == '=':  # Calcular
            self.calculate_result()

    def calculate_result(self):
        try:
            expression = self.result_var.get()
            if '/0' in expression:  # Evitar división por cero
                raise ZeroDivisionError("División por cero no permitida.")
            result = eval(expression)  # Evalúa la expresión
            self.result_var.set(str(result))
            self.add_to_history(expression, result)
        except ZeroDivisionError:
            self.result_var.set("Error")
            messagebox.showerror("Error", "División por cero no permitida.")
        except Exception as e:
            self.result_var.set("Error")
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    def add_to_history(self, expression, result):
        """Agrega el cálculo al historial y lo guarda en un archivo."""
        entry = f"{expression} = {result}\n"

        # Agregar al cuadro de historial
        self.history_text.config(state='normal')
        self.history_text.insert('end', entry)
        self.history_text.config(state='disabled')
        self.history_text.see('end')

        # Guardar en archivo
        with open("historial.txt", "a") as file:
            file.write(entry)

    def clear_all(self):
        """Limpia la pantalla y el historial."""
        self.result_var.set("")
        self.history_text.config(state='normal')
        self.history_text.delete('1.0', 'end')  # Borra todo el historial
        self.history_text.config(state='disabled')

        # Reiniciar el archivo de historial
        with open("historial.txt", "w") as file:
            file.write("")

    def clear_entry(self):
        """Limpia únicamente la entrada actual."""
        self.result_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
