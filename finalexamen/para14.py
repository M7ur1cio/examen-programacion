#4. Imprimir una serie de números: Imprime todos los números del 10 al 1 en orden
#descendente usando un ciclo for.
def Imprimir_una_serie_de_números():
    print ("---Imprimir una serie de números---")
    print ("esto es en orden descendente")
    for i in range(10, 0, -1):
        print(i)
    ir_almenu=input("presine (c) para regresar al menú: ")
