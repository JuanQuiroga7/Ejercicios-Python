
def bisiestocheck(year):
    if year % 4 == 0:
        if year % 100 and year % 400:
            return True
        else:
            return False
    else:
        return False        
      

year = int(input("Ingrese el año a revisar: "))

if bisiestocheck(year):
    print("El año ",year,"es bisiesto")
else:
    print("El año ",year,"NO es bisiesto")
        
    