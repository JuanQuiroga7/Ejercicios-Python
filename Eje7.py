hora_actual = int(input("Ingrese la hora actual (dentro de 1 a 24): "))
hora_adelanto = int(input("Ingrese las horas a adelantar: "))

hora_final = (hora_actual + hora_adelanto) %24

print("Si adelantas ",hora_adelanto," horas", "y la hora actual es ",hora_actual,"para entonces serian las ",hora_final)