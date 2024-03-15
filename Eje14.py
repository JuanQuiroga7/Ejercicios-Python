palabra1 = (input("Ingrese la primera palabra a comparar: "))
palabra2 = (input("Ingrese la segunda palabra: "))

palabra1_cantidad = len(palabra1)
palabra2_cantidad = len(palabra2)


if palabra1_cantidad > palabra2_cantidad:
    resultado1 = palabra1_cantidad - palabra2_cantidad
    print("la palabra ",palabra1," es mayor por ",resultado1," letras")
elif palabra1_cantidad < palabra2_cantidad:
    resultado2 = palabra2_cantidad - palabra1_cantidad
    print("la palabra ",palabra2," es mayor por ",resultado2," letras")
else:
    print("Ambas palabras tienen la misma cantidad de letras ","(",palabra1_cantidad,")")




