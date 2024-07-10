#3. Sumar números hasta un límite: Pide al usuario que ingrese números enteros positivos uno
#a uno y suma estos números hasta que la suma alcance un límite (por ejemplo, 100). Usa un
#ciclo while.
def Sumar_números_hasta_un_límite ():
    print ("---Sumar números hasta un límite---")
    litm= 100
    conta= 0
    while conta < litm:
        numero = int(input("Ingresa un número positivo: "))
        conta += numero
    print("La suma alcanzó o superó el límite de", litm)
    ir_almenu=input("presine (c) para regresar al menú: ")
