#Escribe un programa que solicite un carácter al usuario y determine si es una letra (a-z,
#A-Z) o un dígito (0-9).
def Determinar_si_un_carácter_es_una_letra_o_un_dígito ():
    print ("---Determinar si un carácter es una letra o un dígito---")
    pal= input("ingrese una letra o numero: ")
    if pal.isalpha():
        print(f"'{pal}' es una letra.")
    elif pal.isdigit():
        print(f"'{pal}' es un dígito.")
    else:
        print(f"'{pal}' no es ni una letra ni un dígito.")
    ir_almenu=input("presine (c) para regresar al menú: ")
