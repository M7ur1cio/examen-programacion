def Determinarsiuncarácteresunavocal():
    print ("---Determinar si un carácter es una vocal---")
    letra = input("Introduce una letra: ")
    if letra.lower() in "aeiou":
        print("La letra que ingresaste, Es una vocal.")
    else:
        print("La letra que ingresaste, No es una vocal.")
    ir_almenu=input("presine (c) para regresar al menú: ")
