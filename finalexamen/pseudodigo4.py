def hallador_de_area_recatángulo ():
    print("---hallador de area del recatángulo---")
    ab=input("numero de lado A: " )
    dc=input("numero de lado B: " )
    cd=input("numero de lado C: " )
    da=input("numero de lado D: " )

    ab=int(ab)
    dc=int(dc)
    cd=int(cd)
    da=int(da)
    p=ab+dc+cd+da
    p=int(p)

    print(f"el resultado de la medidas son {p}")
    ir_almenu=input("presine (c) para regresar al menú: ")
