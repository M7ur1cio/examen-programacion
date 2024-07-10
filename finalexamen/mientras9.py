#9. Convertir de decimal a binario: Pide al usuario un número entero positivo y convierte ese
#número a binario usando un ciclo while.
def convertidor_de_decimal_a_binario ():
    print ('---convertidor de decimal a binario---')
    c1= int(input ('ingrese un numero entero: '))
    conver= ""
    while c1 > 0:
        conver = str(c1 % 2) + conver
        c1 //= 2
    print("El número en binario es:", conver)
    ir_almenu=input("presine (c) para regresar al menú: ")

