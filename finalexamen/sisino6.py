#Escribe un programa que solicite la edad del usuario y clasifique la edad en una de las
#siguientes categorías: "Infantil" (0-12), "Adolescente" (13-19), "Adulto" (20-59) y "Adulto
#mayor" (60 o más)
def Clasificar_la_categoría_de_edad ():
    print ("---Clasificar la categoría de edad---")
    edad = int(input("Ingresa tu edad: "))
    if edad <= 12:
        print("Categoría: Infantil")
    elif 13 <= edad <= 19:
        print("Categoría: Adolescente")
    elif 20 <= edad <= 59:
        print("Categoría: Adulto")
    else:
        print("Categoría: Adulto mayor")
    ir_almenu=input("presine (c) para regresar al menú: ")
