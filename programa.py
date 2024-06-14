# programa_principal.py

import manipulacion_cadenas as mc
import operaciones_listas as ol
import diccionarios_archivos as da

def main():
    # Parte 1: Manipulación de cadenas
    cadena = input("Ingrese una cadena de texto: ")
    cadena_invertida = mc.invertir_cadena(cadena)
    num_vocales = mc.contar_vocales(cadena)
    print(f"Cadena invertida: {cadena_invertida}")
    print(f"Número de vocales: {num_vocales}")

    # Parte 2: Operaciones con listas
    lista_str = input("Ingrese una lista de números separados por comas: ")
    lista = [int(num) for num in lista_str.split(',')]
    suma = ol.suma_lista(lista)
    maximo = ol.mayor_elemento(lista)
    print(f"Suma de la lista: {suma}")
    print(f"Mayor elemento de la lista: {maximo}")

    # Parte 3: Lectura y procesamiento de archivo
    archivo_entrada = 'texto.txt'
    frecuencia = da.leer_archivo(archivo_entrada)
    archivo_salida = 'frecuencia_palabras.txt'
    da.guardar_diccionario(frecuencia, archivo_salida)
    print(f"Frecuencia de palabras guardada en {archivo_salida}")

if _name_ == "_main_":
    main()