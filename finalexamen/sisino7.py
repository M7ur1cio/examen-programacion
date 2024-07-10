#Escribe un programa que solicite el precio de un producto y determine el precio final
#después de aplicar un descuento del 10% si el precio es mayor a $100.
def Calcular_el_precio_con_descuento ():
    print ("---Calcular el precio con descuento---")
    prod= float (input("ingrese precio del producto: " ))
    if prod > 100:
        descuento = prod * 0.10
        precio_final = prod - descuento
        print(f"Precio con descuento: ${precio_final:.2f}")
    else:
        print("No se aplica descuento.")
    ir_almenu=input("presine (c) para regresar al menú: ")
