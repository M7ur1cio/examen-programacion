#Verificar si un triángulo es válido:
#o Escribe un programa que solicite las longitudes de los tres lados de un triángulo y
#determine si es un triángulo válido (la suma de las longitudes de dos lados debe ser
#mayor que la longitud del tercer lado).
def Verificar_si_un_triángulo_es_válido():
    print ("---Verificar si un triángulo es válido---")
    l1 = float(input("Ingresa la longitud del primer lado: "))
    l2 = float(input("Ingresa la longitud del segundo lado: "))
    l3 = float(input("Ingresa la longitud del tercer lado: "))

    if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
        print("Es un triángulo válido.")
    else:
        print("No es un triángulo válido.")
