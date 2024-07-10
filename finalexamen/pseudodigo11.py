def regla_de_tres_simple ():
    print ("---sus notas por favor---")
    a=input("ingrese su nota: ")
    b=input("ingrese otra nota: " )
    c=input("ingrese la ultima nota: ")

    a=float(a)
    b=float(b)
    c=float(c)
    r=(b/a)
    r=int(r)
    x=(c*r)
    x=int(x)

    print(f"el resultado es {x}")
    ir_almenu=input("presine (c) para regresar al menú: ")
