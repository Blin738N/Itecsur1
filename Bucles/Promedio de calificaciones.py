
#
suma = 0
cantidad = 0

#Solicitar la calificaciones al usuario
while True:
    calificacion = float(input("Ingrese una calificacion (-1 para termnar): "))

    if calificacion == -1:
        break

    suma += calificacion
    cantidad += 1

if cantidad > 0:
    promedio = suma / cantidad
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones.")
