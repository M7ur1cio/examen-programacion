#Verificar si un nombre es corto, mediano o largo:
#o Escribe un programa que solicite un nombre al usuario y determine si el nombre es
#corto (menos de 5 letras), mediano (5-8 letras) o largo (más de 8 letras). 
#nombre = input("Ingresa un nombre: ")
def Verificar_si_un_nombre_es_corto_mediano_o_largo():
    print ("---Verificar si un nombre es corto, mediano o largo---")
    nomb = input("Ingresa un nombre: ")
    if len(nomb) < 5:
        print("Nombre corto")
    elif 5 <= len(nomb) <= 8:
        print("Nombre mediano")
    else:
        print("Nombre largo")
