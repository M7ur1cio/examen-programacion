def Verificar_si_un_número_es_múltiplo_de_5 ():
    print ("---Verificar si un número es múltiplo de 5---")
    numero = int(input("Introduce un número: "))
    if numero % 5 == 0:
        print("El número es múltiplo de 5.")
    else:
        print("El número no es múltiplo de 5.")
    ir_almenu=input("presine (c) para regresar al menú: ")