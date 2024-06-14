#primera función:
def suma_lista(lista):
  total = 0
  for numero in lista:
    total += numero
  return total


#segunda funcion:
def mayor_elemento(lista):
  if not lista:
    return None 
  mayor = lista [0]
  for numero in lista:
      if numero > mayor:
        mayor = numero
  return mayor
