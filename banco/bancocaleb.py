import tkinter as tk
from tkinter import messagebox, filedialog, ttk, simpledialog
from PIL import Image, ImageTk, ImageDraw

# Clase que simula una cuenta bancaria
class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial, tipo_cuenta, foto_perfil=None):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo_inicial
        self.tipo_cuenta = tipo_cuenta
        self.transacciones = []
        self.foto_perfil = foto_perfil  # Ruta de la foto de perfil

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            self.transacciones.append(f"Depósito: ${monto:.2f}")
            return True
        return False

    def retirar(self, monto):
        if monto > 0 and self.saldo >= monto:
            self.saldo -= monto
            self.transacciones.append(f"Retiro: ${monto:.2f}")
            return True
        return False

    def transferir(self, cuenta_destino, monto):
        if monto > 0 and self.saldo >= monto:
            self.retirar(monto)
            cuenta_destino.depositar(monto)
            self.transacciones.append(f"Transferencia: ${monto:.2f} a Cuenta {cuenta_destino.numero_cuenta}")
            cuenta_destino.transacciones.append(f"Transferencia recibida: ${monto:.2f} de Cuenta {self.numero_cuenta}")
            return True
        return False

    def mostrar_historial(self):
        return "\n".join(self.transacciones)


class BancoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Caleb - Simulación de Cuenta Bancaria")
        self.root.geometry("600x700")
        self.root.config(bg="#004b87")

        self.cuentas = {}  # Diccionario para almacenar las cuentas bancarias
        self.foto_perfil_ruta = None  # Ruta temporal de la foto seleccionada
        self.create_widgets()

    def create_widgets(self):
        # Título
        self.label_titulo = tk.Label(self.root, text="Bank Caleb", font=("Arial", 24, "bold"), fg="#f1c40f", bg="#004b87", relief="raised", bd=6)
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        # Titular
        self.label_titular = tk.Label(self.root, text="Titular de la Cuenta:", font=("Arial", 12), fg="white", bg="#004b87")
        self.label_titular.grid(row=1, column=0, sticky="e", padx=20)
        self.entry_titular = tk.Entry(self.root, font=("Arial", 12), bg="#ecf0f1", bd=3)
        self.entry_titular.grid(row=1, column=1, padx=20)

        # Número de cuenta
        self.label_numero_cuenta = tk.Label(self.root, text="Número de Cuenta:", font=("Arial", 12), fg="white", bg="#004b87")
        self.label_numero_cuenta.grid(row=2, column=0, sticky="e", padx=20)
        self.entry_numero_cuenta = tk.Entry(self.root, font=("Arial", 12), bg="#ecf0f1", bd=3)
        self.entry_numero_cuenta.grid(row=2, column=1, padx=20)

        # Saldo inicial
        self.label_saldo = tk.Label(self.root, text="Saldo Inicial:", font=("Arial", 12), fg="white", bg="#004b87")
        self.label_saldo.grid(row=3, column=0, sticky="e", padx=20)
        self.entry_saldo = tk.Entry(self.root, font=("Arial", 12), bg="#ecf0f1", bd=3)
        self.entry_saldo.grid(row=3, column=1, padx=20)

        # Tipo de cuenta
        self.label_tipo_cuenta = tk.Label(self.root, text="Tipo de Cuenta:", font=("Arial", 12), fg="white", bg="#004b87")
        self.label_tipo_cuenta.grid(row=4, column=0, sticky="e", padx=20)
        self.tipo_cuenta = ttk.Combobox(self.root, values=["Ahorro", "Corriente"], font=("Arial", 12), state="readonly")
        self.tipo_cuenta.grid(row=4, column=1, padx=20)
        self.tipo_cuenta.set("Ahorro")

        # Foto de perfil
        self.label_foto = tk.Label(self.root, text="Foto de Perfil:", font=("Arial", 12), fg="white", bg="#004b87")
        self.label_foto.grid(row=5, column=0, sticky="e", padx=20)
        self.btn_seleccionar_foto = tk.Button(self.root, text="Seleccionar Foto", font=("Arial", 12), bg="#3498db", fg="white", command=self.seleccionar_foto)
        self.btn_seleccionar_foto.grid(row=5, column=1, pady=10)

        # Crear cuenta
        self.btn_crear_cuenta = tk.Button(self.root, text="Crear Cuenta", font=("Arial", 12, "bold"), bg="#27ae60", fg="white", command=self.crear_cuenta)
        self.btn_crear_cuenta.grid(row=6, column=0, columnspan=2, pady=20)

    def seleccionar_foto(self):
        """Permite seleccionar una foto de perfil desde el sistema de archivos."""
        ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
        if ruta:
            self.foto_perfil_ruta = ruta
            messagebox.showinfo("Foto seleccionada", "La foto de perfil ha sido seleccionada.")

    def crear_cuenta(self):
        titular = self.entry_titular.get().strip()
        if not titular:
            messagebox.showerror("Error", "El titular no puede estar vacío.")
            return

        try:
            numero_cuenta = int(self.entry_numero_cuenta.get())
            saldo_inicial = float(self.entry_saldo.get())
            tipo_cuenta = self.tipo_cuenta.get()

            if numero_cuenta in self.cuentas:
                messagebox.showerror("Error", "El número de cuenta ya existe.")
                return

            cuenta = CuentaBancaria(numero_cuenta, titular, saldo_inicial, tipo_cuenta, self.foto_perfil_ruta)
            self.cuentas[numero_cuenta] = cuenta
            messagebox.showinfo("Éxito", f"Cuenta {numero_cuenta} creada exitosamente.")
            self.mostrar_pantalla_cuenta(cuenta)
            self.limpiar_pantalla_registro()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para los campos.")

    def mostrar_pantalla_cuenta(self, cuenta):
        self.ventana_usuario = tk.Toplevel(self.root)
        self.ventana_usuario.title(f"Cuenta: {cuenta.titular}")
        self.ventana_usuario.geometry("600x500")
        self.ventana_usuario.config(bg="#004b87")

        # Foto de perfil redonda
        if cuenta.foto_perfil:
            img = Image.open(cuenta.foto_perfil)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)

            # Crear la máscara circular
            mask = Image.new('L', img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

            # Aplicar la máscara circular
            img.putalpha(mask)
            foto = ImageTk.PhotoImage(img)

            self.label_foto_usuario = tk.Label(self.ventana_usuario, image=foto, bg="#004b87")
            self.label_foto_usuario.image = foto  # Mantener la referencia
            self.label_foto_usuario.grid(row=0, column=0, pady=20, columnspan=2)

        # Bienvenida
        self.label_bienvenida = tk.Label(self.ventana_usuario, text=f"Bienvenido, {cuenta.titular}", font=("Arial", 18, "bold"), fg="#f1c40f", bg="#004b87")
        self.label_bienvenida.grid(row=1, column=0, columnspan=2, pady=10)

        # Botones de operaciones
        self.btn_depositar = tk.Button(self.ventana_usuario, text="Depositar", font=("Arial", 12), bg="#27ae60", fg="white", command=lambda: self.operar(cuenta, "depositar"))
        self.btn_depositar.grid(row=2, column=0, padx=20, pady=10)

        self.btn_retirar = tk.Button(self.ventana_usuario, text="Retirar", font=("Arial", 12), bg="#e74c3c", fg="white", command=lambda: self.operar(cuenta, "retirar"))
        self.btn_retirar.grid(row=2, column=1, padx=20, pady=10)

        self.btn_transferir = tk.Button(self.ventana_usuario, text="Transferir", font=("Arial", 12), bg="#3498db", fg="white", command=lambda: self.operar(cuenta, "transferir"))
        self.btn_transferir.grid(row=3, column=0, padx=20, pady=10)

        self.btn_historial = tk.Button(self.ventana_usuario, text="Ver Historial", font=("Arial", 12), bg="#9b59b6", fg="white", command=lambda: self.mostrar_historial(cuenta))
        self.btn_historial.grid(row=3, column=1, padx=20, pady=10)

        self.btn_saldo = tk.Button(self.ventana_usuario, text="Consultar Saldo", font=("Arial", 12), bg="#f39c12", fg="white", command=lambda: self.consultar_saldo(cuenta))
        self.btn_saldo.grid(row=4, column=0, columnspan=2, pady=10)

    def operar(self, cuenta, operacion):
        """Función para manejar operaciones de deposito, retiro y transferencia."""
        if operacion == "depositar":
            monto = simpledialog.askfloat("Depositar", "Ingrese el monto a depositar:")
            if monto and cuenta.depositar(monto):
                messagebox.showinfo("Éxito", f"Depósito de ${monto:.2f} realizado con éxito.")
            else:
                messagebox.showerror("Error", "Monto no válido.")
        elif operacion == "retirar":
            monto = simpledialog.askfloat("Retirar", "Ingrese el monto a retirar:")
            if monto and cuenta.retirar(monto):
                messagebox.showinfo("Éxito", f"Retiro de ${monto:.2f} realizado con éxito.")
            else:
                messagebox.showerror("Error", "Monto no válido o saldo insuficiente.")
        elif operacion == "transferir":
            cuenta_destino_numero = simpledialog.askinteger("Transferir", "Ingrese el número de cuenta destino:")
            monto = simpledialog.askfloat("Transferir", "Ingrese el monto a transferir:")

            cuenta_destino = self.cuentas.get(cuenta_destino_numero)
            if cuenta_destino and monto:
                if cuenta.transferir(cuenta_destino, monto):
                    messagebox.showinfo("Éxito", f"Transferencia de ${monto:.2f} realizada con éxito a la cuenta {cuenta_destino_numero}.")
                else:
                    messagebox.showerror("Error", "Transferencia fallida. Verifique el monto o saldo.")
            else:
                messagebox.showerror("Error", "Cuenta destino no válida.")

    def mostrar_historial(self, cuenta):
        historial = cuenta.mostrar_historial()
        if historial:
            messagebox.showinfo(f"Historial de Transacciones de {cuenta.titular}", historial)
        else:
            messagebox.showinfo("Historial", "No hay transacciones registradas.")

    def consultar_saldo(self, cuenta):
        saldo = cuenta.consultar_saldo()
        messagebox.showinfo("Saldo Actual", f"Saldo de {cuenta.titular}: ${saldo:.2f}")

    def limpiar_pantalla_registro(self):
        self.entry_titular.delete(0, tk.END)
        self.entry_numero_cuenta.delete(0, tk.END)
        self.entry_saldo.delete(0, tk.END)
        self.tipo_cuenta.set("Ahorro")
        self.foto_perfil_ruta = None


# Crear la ventana principal
root = tk.Tk()
app = BancoApp(root)
root.mainloop()
