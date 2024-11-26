
#Solicitar la edad de un usuario
edad= int(input("Ingresa tu edada:"))

#clasificacion segun la edad
if 0 <=edad <=12:
    clasificacion= "Eres niño."
elif 13 <= edad <=17:
    clasificacion= "Eres adolescente."
elif 18 <= edad <=64:
    clasificacion= "Eres adulto."
else:
    clasificacion= "Eres adulto mayor"
    
#imprimo la clasificacion
print(clasificacion)
