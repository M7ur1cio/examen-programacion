#Clasificar el IMC:
#o Escribe un programa que solicite al usuario su peso y altura, calcule el Índice de Masa
#Corporal (IMC) y clasifique el resultado: "Bajo peso" (IMC < 18.5), "Normal" (18.5 ≤ IMC
#< 24.9), "Sobrepeso" (25 ≤ IMC < 29.9) y "Obesidad" (IMC ≥ 30)
def Clasificar_el_IMC():
    print ("---Clasificar el IMC---")
    ilo = float(input("Ingresa tu peso en kilogramos: "))
    distancia = float(input("Ingresa tu altura en metros: "))

    imc = ilo / (distancia**2)

    if imc < 18.5:
        print("Estas Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Estas Normal")
    elif 25 <= imc < 29.9:
        print("Estas en Sobrepeso")
    else:
        print("Estas en Obesidad")
