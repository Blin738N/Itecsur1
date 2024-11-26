
#recorrer los numeros entre 1 y 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=", " if i < 20 else "")
