
#Asignar un numero aletorio entre 1 y 10
num_aleatorio= 7

#Solicitar al usuario que adivine el numero
adivza= int(input("Adivina el numero entre 1 y 10: "))

#Verificar si el numero es correcto
if adivza == num_aleatorio:
    print("¡Felicidades, acertaste!")
else:
    print("Intenta de nuevo.")
