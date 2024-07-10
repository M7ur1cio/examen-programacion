#Adivinar un número: Escribe un programa que elija un número aleatorio entre 1 y 10 y
#permita al usuario adivinarlo, dándole pistas de "mayor" o "menor" hasta que acierte. Usa un
#ciclo while.
def Adivinar_un_número ():
    print ("---Adivinar un número---")
    import random
    secreto = random.randint(1, 10)
    it = 0
    while True:
        it += 1
        nume = int(input("Adivina el número (entre 1 y 10): "))
        if nume == secreto:
            print(f"felicidades...!!!. El número era {secreto}. \n la cantidad de intentos es de:{it} .")
            break
        elif nume < secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
    ir_almenu=input("presine (c) para regresar al menú: ")
