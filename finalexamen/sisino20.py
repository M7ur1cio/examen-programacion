#Calcular la tarifa de un taxi:
#o Escribe un programa que solicite la distancia recorrida en kilómetros y calcule la tarifa
#del taxi. La tarifa es $2.50 por kilómetro para los primeros 10 kilómetros y $2.00 por
#kilómetro adicional.
def Calcular_la_tarifa_de_un_taxi():
    print ("---Calcular la tarifa de un taxi---")
    km = float(input("Ingresa la distancia recorrida: "))

    base = 2.50
    adicional = 2.00

    if km <= 10:
        total = (base * km)
    else:
        total = base * 10 + adicional * (km - 10)

    print(f"Tarifa total del taxi: ${total:.2f}")
