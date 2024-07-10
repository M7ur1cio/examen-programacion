#Determinar la categoría de un trabajador:
#o Escribe un programa que solicite al usuario los años de experiencia y determine la
#categoría del trabajador: "Junior" (menos de 2 años), "Semi-Senior" (2-5 años), "Senior"
#(más de 5 años).
def Determinar_la_categoría_de_un_trabajador():
    print ("---Determinar la categoría de un trabajador---")
    exp = int(input("Ingresa los años de trabajo: "))
    if exp < 2:
        print("eres: Junior")
    elif 2 <= exp <= 5:
        print("eres: Semi-Senior")
    else:
        print("eres: Senior")
