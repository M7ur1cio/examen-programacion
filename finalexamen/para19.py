#9. Dibujar un triángulo de asteriscos: Pide al usuario un número entero positivo NNN y dibuja
#un triángulo de asteriscos de altura NNN usando un ciclo for.
def Dibujar_un_triángulo_de_asteriscos():
    print ("---Dibujar un triángulo de asteriscos---")
    nunn=int (input("ingrese un numero: "))
    for i in range(1, nunn + 1):
        print("*" * i)
    ir_almenu=input("presine (c) para regresar al menú: ")
