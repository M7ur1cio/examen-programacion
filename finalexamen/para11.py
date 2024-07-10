#Tabla de multiplicar: Pide al usuario un número entero positivo y muestra su tabla de
#multiplicar del 1 al 10 usando un ciclo for.
def tabla_de_multiplicación ():
    print ('---tabla de multiplicación---')
    nn= int (input("ingrese un numero: "))
    for i in range(1, 11):
        print(f"{nn} x {i} = {nn * i}")
    print ("fin.")
    ir_almenu=input("presine (c) para regresar al menú: ")
