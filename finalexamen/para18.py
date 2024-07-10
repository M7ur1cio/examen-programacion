#8. Convertir grados Celsius a Fahrenheit: Pide al usuario un rango de temperaturas en grados
#Celsius (inicio y fin) y muestra la conversión a Fahrenheit para cada grado en ese rango
#usando un ciclo for.
def convertir_grados_Celsius_a_Fahrenheit():
    print ("---convertir grados Celsius a Fahrenheit---")
    cr= int (input("ingrese un temperatura inicial: "))
    cr2=int (input("ingrese un temperatura final: "))

    print("Temperatura en Fahrenheit:")
    for i in range((cr),(cr2) + 1):
        fahrenheit = (i * 9/5) + 32
        print(f"{i}°C = {fahrenheit:.2f}°F")
    ir_almenu=input("presine (c) para regresar al menú: ")
