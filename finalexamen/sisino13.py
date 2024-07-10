#Determinar si un año es un siglo:
#o Escribe un programa que solicite un año al usuario y determine si es el primer año de
#un siglo (por ejemplo, 1900, 2000, 2100).
def Determinar_si_un_año_es_un_siglo():
    print ("---Determinar si un año es un siglo---")
    alo = int(input("Ingresa el año: "))
    if alo % 100 == 0:
        print(f"{alo} es el primer año de un siglo.")
    else:
        print(f"{alo} no es el primer año de un siglo.")
