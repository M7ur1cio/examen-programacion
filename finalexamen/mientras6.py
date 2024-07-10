#6. Mostrar múltiplos de un número: Pide al usuario un número entero positivo y muestra sus
#múltiplos del 1 al 10 usando un ciclo while
def Mostrar_múltiplos_de_un_número():
    print ('---Mostrar múltiplos de un número---')
    n1= int (input('ingrese un numero: '))
    n2= 1
    while n2 <= 10:
        print(n1 * n2)
        n2 += 1
    ir_almenu=input("presine (c) para regresar al menú: ")
