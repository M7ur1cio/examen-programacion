def Verificars_i_una_palabra_tiene_más_de_5letras ():
    print ("---Verificar si una palabra tiene más de 5 letras--- ")
    pal = input("Introduce una palabra: ")
    if len(pal) > 5:
        print("La palabra tiene más de 5 letras.")
    else:
        print("La palabra no tiene más de 5 letras.")
    ir_almenu=input("presine (c) para regresar al menú: ")
