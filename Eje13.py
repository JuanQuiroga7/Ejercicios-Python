dividendo = int(input("Ingrese el numero a dividir: "))
divisor = int(input("Ingrese el numero por el cual divide: "))

if dividendo %divisor == 0:
    print("La division es exacta")
else:
    print("La division no es exacta")