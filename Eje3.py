not1 = int(input("Ingrese el primer numero: "))
not2 = int(input("Ingrese el segundo numero: "))
not3 = int(input("Ingrese el tercer numero: "))
not4 = int(input("Ingrese el cuarto numero: "))

datos= (not1, not2, not3, not4)
promedio = sum(datos) / len(datos)

print("El promedio de los numeros dados es: ", promedio)