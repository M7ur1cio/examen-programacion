#6. Sumar los primeros N números naturales: Pide al usuario un número entero positivo NNN y
#suma los primeros NNN números naturales usando un ciclo for.
def Sumar_los_primeros_N_números_naturales():
    print ("---Sumar los primeros N números naturales---")
    na=int (input("ingrese un numeros:"))
    r= 0
    for i in range(1, na + 1):
        r += i
    print(f"La suma de {na} es: {r}")
    ir_almenu=input("presine (c) para regresar al menú: ")
