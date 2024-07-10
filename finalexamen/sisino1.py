def Verificar_si_un_número_es_positivo():
    print ("---Verificar si un número es positivo, negativo o cero---")
    nun = float(input("Introduce un número: "))
    if nun > 0:
        print("El número es positivo.")
    elif nun < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
    ir_almenu=input("presine (c) para regresar al menú: ")
