
#Solicitar la calificacion
notas= float(input("Ingresa tu calificacion: "))

#Determinar la letra correspondiente
if 90 <= notas <= 100:
    letra= "A"
elif 80 <= notas < 90:
    letra= "B"
elif 70 <= notas < 80:
    letra= "C"
elif 60 <= notas < 70:
    letra= "D"
else:
    letra= "F"

#Mostrar el resultado
print(f"Tu calificacion es {letra}.")
