
#Solicitar el año al usuario

año= int(input("Ingresa un año: "))

#verificar si el año es bisiesto
if(año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    restd= "Es bisiesto"
else:
    restd= "No es bisiesto"

#Mostrar el resultado
print(restd)
