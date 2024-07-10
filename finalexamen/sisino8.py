#Escribe un programa que solicite al usuario un número y determine si está entre 1 y
#100 inclusive.
def Verificar_si_un_número_está_en_un_rango():
    print ("---Verificar si un número está en un rango---")
    n1= int (input("ingrese un numero: " ))
    if 1 <= n1 <= 100:
        print(f"{n1} está en el rango de 1 a 100.")
    else:
        print(f"{n1} está fuera del rango de 1 a 100.")
    ir_almenu=input("presine (c) para regresar al menú: ")
