def calculo_inpuesto_product():
    print ("->calculadora de inpuesto de prducto\n")
    pre=input ("ingrese el precio ")
    can=input ("ingrese la cantidad ")

    pre=float(pre)
    can=float(can)
    p1=(pre*can)
    p1=float(p1)
    p2=(p1*0.10)
    p2=float(p2)
    p3=(p1+p2)
    p3=(p3)

    print ("el impuesto del producto es ",p3)
    ir_almenu=input("presine (c) para regresar al menú: ")
