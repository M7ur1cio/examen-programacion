#Validar entrada: Pide al usuario que ingrese un número positivo. Si el usuario ingresa un
#número negativo, solicita nuevamente la entrada hasta que ingrese un número positivo. Usa
#un ciclo while.
def Validar_entrada ():
    print ('---Validar entrada---')
    while True:
        vn = int(input("Ingresa un número positivo: "))
        if vn > 0:
            print("gracias eso era todo. adios...")
            break
        else:
            print("El número debe ser positivo. Inténtalo nuevamente.")
    ir_almenu=input("presine (c) para regresar al menú: ")
