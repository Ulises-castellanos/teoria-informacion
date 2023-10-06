class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.izquierda = None
    self.derecha = None

prueba = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#prueba = [0.5, 0.125, 0.125, 0.125, 0.125]

nodos = []

for numero in prueba:
    nodo = Nodo(numero)
    nodos.append(nodo)

for nodo in nodos:
  print("   Nodo:",nodo.dato)

while len(nodos) > 1:
  nodos.sort(key=lambda x: x.dato)
  nodo1 = nodos.pop(0)
  print("nodo1",str(nodo1.dato))
  nodo2 = nodos.pop(0)
  print("nodo2",str(nodo2.dato))
  suma = nodo1.dato + nodo2.dato
  nuevo_nodo = Nodo(suma)
  print("dato",nuevo_nodo.dato)
  nuevo_nodo.izquierda = nodo1
  nuevo_nodo.derecha = nodo2

  nodos.append(nuevo_nodo)
  for nodo in nodos:
    print("   Nodo:",nodo.dato)
arbol_huffman = nodos[0]

def imprimir_arbol(arbol, nivel=0):
  if arbol is not None:
    print(" " * nivel + str(arbol.dato))
    imprimir_arbol(arbol.izquierda, nivel + 1)
    imprimir_arbol(arbol.derecha, nivel + 1)

imprimir_arbol(arbol_huffman)