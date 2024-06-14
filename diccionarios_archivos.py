def leer_archivo(nombre_archivo):
    dic = {}

    with open(nombre_archivo, 'r') as f:
        lineas = f.readlines()

        for linea in lineas:
            palabras = linea.split(" ")
            
            for palabra in palabras:
                palabra = palabra.replace("\n","")
                if palabra not in dic:
                    dic[palabra] = 1
                else:
                    dic[palabra] += 1

    return dic


def guardar_diccionario(diccionario, nombre_archivo):
    with open(nombre_archivo,'w') as f:
        for clave in diccionario:
            f.write("La palabra " + clave + " aparece " + str(diccionario[clave])+"\n")


diccionario = leer_archivo("hola.txt")

guardar_diccionario(diccionario, "palabras.txt")
print(diccionario)