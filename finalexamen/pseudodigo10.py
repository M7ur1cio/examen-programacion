def cenvertidor_metro_a_pies_y_pulgadas():
    print("---cenvertidor de metros a pies y pulgadas---")
    m=input("ingrese el metro: ")

    m=float(m)
    ft=(m*3.28084)
    en=m*39.37
    m1=m
    ft=int(ft)
    en=int(en)
    m1=int(m1)
    print("metro a pies ",ft,",metro a pulgadas ",en,",metro ",m1)
    ir_almenu=input("presine (c) para regresar al menú: ")
