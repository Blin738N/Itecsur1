import tkinter as tk
from tkinter import ttk, messagebox


class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Calificaciones")
        self.root.geometry("800x500")

        self.students = {}

        # Frame principal
        self.main_frame = ttk.Frame(root, padding=10)
        self.main_frame.pack(fill="both", expand=True)

        # Frame de entrada
        self.input_frame = ttk.LabelFrame(self.main_frame, text="Datos del Alumno")
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Elementos de entrada
        ttk.Label(self.input_frame, text="DNI:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(self.input_frame, text="Apellidos:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(self.input_frame, text="Nombre:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(self.input_frame, text="Nota:").grid(row=3, column=0, sticky="e", padx=5, pady=5)

        self.dni_entry = ttk.Entry(self.input_frame)
        self.last_name_entry = ttk.Entry(self.input_frame)
        self.first_name_entry = ttk.Entry(self.input_frame)
        self.grade_entry = ttk.Entry(self.input_frame)

        self.dni_entry.grid(row=0, column=1, padx=5, pady=5)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.first_name_entry.grid(row=2, column=1, padx=5, pady=5)
        self.grade_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botones de acciones
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ttk.Button(self.button_frame, text="Añadir Alumno", command=self.add_student).grid(row=0, column=0, pady=5, sticky="ew")
        ttk.Button(self.button_frame, text="Eliminar Alumno", command=self.delete_student).grid(row=1, column=0, pady=5, sticky="ew")
        ttk.Button(self.button_frame, text="Modificar Nota", command=self.modify_grade).grid(row=2, column=0, pady=5, sticky="ew")
        ttk.Button(self.button_frame, text="Mostrar Suspensos", command=self.show_failing_students).grid(row=3, column=0, pady=5, sticky="ew")
        ttk.Button(self.button_frame, text="Mostrar Aprobados", command=self.show_passing_students).grid(row=4, column=0, pady=5, sticky="ew")
        ttk.Button(self.button_frame, text="Candidatos a MH", command=self.show_candidates_for_mh).grid(row=5, column=0, pady=5, sticky="ew")
        ttk.Button(self.button_frame, text="Mostrar Todos", command=self.show_all_students).grid(row=6, column=0, pady=5, sticky="ew")

        # Tabla para mostrar estudiantes
        self.tree_frame = ttk.Frame(self.main_frame)
        self.tree_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.tree = ttk.Treeview(self.tree_frame, columns=("dni", "apellidos", "nombre", "nota", "calificacion"), show="headings")
        self.tree.heading("dni", text="DNI")
        self.tree.heading("apellidos", text="Apellidos")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("nota", text="Nota")
        self.tree.heading("calificacion", text="Calificación")

        self.tree.column("dni", width=100)
        self.tree.column("apellidos", width=200)
        self.tree.column("nombre", width=150)
        self.tree.column("nota", width=100)
        self.tree.column("calificacion", width=100)

        self.tree.pack(fill="both", expand=True)

    def calculate_calification(self, grade):
        if grade < 5:
            return "SS"
        elif 5 <= grade < 7:
            return "AP"
        elif 7 <= grade < 9:
            return "NT"
        else:
            return "SB"

    def add_student(self):
        dni = self.dni_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        first_name = self.first_name_entry.get().strip()
        try:
            grade = float(self.grade_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Nota debe ser un número.")
            return

        if not dni or not last_name or not first_name:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if dni in self.students:
            messagebox.showerror("Error", "El alumno ya existe.")
        else:
            calification = self.calculate_calification(grade)
            self.students[dni] = {
                "apellidos": last_name,
                "nombre": first_name,
                "nota": grade,
                "calificación": calification
            }
            self.update_table()
            messagebox.showinfo("Éxito", "Alumno añadido correctamente.")

    def delete_student(self):
        dni = self.dni_entry.get().strip()
        if dni in self.students:
            del self.students[dni]
            self.update_table()
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
        else:
            messagebox.showerror("Error", "Alumno no encontrado.")

    def modify_grade(self):
        dni = self.dni_entry.get().strip()
        if dni in self.students:
            try:
                new_grade = float(self.grade_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Nota debe ser un número.")
                return
            self.students[dni]["nota"] = new_grade
            self.students[dni]["calificación"] = self.calculate_calification(new_grade)
            self.update_table()
            messagebox.showinfo("Éxito", "Nota modificada correctamente.")
        else:
            messagebox.showerror("Error", "Alumno no encontrado.")

    def show_failing_students(self):
        self.filter_students(lambda data: data["nota"] < 5, "Alumnos Suspensos")

    def show_passing_students(self):
        self.filter_students(lambda data: data["nota"] >= 5, "Alumnos Aprobados")

    def show_candidates_for_mh(self):
        self.filter_students(lambda data: data["nota"] == 10, "Candidatos a MH")

    def show_all_students(self):
        self.update_table()

    def filter_students(self, condition, title):
        filtered_students = {dni: data for dni, data in self.students.items() if condition(data)}
        self.update_table(filtered_students)
        messagebox.showinfo(title, f"Se encontraron {len(filtered_students)} alumnos.")

    def update_table(self, students=None):
        for row in self.tree.get_children():
            self.tree.delete(row)

        students = students or self.students
        for dni, data in students.items():
            self.tree.insert("", "end", values=(dni, data["apellidos"], data["nombre"], data["nota"], data["calificación"]))


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()
