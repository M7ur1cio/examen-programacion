#Calcular el salario neto:
#o Escribe un programa que solicite al usuario su salario bruto y calcule el salario neto
#después de aplicar un impuesto del 20% si el salario bruto es mayor a $2000.
def Calcular_el_salario_neto():
    print ("---Calcular el salario neto---")
    sal = float(input("Ingresa tu salario aqui: "))
    if sal > 2000:
        impuesto = sal * 0.20
        saleto = sal - impuesto
        print(f"Tu salario neto es: ${saleto:.2f}")
    else:
        print("No se aplica impuesto.su salario es igual.")
