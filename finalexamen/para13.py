#3. Contar vocales en una cadena: Pide al usuario que ingrese una cadena de texto y cuenta
#cuántas vocales hay en la cadena usando un ciclo for.
def Contar_vocales_en_una_cadena():
    print ("---Contar vocales en una cadena---")
    v1= str (input ("ingrese una palabra: "))
    con="aeiouAEIOU"
    vol=0
    for i in v1:
        if i in con:
            vol += 1
    print(f"La palabra que ingreso tiene: {vol} vocales.")
    ir_almenu=input("presine (c) para regresar al menú: ")
