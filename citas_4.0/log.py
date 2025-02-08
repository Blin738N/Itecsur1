import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Variables globales para las ventanas
ventana_actual = None
ventana_login = None

# Crear la base de datos y las tablas (si no existen)
def crear_base_datos():
    conn = sqlite3.connect('citas_medicas.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        usuario TEXT NOT NULL UNIQUE,
        contraseña TEXT NOT NULL
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctores (
        id_doctor INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_doctor TEXT NOT NULL
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS especializaciones (
        id_especializacion INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_especializacion TEXT NOT NULL
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS citas (
        id_cita INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        id_doctor INTEGER NOT NULL,
        id_especializacion INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        hora TEXT NOT NULL,
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
        FOREIGN KEY(id_doctor) REFERENCES doctores(id_doctor),
        FOREIGN KEY(id_especializacion) REFERENCES especializaciones(id_especializacion)
    );
    ''')
    
    conn.commit()
    conn.close()

# Función para centrar la ventana
def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Función para cerrar la ventana actual
def cerrar_ventana_actual():
    global ventana_actual
    if ventana_actual is not None:
        ventana_actual.destroy()

# Función para regresar a la ventana de login
def cerrar_sesion():
    cerrar_ventana_actual()  # Cerrar la ventana actual
    global ventana_login
    ventana_login.deiconify()  # Mostrar la ventana de login

# Función para crear el marco negro
def crear_marco_negro(ventana):
    marco_negro = tk.Frame(ventana, bg="black", padx=10, pady=10)
    marco_negro.pack(fill="both", expand=True, padx=20, pady=20)
    return marco_negro

# Función para loguearse
def login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    conn = sqlite3.connect('citas_medicas.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM usuarios WHERE usuario=? AND contraseña=?', (usuario, contraseña))
    user = cursor.fetchone()
    
    if user:  # Si el usuario existe
        if usuario == "admin":  # Si es admin
            ventana_admin()
        else:
            ventana_usuario(user[0])  # ID del usuario
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    conn.close()
    
    # Limpiar los campos de entrada
    entry_usuario.delete(0, tk.END)
    entry_contraseña.delete(0, tk.END)

# Ventana para Admin
def ventana_admin():
    cerrar_ventana_actual()  # Cerrar la ventana anterior
    global ventana_actual
    ventana_actual = tk.Toplevel()
    ventana_actual.title("Panel de Administración")
    centrar_ventana(ventana_actual, 500, 700)  # Ajustar altura
    ventana_actual.config(bg="#B0E0E6")  # Celeste claro

    marco_negro = crear_marco_negro(ventana_actual)

    frame_admin = tk.Frame(marco_negro, bg="#B0E0E6")
    frame_admin.pack(fill="both", expand=True)

    label_admin = tk.Label(frame_admin, text="Bienvenido, Admin", font=("Arial", 16), bg="#B0E0E6")
    label_admin.pack(pady=20)

    # Crear usuario
    tk.Button(frame_admin, text="Crear Usuario", font=("Arial", 12), command=crear_usuario).pack(pady=10)
    
    # Agendar cita
    tk.Button(frame_admin, text="Agendar Cita", font=("Arial", 12), command=agendar_cita).pack(pady=10)
    
    # Editar cita
    tk.Button(frame_admin, text="Editar Cita", font=("Arial", 12), command=editar_cita).pack(pady=10)
    
    # Eliminar cita
    tk.Button(frame_admin, text="Eliminar Cita", font=("Arial", 12), command=eliminar_cita).pack(pady=10)

    # Botón de cerrar sesión
    tk.Button(frame_admin, text="Cerrar Sesión", font=("Arial", 12), command=cerrar_sesion).pack(pady=20)

# Ventana para el usuario
def ventana_usuario(id_usuario):
    cerrar_ventana_actual()  # Cerrar la ventana anterior
    global ventana_actual
    ventana_actual = tk.Toplevel()
    ventana_actual.title("Mis Citas")
    centrar_ventana(ventana_actual, 500, 700)  # Ajustar altura
    ventana_actual.config(bg="#B0E0E6")  # Celeste claro

    marco_negro = crear_marco_negro(ventana_actual)

    frame_usuario = tk.Frame(marco_negro, bg="#B0E0E6")
    frame_usuario.pack(fill="both", expand=True)

    label_usuario = tk.Label(frame_usuario, text="Mis Citas", font=("Arial", 16), bg="#B0E0E6")
    label_usuario.pack(pady=20)

    # Mostrar las citas del usuario
    conn = sqlite3.connect('citas_medicas.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT doctores.nombre_doctor, especializaciones.nombre_especializacion, citas.fecha, citas.hora 
                      FROM citas
                      JOIN doctores ON citas.id_doctor = doctores.id_doctor
                      JOIN especializaciones ON citas.id_especializacion = especializaciones.id_especializacion
                      WHERE citas.id_usuario = ?''', (id_usuario,))
    citas = cursor.fetchall()

    for cita in citas:
        tk.Label(frame_usuario, text=f"{cita[0]} - {cita[1]} | Fecha: {cita[2]} | Hora: {cita[3]}", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
    
    conn.close()

    # Botón de cerrar sesión
    tk.Button(frame_usuario, text="Cerrar Sesión", font=("Arial", 12), command=cerrar_sesion).pack(pady=20)

# Crear usuario
def crear_usuario():
    ventana_crear_usuario = tk.Toplevel()
    ventana_crear_usuario.title("Crear Usuario")
    centrar_ventana(ventana_crear_usuario, 500, 700)  # Ajustar altura
    ventana_crear_usuario.config(bg="#B0E0E6")  # Celeste claro
    
    marco_negro = crear_marco_negro(ventana_crear_usuario)

    frame_crear_usuario = tk.Frame(marco_negro, bg="#B0E0E6")
    frame_crear_usuario.pack(fill="both", expand=True)
    
    tk.Label(frame_crear_usuario, text="Nombre:", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
    entry_nombre = tk.Entry(frame_crear_usuario, font=("Arial", 12))
    entry_nombre.pack(pady=5)

    tk.Label(frame_crear_usuario, text="Apellido:", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
    entry_apellido = tk.Entry(frame_crear_usuario, font=("Arial", 12))
    entry_apellido.pack(pady=5)

    def guardar_usuario():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        usuario = nombre
        contraseña = nombre + "123"
        
        conn = sqlite3.connect('citas_medicas.db')
        cursor = conn.cursor()
        
        # Verificar si el usuario ya existe
        cursor.execute("SELECT * FROM usuarios WHERE usuario=?", (usuario,))
        if cursor.fetchone():
            messagebox.showerror("Error", "El usuario ya existe")
        else:
            cursor.execute("INSERT INTO usuarios (nombre, apellido, usuario, contraseña) VALUES (?, ?, ?, ?)", (nombre, apellido, usuario, contraseña))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Usuario creado con éxito")
            ventana_crear_usuario.destroy()
    
    tk.Button(frame_crear_usuario, text="Guardar Usuario", font=("Arial", 12), command=guardar_usuario).pack(pady=10)

# Agendar cita
def agendar_cita():
    ventana_agendar = tk.Toplevel()
    ventana_agendar.title("Agendar Cita")
    centrar_ventana(ventana_agendar, 500, 700)  # Ajustar altura
    ventana_agendar.config(bg="#B0E0E6")  # Celeste claro
    
    marco_negro = crear_marco_negro(ventana_agendar)

    frame_agendar = tk.Frame(marco_negro, bg="#B0E0E6")
    frame_agendar.pack(fill="both", expand=True)
    
    conn = sqlite3.connect('citas_medicas.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_usuario, nombre FROM usuarios")
    usuarios = cursor.fetchall()
    lista_usuarios = [usuario[1] for usuario in usuarios]
    combo_usuario = ttk.Combobox(frame_agendar, values=lista_usuarios, font=("Arial", 12))
    combo_usuario.pack(pady=10)
    
    cursor.execute("SELECT id_doctor, nombre_doctor FROM doctores")
    doctores = cursor.fetchall()
    lista_doctores = [doctor[1] for doctor in doctores]
    combo_doctor = ttk.Combobox(frame_agendar, values=lista_doctores, font=("Arial", 12))
    combo_doctor.pack(pady=10)
    
    cursor.execute("SELECT id_especializacion, nombre_especializacion FROM especializaciones")
    especializaciones = cursor.fetchall()
    lista_especializaciones = [especializacion[1] for especializacion in especializaciones]
    combo_especializacion = ttk.Combobox(frame_agendar, values=lista_especializaciones, font=("Arial", 12))
    combo_especializacion.pack(pady=10)
    
    tk.Label(frame_agendar, text="Fecha (YYYY-MM-DD):", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
    entry_fecha = tk.Entry(frame_agendar, font=("Arial", 12))
    entry_fecha.pack(pady=5)

    tk.Label(frame_agendar, text="Hora (HH:MM):", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
    entry_hora = tk.Entry(frame_agendar, font=("Arial", 12))
    entry_hora.pack(pady=5)

    def guardar_cita():
        usuario = combo_usuario.get()
        doctor = combo_doctor.get()
        especializacion = combo_especializacion.get()
        fecha = entry_fecha.get()
        hora = entry_hora.get()
        
        conn = sqlite3.connect('citas_medicas.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id_usuario FROM usuarios WHERE nombre=?", (usuario,))
        id_usuario = cursor.fetchone()[0]

        cursor.execute("SELECT id_doctor FROM doctores WHERE nombre_doctor=?", (doctor,))
        id_doctor = cursor.fetchone()[0]

        cursor.execute("SELECT id_especializacion FROM especializaciones WHERE nombre_especializacion=?", (especializacion,))
        id_especializacion = cursor.fetchone()[0]

        cursor.execute("INSERT INTO citas (id_usuario, id_doctor, id_especializacion, fecha, hora) VALUES (?, ?, ?, ?, ?)", 
                       (id_usuario, id_doctor, id_especializacion, fecha, hora))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Cita agendada con éxito")
        ventana_agendar.destroy()

    tk.Button(frame_agendar, text="Guardar Cita", font=("Arial", 12), command=guardar_cita).pack(pady=10)

# Editar cita
def editar_cita():
    ventana_editar = tk.Toplevel()
    ventana_editar.title("Editar Cita")
    centrar_ventana(ventana_editar, 500, 700)  # Ajustar altura
    ventana_editar.config(bg="#B0E0E6")  # Celeste claro
    
    marco_negro = crear_marco_negro(ventana_editar)

    frame_editar = tk.Frame(marco_negro, bg="#B0E0E6")
    frame_editar.pack(fill="both", expand=True)
    
    conn = sqlite3.connect('citas_medicas.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_cita, fecha, hora FROM citas")
    citas = cursor.fetchall()
    
    citas_list = [(cita[0], f"Fecha: {cita[1]} | Hora: {cita[2]}") for cita in citas]
    combo_cita = ttk.Combobox(frame_editar, values=[cita[1] for cita in citas_list], font=("Arial", 12))
    combo_cita.pack(pady=10)

    # Variables para los campos de entrada
    entry_nombre = None
    entry_apellido = None
    entry_nueva_fecha = None
    entry_nueva_hora = None
    combo_doctor = None
    combo_especializacion = None
    guardar_button = None

    def cargar_datos():
        nonlocal entry_nombre, entry_apellido, entry_nueva_fecha, entry_nueva_hora, combo_doctor, combo_especializacion, guardar_button  # Usar las variables de entrada

        # Limpiar solo los widgets que se agregan al cargar datos
        for widget in frame_editar.winfo_children():
            if isinstance(widget, (tk.Label, tk.Entry, ttk.Combobox)) and widget not in (combo_cita, guardar_button):  # No eliminar el combobox ni el botón de guardar
                widget.destroy()

        cita_seleccionada = combo_cita.get()
        if cita_seleccionada:
            id_cita = [cita[0] for cita in citas_list if cita[1] == cita_seleccionada][0]
            cursor.execute('''SELECT usuarios.id_usuario, usuarios.nombre, usuarios.apellido, doctores.nombre_doctor, especializaciones.nombre_especializacion, citas.fecha, citas.hora 
                              FROM citas
                              JOIN usuarios ON citas.id_usuario = usuarios.id_usuario
                              JOIN doctores ON citas.id_doctor = doctores.id_doctor
                              JOIN especializaciones ON citas.id_especializacion = especializaciones.id_especializacion
                              WHERE citas.id_cita = ?''', (id_cita,))
            datos_cita = cursor.fetchone()
            
            if datos_cita:
                tk.Label(frame_editar, text="Modificar Datos de la Cita", font=("Arial", 14), bg="#B0E0E6").pack(pady=10)

                # Campos para editar nombre y apellido
                tk.Label(frame_editar, text="Nombre:", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
                entry_nombre = tk.Entry(frame_editar, font=("Arial", 12))
                entry_nombre.insert(0, datos_cita[1])  # Establecer el nombre actual
                entry_nombre.pack(pady=5)

                tk.Label(frame_editar, text="Apellido:", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
                entry_apellido = tk.Entry(frame_editar, font=("Arial", 12))
                entry_apellido.insert(0, datos_cita[2])  # Establecer el apellido actual
                entry_apellido.pack(pady=5)

                # Cargar doctores
                cursor.execute("SELECT id_doctor, nombre_doctor FROM doctores")
                doctores = cursor.fetchall()
                lista_doctores = [doctor[1] for doctor in doctores]
                combo_doctor = ttk.Combobox(frame_editar, values=lista_doctores, font=("Arial", 12))
                combo_doctor.set(datos_cita[3])  # Establecer el doctor actual
                combo_doctor.pack(pady=5)

                # Cargar especializaciones
                cursor.execute("SELECT id_especializacion, nombre_especializacion FROM especializaciones")
                especializaciones = cursor.fetchall()
                lista_especializaciones = [especializacion[1] for especializacion in especializaciones]
                combo_especializacion = ttk.Combobox(frame_editar, values=lista_especializaciones, font=("Arial", 12))
                combo_especializacion.set(datos_cita[4])  # Establecer la especialización actual
                combo_especializacion.pack(pady=5)

                tk.Label(frame_editar, text="Fecha (YYYY-MM-DD):", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
                entry_nueva_fecha = tk.Entry(frame_editar, font=("Arial", 12))
                entry_nueva_fecha.insert(0, datos_cita[5])  # Establecer la fecha actual
                entry_nueva_fecha.pack(pady=5)

                tk.Label(frame_editar, text="Hora (HH:MM):", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
                entry_nueva_hora = tk.Entry(frame_editar, font=("Arial", 12))
                entry_nueva_hora.insert(0, datos_cita[6])  # Establecer la hora actual
                entry_nueva_hora.pack(pady=5)

                def guardar_edicion():
                    nueva_nombre = entry_nombre.get()
                    nueva_apellido = entry_apellido.get()
                    nueva_fecha = entry_nueva_fecha.get()
                    nueva_hora = entry_nueva_hora.get()
                    id_doctor = [doctor[0] for doctor in doctores if doctor[1] == combo_doctor.get()][0]
                    id_especializacion = [especializacion[0] for especializacion in especializaciones if especializacion[1] == combo_especializacion.get()][0]

                    # Actualizar el nombre y apellido del usuario
                    cursor.execute("UPDATE usuarios SET nombre=?, apellido=? WHERE id_usuario=?", 
                                   (nueva_nombre, nueva_apellido, datos_cita[0]))
                    # Actualizar la cita seleccionada
                    cursor.execute("UPDATE citas SET id_doctor=?, id_especializacion=?, fecha=?, hora=? WHERE id_cita=?", 
                                   (id_doctor, id_especializacion, nueva_fecha, nueva_hora, id_cita))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Éxito", "Cita actualizada con éxito")
                    ventana_editar.destroy()

                # Crear el botón de guardar
                if guardar_button is None:
                    guardar_button = tk.Button(frame_editar, text="Guardar Edición", font=("Arial", 12), command=guardar_edicion)
                    guardar_button.pack(side=tk.BOTTOM, pady=10)  # Colocar el botón en la parte inferior

    tk.Button(frame_editar, text="Cargar Datos", font=("Arial", 12), command=cargar_datos).pack(pady=10)

# Eliminar cita
def eliminar_cita():
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Cita")
    centrar_ventana(ventana_eliminar, 500, 600)  # Ajustar altura
    ventana_eliminar.config(bg="#B0E0E6")  # Celeste claro
    
    marco_negro = crear_marco_negro(ventana_eliminar)

    frame_eliminar = tk.Frame(marco_negro, bg="#B0E0E6")
    frame_eliminar.pack(fill="both", expand=True)
    
    conn = sqlite3.connect('citas_medicas.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_cita, fecha, hora FROM citas")
    citas = cursor.fetchall()
    
    citas_list = [(cita[0], f"Fecha: {cita[1]} | Hora: {cita[2]}") for cita in citas]
    
    # Combobox para seleccionar la cita
    combo_cita = ttk.Combobox(frame_eliminar, values=[cita[1] for cita in citas_list], font=("Arial", 12))
    combo_cita.pack(pady=10)

    # Botón para cargar datos
    cargar_button = tk.Button(frame_eliminar, text="Cargar Datos", font=("Arial", 12), command=lambda: cargar_datos())
    cargar_button.pack(pady=10)

    # Variable para almacenar el botón de eliminar
    eliminar_button = None

    def cargar_datos():
        nonlocal eliminar_button  # Usar la variable de botón de eliminar

        # Limpiar solo los widgets que se agregan al cargar datos
        for widget in frame_eliminar.winfo_children():
            if isinstance(widget, tk.Label) and widget != combo_cita and widget != cargar_button:  # No eliminar el combobox ni el botón de cargar
                widget.destroy()

        # Eliminar el botón de eliminar anterior si existe
        if eliminar_button is not None:
            eliminar_button.destroy()
            eliminar_button = None  # Reiniciar la referencia

        cita_seleccionada = combo_cita.get()
        if cita_seleccionada:
            id_cita = [cita[0] for cita in citas_list if cita[1] == cita_seleccionada][0]
            cursor.execute('''SELECT usuarios.nombre, usuarios.apellido, doctores.nombre_doctor, especializaciones.nombre_especializacion, citas.fecha, citas.hora 
                              FROM citas
                              JOIN usuarios ON citas.id_usuario = usuarios.id_usuario
                              JOIN doctores ON citas.id_doctor = doctores.id_doctor
                              JOIN especializaciones ON citas.id_especializacion = especializaciones.id_especializacion
                              WHERE citas.id_cita = ?''', (id_cita,))
            datos_cita = cursor.fetchone()
            
            if datos_cita:
                tk.Label(frame_eliminar, text=f"Nombre: {datos_cita[0]}", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
                tk.Label(frame_eliminar, text=f"Apellido: {datos_cita[1]}", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
                tk.Label(frame_eliminar, text=f"Doctor: {datos_cita[2]}", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
                tk.Label(frame_eliminar, text=f"Especialización: {datos_cita[3]}", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
                tk.Label(frame_eliminar, text=f"Fecha: {datos_cita[4]}", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)
                tk.Label(frame_eliminar, text=f"Hora: {datos_cita[5]}", font=("Arial", 12), bg="#B0E0E6").pack(pady=5)

                # Crear el botón de eliminar
                eliminar_button = tk.Button(frame_eliminar, text="Eliminar Cita", font=("Arial", 12), command=lambda: eliminar(id_cita))
                eliminar_button.pack(pady=10)

    def eliminar(id_cita):
        cursor.execute("DELETE FROM citas WHERE id_cita=?", (id_cita,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Cita eliminada con éxito")
        ventana_eliminar.destroy()

# Crear la base de datos si no existe
crear_base_datos()

# Configuración de la ventana principal (login)
ventana_login = tk.Tk()
ventana_login.title("Login")
centrar_ventana(ventana_login, 400, 300)
ventana_login.config(bg="#B0E0E6")  # Celeste claro

marco_negro = crear_marco_negro(ventana_login)

frame_login = tk.Frame(marco_negro, bg="#B0E0E6")
frame_login.pack(fill="both", expand=True)

tk.Label(frame_login, text="Usuario", font=("Arial", 14), bg="#B0E0E6").pack(pady=10)
entry_usuario = tk.Entry(frame_login, font=("Arial", 12))
entry_usuario.pack(pady=10)

tk.Label(frame_login, text="Contraseña", font=("Arial", 14), bg="#B0E0E6").pack(pady=10)
entry_contraseña = tk.Entry(frame_login, show="*", font=("Arial", 12))
entry_contraseña.pack(pady=10)

tk.Button(frame_login, text="Login", font=("Arial", 12), command=login).pack(pady=20)

ventana_login.mainloop()