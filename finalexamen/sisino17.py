#Determinar el tipo de licencia de conducir:
#o Escribe un programa que solicite la edad del usuario y determine el tipo de licencia de
#conducir que puede obtener: "Licencia de menor" (16-17 años), "Licencia de adulto"
#(18-65 años) y "Licencia de adulto mayor" (más de 65 años)
def Determinar_el_tipo_de_licencia_de_conducir():
    print ("---Determinar el tipo de licencia de conducir---")
    ed = int(input("Ingresa tu edad: "))

    if 16 <= ed <= 17:
        print("Licencia de menor")
    elif 18 <= ed <= 65:
        print("Licencia de adulto")
    else:
        print("Licencia de adulto mayor")
