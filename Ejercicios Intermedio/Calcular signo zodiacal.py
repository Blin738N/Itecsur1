
#Solicitar el dia y el mes de nacimiento
dia=int(input("Ingresa el dia de nacimiento(numero): "))
mes=input("Ingresa el mes de nacimineto(nombre): ").lower()

#determinar el signo zodiacal
if(mes == "marzo" and dia >=21) or (mes == "abril" and dia <=19):
    signo = "Aries"
elif(mes == "abril" and dia >=20) or (mes == "mayo" and dia <=20):
    signo = "Tauro"
elif(mes == "mayo" and dia >=21) or (mes == "junio" and dia <=20):
    signo = "Geminis"
elif(mes == "junio" and dia >=21) or (mes == "julio" and dia <=22):
    signo = "Cancer"
elif(mes == "julio" and dia >=23) or (mes == "agosto" and dia <=22):
    signo = "Leo"
elif(mes == "agosto" and dia >=23) or (mes == "septiembre" and dia <=22):
    signo = "Virgo"
elif(mes == "septiembre" and dia >=23) or (mes == "octubre" and dia <=22):
    signo = "Libra"
elif(mes == "octubre" and dia >=23) or (mes == "noviemvre" and dia <=21):
    signo = "Escorpio"
elif(mes == "noviembre" and dia >=22) or (mes == "diciembre" and dia <=21):
    signo = "Sagitario"
elif(mes == "diciembre" and dia >=22) or (mes == "enero" and dia <=19):
    signo = "Capricornio"
elif(mes == "enero" and dia >=20) or (mes == "febrero" and dia <=18):
    signo = "Acuario"
elif(mes == "febrero" and dia >=19) or (mes == "marzo" and dia <=20):
    signo = "Piscis"

#Mostrar el resultado
print(f"Tu signo zodiacal es {signo}.")


