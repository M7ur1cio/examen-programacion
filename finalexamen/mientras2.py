#2. Contar hasta un número dado:
#Pide al usuario un número entero positivo y muestra todos
#los números del 1 hasta ese número usando un ciclo while.
def Contar_hasta_un_número_dado ():
    print ("---Contar hasta un número dado---")
    num=int(input("ingrese un numero positivo "))
    contador = 1
    while contador <= num:
        print(contador)
        contador += 1
    ir_almenu=input("presine (c) para regresar al menú: ")
