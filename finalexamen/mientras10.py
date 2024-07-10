#10.Simular un cajero automático: Escribe un programa que simule un cajero automático. Pide
#al usuario que ingrese su PIN y permite tres intentos para ingresarlo correctamente. Si no lo
#hace en tres intentos, muestra un mensaje de bloqueo. Usa un ciclo while
def Simular_un_cajero_automático ():
    print ('cajero automatico.com \n')
    contra= "1234"
    contac= 3
    intentos=0
    while intentos < contac:
        con2 = input("Ingresa su PIN: ")
        if con2 == contra:
            print("Entrado a su cuenta... ¡Bienvenido!")
            break
        else:
            intentos += 1
            print(f"PIN incorrecto. Te quedan {contac - intentos} intentos.")

    if intentos == contac:
        print("demasiados intentos. Tu cuenta ha sido bloqueada.")
    ir_almenu=input("presine (c) para regresar al menú: ")
