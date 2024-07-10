# Determinar si un número es primo:
#o Escribe un programa que solicite un número al usuario y determine si es un número
#primo.
def Determinar_si_un_número_es_primo ():
    print ("---Determinar si un número es primo---")
    nume = int(input("Ingresa un número: "))
    if nume <= 1:
        print(f"{nume} no es un número primo.")

    elif nume == 2:
        print(f"{nume} es un número primo.")

    elif nume % 2 == 0:
        print(f"{nume} no es un número primo.")
