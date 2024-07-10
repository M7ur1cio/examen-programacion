def suma_multiplicacion_division_4_numeros ():
    print ("---suma,multiplicacion,division, de 4---")
    a=2
    b=5
    c=3
    aux=0

    a=int(a)
    b=int(b)
    c=int(c)
    aux=int(aux)
    a=(a+3)
    b=(5*a)
    c=b
    aux=c
    a=(b+c)
    b=(aux/c)
    c=((a+b)*aux)

    print (a,",",b,",",c,",",aux)
    ir_almenu=input("presine (c) para regresar al menú: ")
