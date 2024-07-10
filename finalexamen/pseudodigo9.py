def monto_tasa ():
    print ("--el monto + la tasa--")
    monto=input("ingrese el monto: ")
    tasa=input(" ingrese la tasa: ")

    monto=float(monto)
    tasa=float(tasa)
    interes_mensual=((monto*(tasa/100))/12)
    capital= (monto-interes_mensual)
    interes_mensual=float(interes_mensual)
    capital=float(capital)
    print (f"el interes mensual es:{interes_mensual} y el capital es {capital}")
    ir_almenu=input("presine (c) para regresar al menú: ")
