import pygame
import io
import os
import random
import math
from collections import Counter

entropia = 0

class Nodo:
  def __init__(self, nombre, dato):
    self.nombre = nombre
    self.dato = dato
    self.izquierda = None
    self.derecha = None
    self.valor_binario = ""

def emisor():
  with open('prue4.mp3', 'rb') as mp3_file:
    contenido_binario = mp3_file.read()
  return contenido_binario

def convertir_a_bits(bytes_data):
  bits = [format(byte, '08b') for byte in bytes_data]
  bits_str = ''.join(bits)
  return bits_str  

def bits_a_bytes(bits_str):
  grupos_de_bits = [bits_str[i:i+8] for i in range(0, len(bits_str), 8)]
  bytes_data = [int(bits, 2) for bits in grupos_de_bits]
  bytes_resultantes = bytes(bytes_data)
  return bytes_resultantes

def inversor(contenido_binario):
  #return bytes([~x & 0xFF for x in contenido_binario])
  return contenido_binario

def transmisor(contenido_binario,t_paquete):
  contenido_i = inversor(contenido_binario)
  paquetes = dividir_paquetes(contenido_i, t_paquete)
  prob = probabilidad(paquetes)
  paq_num = list(enumerate(paquetes, start=1))
  paquetes = [[nombre, numero] for numero, nombre in paq_num]
  res = int(input("Que codificacion quieres usar?\nHuffman = 1\nShannon-Fano=2"))
  print("p",paquetes[:5])
  if res == 1:
    lista_h = huffman(prob)
    paquetes = codificar(1, 0, paquetes, lista_h)
  elif res == 2:
    nodos = []
    for nombre, numero in prob:
      nodo = Nodo(nombre, numero)
      nodos.append(nodo)
    nodos = sf(nodos)
    lista_h=[]
    for i in nodos:
      lista_h.append([i.nombre,i.valor_binario])
    paquetes = codificar(1, 0, paquetes, lista_h)
  print("p",paquetes[:5])
  return paquetes, lista_h

def receptor(paquetes_con_ruido, lista_h):
  paquetes = codificar(0,1,paquetes_con_ruido, lista_h )
  print("p",paquetes[:5])
  contenido_reensamblado = unir_paquetes(paquetes)
  contenido_original = inversor(contenido_reensamblado)
  return contenido_original


def introducir_ruido(paquete, probabilidad_ruido):
  lista=[]
  paquete_con_ruido = bytearray(paquete)
  for i in range(len(paquete_con_ruido)):
    if random.random() < probabilidad_ruido:
      paquete_con_ruido[i] = random.randint(0, 255)
      lista.append(1/1024)
  global entropia
  for i in lista:
    entropia -= (i * math.log2(i))
    #print(entropia)
  
  return bytes(paquete_con_ruido)

def dividir_paquetes(contenido_binario, t_paquete):
  paquetes = []
  pps = []
  n = 0
  for i in range(0, len(contenido_binario), t_paquete):
    n += 1
    #print("d", n)
    paquete = contenido_binario[i:i + t_paquete]
    paquetes.append(paquete)
  return paquetes

def unir_paquetes(paquetes):
  paquetes = [item[0] for item in paquetes]
  contenido_reensamblado = ''.join(paquetes)
  return contenido_reensamblado

def canal(paquetes, probabilidad_ruido):
  #paquetes_con_ruido = [introducir_ruido(paquete, probabilidad_ruido) for paquete in paquetes]
  #return paquetes_con_ruido
  return paquetes

def Destino(contenido_binario):
  os.environ['SDL_AUDIODRIVER'] = 'directsound'
  pygame.init()
  mp3_stream = io.BytesIO(contenido_binario)
  pygame.mixer.music.load(mp3_stream)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

def probabilidad(numeros):
  prob=[]
  rep = Counter(numeros)
  #print(rep)
  for i in rep:
    prob.append([i,rep[i]/len(numeros)])
  #print(prob)
  return prob

def huffman(num_ord):
  nodos = []
  for nombre, numero in num_ord:
    nodo = Nodo(nombre, numero)
    nodos.append(nodo)

  while len(nodos) > 1:
    nodos.sort(key=lambda x: x.dato)
    nodo1 = nodos.pop(0)
    #print("nodo1",str(nodo1.nombre))
    nodo2 = nodos.pop(0)
    #print("nodo2",str(nodo2.nombre))
    suma = nodo1.dato + nodo2.dato
    nuevo_nodo = Nodo(suma,suma)
    #print("dato",nuevo_nodo.dato)
    nuevo_nodo.izquierda = nodo2
    nuevo_nodo.derecha = nodo1
    nodos.append(nuevo_nodo)

  arbol_huffman = nodos[0]
  valor_binario=""
  asd=[]
  lista_h = calcular_binario(arbol_huffman, valor_binario, asd)

  #imprimir(arbol_huffman)
  #print(lista_h)
  return lista_h

def calcular_binario(arbol, valor_binario, asd):
  if arbol is not None:
    arbol.valor_binario = valor_binario
    asd=calcular_binario(arbol.izquierda, valor_binario + "0", asd)
    if arbol.izquierda is None:
      asd.append([arbol.nombre,valor_binario])
    asd=calcular_binario(arbol.derecha, valor_binario + "1", asd)
  return asd

def imprimir(arbol):
  if arbol is not None:
    print("Nodo:", arbol.nombre, "Valor Binario:", arbol.valor_binario)
    imprimir(arbol.izquierda)
    imprimir(arbol.derecha)

def sf(nodos):
  nodos.sort(reverse=True, key=lambda x: x.dato)
  izq, der = [], []
  nodo1, nodo2 = nodos.pop(0), nodos.pop(-1)
  izq.append(nodo1)
  der.append(nodo2)
  while len(nodos) > 0:
    iz = 0
    de = 0
    for i in izq:
      iz += i.dato
    for i in der:
      de += i.dato
    if iz > de:
      nodo2 = nodos.pop(-1)
      der.append(nodo2)
    if iz <= de:
      nodo1 = nodos.pop(0)
      izq.append(nodo1)
  for i in range(0,len(izq)):
    izq[i].valor_binario+="0"
  for i in range(0,len(der)):
    der[i].valor_binario+="1"
  if len(izq) >1:
    izq = sf(izq)
  if len(der) >1:
    der = sf(der)
  nodos = []
  for i in izq:
    nodos.append(i)
  for i in der:
    nodos.append(i)
  nodos.sort(reverse=True, key=lambda x: x.dato)
  return nodos

def codificar(uno, dos, paquetes, lista_h):
  for i in range(len(paquetes)):
    for h in lista_h:
      if paquetes[i][0] == h[dos]:
        paquetes[i][0] = h[uno]
        break
  return paquetes


t_paquete = 64
probabilidad_ruido = 0.0001
contenido_bytes = emisor()
contenido_binario =convertir_a_bits(contenido_bytes)

paquetes, lista_h = transmisor(contenido_binario,t_paquete)
#print(paquetes)

paquetes_con_ruido = canal(paquetes, probabilidad_ruido)

contenido_original = receptor(paquetes_con_ruido, lista_h)
#print(entropia)
bytes_resultantes = bits_a_bytes(contenido_original)
Destino(bytes_resultantes)

