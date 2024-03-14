num = int(input("Ingrese un numero entero de 3 digitos: "))

reverso = list(str(num))[::-1]

numinvertido= int("".join(reverso))

print(numinvertido)