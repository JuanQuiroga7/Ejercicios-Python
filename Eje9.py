not1 =  int(input("Ingrese la nota del primer certamen: "))
not2 = int(input("Ingrese la nota del segundo certamen: "))
nota_laboratorio = int(input("Ingrese la nota de Laboratorio: "))

nota_final = 60
nota_objetivo = (nota_final - nota_laboratorio * 0.3) / 0.7

nota3 = 2 * nota_objetivo - not1 - not2

print("Necesita",nota3, "en el certamen 3")