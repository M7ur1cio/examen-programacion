#5. Imprimir números impares: Pide al usuario un número entero positivo y muestra todos los
#números impares del 1 hasta ese número usando un ciclo for.
def imprimir_numeros_impares():
    print ("---imprimir numeros impares---")
    n3= int (input ("ingrese un numero entero: "))
    print ("esto es todos los numero impares: ")
    for i in range(1, n3 + 1, 2):
        print(i)
    ir_almenu=input("presine (c) para regresar al menú: ")
