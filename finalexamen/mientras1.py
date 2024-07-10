#1.Sumar números del 1 al 100: Escribe un programa que sume todos los números del 1 al 100
#usando un ciclo while
def Sumar_números_del_1_al_100 ():
    print ("---Sumar números del 1 al 100---")
    tol = 0
    num = 1
    while num <= 100:
        tol += num
        num += 1
    print("La suma de los números del 1 al 100 es:", tol)
    ir_almenu=input("presine (c) para regresar al menú: ")
