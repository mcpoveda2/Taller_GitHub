#primera función:
def invertir_cadena(cadena):
    return cadena[::-1]

#Segunda función:
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for cad in cadena:
        if cad in vocales:
            contador += 1
    return contador