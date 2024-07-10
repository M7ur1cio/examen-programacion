#Determinar si un número es divisible por 3 y 5:
#o Escribe un programa que solicite un número al usuario y determine si es divisible por 3,
#por 5, por ambos o por ninguno
def Determinar_si_un_número_es_divisible_por_3_y_5 ():
    print ("---Determinar si un número es divisible por 3 y 5---")
    nu = int(input("Ingresa un número: "))

    if nu % 3 == 0 and nu % 5 == 0:
        print(f"{nu} es divisible por 3 y 5.")
    elif nu % 3 == 0:
        print(f"{nu} es divisible por 3 pero no por 5.")
    elif nu % 5 == 0:
        print(f"{nu} es divisible por 5 pero no por 3.")
    else:
        print(f"{nu} no es divisible ni por 3 ni por 5.")
