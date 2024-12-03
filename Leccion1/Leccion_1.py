import tkinter as tk
from tkinter import messagebox

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Calificaciones")

        self.students = {}

        # Frame principal
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Elementos de entrada
        tk.Label(self.frame, text="DNI:").grid(row=0, column=0, sticky="e")
        tk.Label(self.frame, text="Apellidos:").grid(row=1, column=0, sticky="e")
        tk.Label(self.frame, text="Nombre:").grid(row=2, column=0, sticky="e")
        tk.Label(self.frame, text="Nota:").grid(row=3, column=0, sticky="e")

        self.dni_entry = tk.Entry(self.frame)
        self.last_name_entry = tk.Entry(self.frame)
        self.first_name_entry = tk.Entry(self.frame)
        self.grade_entry = tk.Entry(self.frame)

        self.dni_entry.grid(row=0, column=1)
        self.last_name_entry.grid(row=1, column=1)
        self.first_name_entry.grid(row=2, column=1)
        self.grade_entry.grid(row=3, column=1)

        # Botones de acciones
        tk.Button(self.frame, text="Añadir Alumno", command=self.add_student).grid(row=4, column=0, pady=5)
        tk.Button(self.frame, text="Eliminar Alumno", command=self.delete_student).grid(row=4, column=1, pady=5)
        tk.Button(self.frame, text="Consultar Alumno", command=self.consult_student).grid(row=5, column=0, pady=5)
        tk.Button(self.frame, text="Modificar Nota", command=self.modify_grade).grid(row=5, column=1, pady=5)
        tk.Button(self.frame, text="Mostrar Suspensos", command=self.show_failing_students).grid(row=6, column=0, pady=5)
        tk.Button(self.frame, text="Mostrar Aprobados", command=self.show_passing_students).grid(row=6, column=1, pady=5)
        tk.Button(self.frame, text="Candidatos a MH", command=self.show_candidates_for_mh).grid(row=7, column=0, pady=5)
        tk.Button(self.frame, text="Mostrar Todos", command=self.show_all_students).grid(row=7, column=1, pady=5)

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
        dni = self.dni_entry.get()
        last_name = self.last_name_entry.get()
        first_name = self.first_name_entry.get()
        try:
            grade = float(self.grade_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Nota debe ser un número.")
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
            messagebox.showinfo("Éxito", "Alumno añadido correctamente.")

    def delete_student(self):
        dni = self.dni_entry.get()
        if dni in self.students:
            del self.students[dni]
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
        else:
            messagebox.showerror("Error", "Alumno no encontrado.")

    def consult_student(self):
        dni = self.dni_entry.get()
        if dni in self.students:
            student = self.students[dni]
            info = f"{dni} {student['apellidos']}, {student['nombre']} {student['nota']} {student['calificación']}"
            messagebox.showinfo("Alumno", info)
        else:
            messagebox.showerror("Error", "Alumno no encontrado.")

    def modify_grade(self):
        dni = self.dni_entry.get()
        if dni in self.students:
            try:
                new_grade = float(self.grade_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Nota debe ser un número.")
                return
            self.students[dni]["nota"] = new_grade
            self.students[dni]["calificación"] = self.calculate_calification(new_grade)
            messagebox.showinfo("Éxito", "Nota modificada correctamente.")
        else:
            messagebox.showerror("Error", "Alumno no encontrado.")

    def show_failing_students(self):
        failing_students = [
            f"{dni} {data['apellidos']}, {data['nombre']} {data['nota']} {data['calificación']}"
            for dni, data in self.students.items() if data['nota'] < 5
        ]
        self.display_list(failing_students, "Alumnos Suspensos")

    def show_passing_students(self):
        passing_students = [
            f"{dni} {data['apellidos']}, {data['nombre']} {data['nota']} {data['calificación']}"
            for dni, data in self.students.items() if data['nota'] >= 5
        ]
        self.display_list(passing_students, "Alumnos Aprobados")

    def show_candidates_for_mh(self):
        mh_candidates = [
            f"{dni} {data['apellidos']}, {data['nombre']} {data['nota']} {data['calificación']}"
            for dni, data in self.students.items() if data['nota'] == 10
        ]
        self.display_list(mh_candidates, "Candidatos a MH")

    def show_all_students(self):
        all_students = [
            f"{dni} {data['apellidos']}, {data['nombre']} {data['nota']} {data['calificación']}"
            for dni, data in self.students.items()
        ]
        self.display_list(all_students, "Todos los Alumnos")

    def display_list(self, items, title):
        if items:
            messagebox.showinfo(title, "\\n".join(items))
        else:
            messagebox.showinfo(title, "No hay datos para mostrar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()
