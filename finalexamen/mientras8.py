#8. Contador de dígitos: Pide al usuario un número entero y cuenta cuántos dígitos tiene usando
#un ciclo while.
def contador_de_digitos():
    print ('---contador de digitos---')
    n=int(input("ingrese un numero entero: "))
    r= 0

    while n != 0:
        r += 1
        n //= 10
    print("El número tiene", r, "dígitos.")
    ir_almenu=input("presine (c) para regresar al menú: ")
