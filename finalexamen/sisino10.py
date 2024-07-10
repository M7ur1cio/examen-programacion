#10. Comparar dos números:
#o Escribe un programa que solicite al usuario dos números y determine cuál es mayor o
#si son iguales.
def Comparar_dos_números ():
    print ("---Comparar dos números---")
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    if n1 > n2:
        print(f"{n1} es mayor que {n2}.")
    elif n1 < n2:
        print(f"{n2} es mayor que {n1}.")
    else:
        print(f"{n1} y {n2} son iguales.")
    ir_almenu=input("presine (c) para regresar al menú: ")
