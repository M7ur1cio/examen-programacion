import pseudodigo1, pseudodigo2, pseudodigo3, pseudodigo4, pseudodigo5, pseudodigo6
import pseudodigo7, pseudodigo8, pseudodigo9, pseudodigo10, pseudodigo11, pseudodigo12
import sisino1, sisino2, sisino3, sisino4, sisino5, sisino6, sisino7, sisino8, sisino9
import sisino10, sisino11, sisino12, sisino13, sisino14, sisino15, sisino16, sisino17
import sisino18, sisino19, sisino20, mientras1, mientras2, mientras4, mientras5, mientras6
import mientras7, mientras8, mientras9, mientras10, para11, para12, para13, para14, para15
import para16, para17, para18, para19, para20

def menuprincialexamen ():
    while True:
        print("""
 ___________________________________________________________________________
|                              Menú principal                               |
|_____________________________Examen_final_2024_____________________________|
|                                                                           |
|                          lista de seudocodigo:                            |
|                       1,2,3,4,5,6,7,8,9,10,11,12                          |
|___________________________________________________________________________|
|                         lista de if, else, elif:                          |
|                  13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,              |
|                  24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 32               |        
|___________________________________________________________________________|
|                           lista de while,for:                             |
|                    33, 34, 35, 36, 37, 38, 39, 40, 41, 42                 |
|                     43, 44, 45, 46, 47, 48, 49, 50, 51,52                 |
|                        __________________________                         |
|                       |  Desea salir,presiona: q |                        |
|                       |__________________________|                        |
|___________________________________________________________________________|       
        """)
        opci= input("Elige un numero de las litas: ")
        
                   
        match opci:
            case "1":
                pseudodigo1.sumador_dos_numero()
            case "2":
                pseudodigo2.calculo_inpuesto_product()
            case "3":
                pseudodigo3.calculo_area_triangulo()
            case "4":
                pseudodigo4.hallador_de_area_recatángulo()
            case "5":
                pseudodigo5.calculadora_de_área_de_trapecio()
            case "6":
                pseudodigo6.alculadora_de_un_prisma_rectangular()
            case "7":
                pseudodigo7.solucion_de_ecuanciones_lineales()
            case "8":
                pseudodigo8.suma_multiplicacion_division_4_numeros()
            case "9":
                pseudodigo9.monto_tasa()
            case "10":
                pseudodigo10.cenvertidor_metro_a_pies_y_pulgadas()
            case "11":
                pseudodigo11.regla_de_tres_simple()
            case "12":
                pseudodigo12.prestamos_salarios_extra()
            case "13":
                sisino1.Verificar_si_un_número_es_positivo()
            case "14":
                sisino2.Determinar_si_una_persona_es_adolescente ()
            case "15":
                sisino3.Verificar_si_un_número_es_múltiplo_de_5 ()
            case "16":
                sisino4.Determinarsiuncarácteresunavocal()
            case "17":
                sisino5.Verificars_i_una_palabra_tiene_más_de_5letras ()
            case "18":
                sisino6.Clasificar_la_categoría_de_edad ()
            case "19":
                sisino7.Calcular_el_precio_con_descuento ()
            case "20":
                sisino8.Verificar_si_un_número_está_en_un_rango()
            case "21":
                sisino9.Determinar_si_un_carácter_es_una_letra_o_un_dígito ()
            case "22":
                sisino10.Comparar_dos_números ()
            case "23":
                sisino11.Determinar_si_un_número_es_primo ()
            case "24":
                sisino12.Calcular_el_salario_neto()
            case "25":
                sisino13.Determinar_si_un_año_es_un_siglo()
            case "26":
                sisino14.Verificar_si_un_triángulo_es_válido()
            case "27":
                sisino15.Determinar_la_categoría_de_un_trabajador()
            case "28":
                sisino16.Clasificar_el_IMC()
            case "29":
                sisino17.Determinar_el_tipo_de_licencia_de_conducir()
            case "30":
                sisino18.Determinar_si_un_número_es_divisible_por_3_y_5 ()
            case "31":
                sisino19.Verificar_si_un_nombre_es_corto_mediano_o_largo()
            case "32":
                sisino20.Calcular_la_tarifa_de_un_taxi()
            case "33":
                mientras1.Sumar_números_del_1_al_100 ()
            case "34":
                mientras2.Contar_hasta_un_número_dado ()
            case "35":
                mientras3.Sumar_números_hasta_un_límite ()
            case "36":
                mientras4.Sumar_dígitos_de_un_número ()
            case "37":
                mientras5.Adivinar_un_número ()
            case "38":
                mientras6.Mostrar_múltiplos_de_un_número()
            case "39":
                mientras7.Validar_entrada ()
            case "40":
                mientras8.contador_de_digitos()
            case "41":
                mientras9.convertidor_de_decimal_a_binario ()
            case "42":
                mientras10.Simular_un_cajero_automático ()
            case "43":
                para11.tabla_de_multiplicación ()
            case "44":
                para12.Sumar_números_pares_del_1_al_100()
            case "45":
                para13.Contar_vocales_en_una_cadena()
            case "46":
                para14.Imprimir_una_serie_de_números()
            case "47":
                para15.imprimir_numeros_impares()
            case "48":
                para16.Sumar_los_primeros_N_números_naturales()
            case "49":
                para17.Determinar_si_un_número_es_primo()
            case "50":
                para18.convertir_grados_Celsius_a_Fahrenheit()
            case "51":
                para19.Dibujar_un_triángulo_de_asteriscos()
            case "52":
                para20.Repetir_una_cadena()
            
            case "q":
                print ("gracias por visitarnos...")
                print ("Este progrma fue Hecho por: Mauricio Bocanegra // Diego Valderrama.")
                print("Saliendo...")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")
    
if __name__ == "__main__":
    menuprincialexamen()