def calculadora_de_área_de_trapecio():
    print("calculadora de área de trapecio \n")
    base1=input("ingrese longitud de la base menor ")
    base2=input("ingrese longitud de la base mayor ")
    altura=input("ingrese la altura ")

    base1=float()
    base2=float()
    altura=float()
    a=((base1+base2)*altura/2)
    a=int(a)

    print (f"este es resultado {a}")
    ir_almenu=input("presine (c) para regresar al menú: ")
