#4. Sumar dígitos de un número: Pide al usuario un número entero y suma sus dígitos usando
# un ciclo while.
def Sumar_dígitos_de_un_número ():
    print ("---Sumar dígitos de un número---")
    num = int(input("Ingresa un número entero: "))
    su = 0
    while num != 0:
        su += num % 10
        num //= 10
    print("La suma de los dígitos es:", su)
    ir_almenu=input("presine (c) para regresar al menú: ")
