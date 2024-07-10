def prestamos_salarios_extra ():
    print ("---salarios---")
    sb=input("salrio base: ")
    ss=input("seguro social: ")
    se=input("salario extra: ")

    sb=float(sb)
    ss=float(ss)
    se=float(se)
    prestamo=(50)
    salario_neto=(sb-ss-se-prestamo)

    print ("su salario es de",salario_neto)
    ir_almenu=input("presine (c) para regresar al menú: ")
