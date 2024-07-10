#7. Determinar si un número es primo: Pide al usuario un número entero positivo y determina si
#es primo usando un ciclo for.
def Determinar_si_un_número_es_primo():
    print ("---Determinar si un número es primo---")
    nu=int(input("ingrese el numero: "))
    nu2= True
    if nu < 2:
        nu2 = False
    else:
        for i in range(2,int(nu**0.5) + 1):
            if nu % i == 0:
                nu2 = False
                break
    if nu2:
        print(f"{nu} este número es primo.")
    else:
        print(f"{nu} este no es un número primo.")
    ir_almenu=input("presine (c) para regresar al menú: ")
