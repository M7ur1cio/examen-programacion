#10.Repetir una cadena: Pide al usuario una cadena de texto y un número entero positivo NNN.
#Muestra la cadena repetida NNN veces, cada vez en una nueva línea, usando un ciclo for.
def Repetir_una_cadena():
    print ("---repetidor de cadena---")
    tx=input("ingrese  un texto: ")
    nun=int (input("ingrese un numero: "))
    for _ in range(nun):
        print(tx)
    ir_almenu=input("presine (c) para regresar al menú: ")
