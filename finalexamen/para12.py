#2. Sumar números pares del 1 al 100: Escribe un programa que sume todos los números pares
#del 1 al 100 usando un ciclo for.
def Sumar_números_pares_del_1_al_100():
    print ("---Sumar números pares del 1 al 100---")
    s=0
    for i in range(1, 100):
        s += i
    print(f"La suma de los números pares del 1 al 100 es: {s}")
    ir_almenu=input("presine (c) para regresar al menú: ")
