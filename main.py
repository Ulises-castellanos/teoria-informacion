import pygame
import io
import os
import random
from collections import Counter
import hashlib

entropia = 0

#Esquema de comunicacion 
def emisor():
  with open('prue4.mp3', 'rb') as mp3_file:
    contenido_binario = mp3_file.read()
  bits = [format(byte, '08b') for byte in contenido_binario]
  bits_str = ''.join(bits)
  return bits_str 

def transmisor(contenido_binario,tamaño):
  paquetes = []
  for i in range(0, len(contenido_binario), tamaño):
    paquete = contenido_binario[i:i + tamaño]
    paquetes.append(paquete)

  prob = probabilidad(paquetes)
  paq_num = list(enumerate(paquetes, start=1))
  paquetes = [[nombre, numero] for numero, nombre in paq_num]
  
  res = int(input("Que codificacion quieres usar?\nHuffman = 1\nShannon-Fano=2\nInversor=3\nDelta=4\n"))
  
  if res == 1:
    handshake = huffman(prob)
  
  elif res == 2:
    nodos = []
    for nombre, numero in prob:
      nodo = Nodo(nombre, numero)
      nodos.append(nodo)
    nodos = sf(nodos)
    handshake=[]
    for i in nodos:
      handshake.append([i.nombre,i.valor_binario])
    print("Lista handshake de Shannon-Fano\n",handshake[:5],"\n")
  
  elif res == 3:
    handshake = inversor(prob)
  
  elif res == 4:
    handshake = delta(prob)
  
  print("Paquetes sin codificar\n",paquetes[:5],"\n")
  paquetes = codificar(1, 0, paquetes, handshake)
  print("Paquetes codificados\n",paquetes[:5],"\n")
  return paquetes, handshake

def ruido_perd(paq, prob_ruido):
  num = random.randint(1, 100)
  if num <= prob_ruido:
    paq = None
  return paq

#Canal con modulacion
def canal(paquetes, prob_ruido):
  filas = 5
  columnas = 2
  canales = [[None for n in range(columnas)] for n in range(filas)]
  nuevos_paq = []
  res = int(input("Que canal deseas usar? del 1 al 5\n"))
  indice = 0
  pa_per =[]
  can_per = None
  fin = len(paquetes)
  paquetes = hash(paquetes)
  while len(paquetes)> len(nuevos_paq):
    if len(paquetes)>0:
      if indice < len(paquetes):
        paq = paquetes[indice]
      else: paq = None
    canales[res-1][1] = canales[res-1][0]
    canales[res-1][0] = paq
    paqr = ruido_perd(canales[res-1][1], prob_ruido)
    if paqr is not None:
      print("paquete enviado por el canal ",res,":", paqr)
      nuevos_paq.append(paqr)
      if len(nuevos_paq) > 1 and  nuevos_paq[-1][1] != nuevos_paq[-2][1]+1 :
        num = nuevos_paq[-1][1]-nuevos_paq[-2][1]-1
        perd= nuevos_paq[-1][1]
        print("paquetes perdidos", num)
        for i in range(0,num):
          perd -=1
          pa_per.append(perd)
        pa_per.append(None)
        print(pa_per)
        indice = nuevos_paq[-1][1]-1
        if res < filas:
          canales[res-1][0], canales[res-1][1] = None, None
          if canales[res][0] != None or canales[res][1] != None:
            if can_per == None:
              can_per =res
              print("canal perdidos", can_per)
            if res == 4:
              res == 1
            else: res +=2
          else: 
            if can_per == None:
              if res == 4:
                can_per = 1
              else: can_per = res + 2
              print("canal perdidos", can_per)
            res +=1
        else:
          canales[res-1][0], canales[res-1][1] = None, None
          if canales[0][0] != None or canales[0][1] != None:
            if can_per == None:
              can_per =res
            res = 2
          else : 
            if can_per == None:
              can_per = 2
              print("canal perdidos", can_per)
            res = 1
        print("cambio de canal al", res)
      elif nuevos_paq[0][1] > 1 and len(nuevos_paq) == 1:
        perd = nuevos_paq[0][1]
        print("paquetes perdidos", perd-1)
        while perd > 1:
          perd -=1
          pa_per.append(perd)
        pa_per.append(None)
        print(pa_per)
        indice = nuevos_paq[-1][1]-1
        if res < filas:
          canales[res-1][0], canales[res-1][1] = None, None
          if canales[res][0] != None or canales[res][1] != None:
            if can_per == None:
              can_per =res
              print("canal perdidos", can_per)
            if res == 4:
              res == 1
            else: res +=2
          else: 
            if can_per == None:
              if res == 4:
                can_per = 1
              else: can_per = res + 2
              print("canal perdidos", can_per)
            res +=1
        else:
          canales[res-1][0], canales[res-1][1] = None, None
          if canales[0][0] != None or canales[0][1] != None:
            if can_per == None:
              can_per = 1
              print("canal perdidos", can_per)
            res = 2
          else : 
            if can_per == None:
              can_per = 2
              print("canal perdidos", can_per)
            res = 1
        print("cambio de canal al", res)
    elif indice == fin:
        perd = fin
        while perd > nuevos_paq[-1][1]:
          pa_per.append(perd)
          perd-=1
        pa_per.append(None)
        print(pa_per)
        if can_per == None:
          if res < 5:
            can_per = res+1
          else: can_per =1
    indice +=1
    if len(pa_per) > 0 :
      in_per = pa_per.pop(0)
      if in_per == None:
        paq = in_per
      else: 
        paq = paquetes[in_per-1]
      canales[can_per-1][1] = canales[can_per-1][0]
      canales[can_per-1][0] = paq
      if canales[can_per-1][1] is not None:
        nuevos_paq.append(canales[can_per-1][1])
      nuevos_paq = sorted(nuevos_paq, key=lambda x: x[1])
    else: 
      if can_per != None:
        canales[can_per-1][0], canales[can_per-1][1] = None, None
      can_per = None
  input("Paquetes recibidos con exito, presione enter")
  return nuevos_paq

def hash(paquetes):
  for i in range(0,len(paquetes)):
    paquetes[i][0] = hashlib.sha256( paquetes[i][0].encode()).hexdigest()
  return paquetes

def hash_handshake(handshake):
  for i in range(0,len(handshake)):
    hs = hashlib.sha256( handshake[i][1].encode()).hexdigest()
    handshake[i].append(hs)
  return handshake

def b_binario(hs, paquete):
  hs_n = []
  print("\nhash en handshake", [l[2] for l in hs] )
  print("paquete",paquete)
  print("hash de enmedio",hs[len(hs)//2][2])
  if len(hs) == 2 and paquete == hs[0][2]: return hs[0][1]
  elif paquete == hs[len(hs)//2][2]: return hs[len(hs)//2][1] 
  elif paquete > hs[len(hs)//2][2]:
    hs_n = hs[(len(hs) // 2):]
    resultado = b_binario(hs_n, paquete)
  elif paquete < hs[len(hs)//2][2]:
    hs_n = hs[:(len(hs) // 2)+1]
    resultado = b_binario(hs_n, paquete)
  return resultado

def receptor(paquetes_hasheados, handshake):
  handshake = hash_handshake(handshake)
  handshake = sorted(handshake, key=lambda x: x[2])
  paq_codificados = []
  for i in paquetes_hasheados:
    tempo = b_binario(handshake, i[0])
    paq_codificados.append([tempo, i[1]])
    print("De hash a codificado",tempo)

  paquetes = codificar(0,1,paq_codificados, handshake )
  print("Paquetes restablecidos\n")
  paquetes = [item[0] for item in paquetes]
  contenido_original = ''.join(paquetes)
  grupos_de_bits = [contenido_original[i:i+8] for i in range(0, len(contenido_original), 8)]
  bytes_data = [int(bits, 2) for bits in grupos_de_bits]
  contenido_bytes = bytes(bytes_data)
  return contenido_bytes

def destino(contenido_binario):
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
  for i in rep:
    prob.append([i,rep[i]/len(numeros)])
  return prob

class Nodo:
  def __init__(self, nombre, dato):
    self.nombre = nombre
    self.dato = dato
    self.izquierda = None
    self.derecha = None
    self.valor_binario = ""

### Primer metodo de codificacion Huffman
def huffman(num_ord):
  nodos = []
  for nombre, numero in num_ord:
    nodo = Nodo(nombre, numero)
    nodos.append(nodo)

  while len(nodos) > 1:
    nodos.sort(key=lambda x: x.dato)
    nodo1 = nodos.pop(0)
    nodo2 = nodos.pop(0)
    suma = nodo1.dato + nodo2.dato
    nuevo_nodo = Nodo(suma,suma)
    #print("dato",nuevo_nodo.dato)
    nuevo_nodo.izquierda = nodo2
    nuevo_nodo.derecha = nodo1
    nodos.append(nuevo_nodo)

  arbol_huffman = nodos[0]
  valor_binario=""
  asd=[]
  handshake = calcular_binario(arbol_huffman, valor_binario, asd)
  #imprimir(arbol_huffman)
  print("Lista handshake de Huffman\n",handshake[:5],"\n")
  return handshake

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

### Segundo metodo de codificacfion Shannon-Fano
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

### Tercer metodo de codificacion Inversor
### Toma cada bit y lo convierte en su inverso, es decir convierte 1 a 0 y viceversa
def inversor(prob):
  handshake = []
  for i in prob:
    paq_l = list(i[0])
    for n in range(len(paq_l)):
      if paq_l[n] == "1":
        paq_l[n] = "0"
      else:
        paq_l[n] = "1"
    uno = "".join(paq_l)
    handshake.append([i[0],uno])
  print("Lista handshake de Inversor\n",handshake[:5],"\n")
  return handshake

### Cuarto metodo de codificacion Delta
### Conserva el primer bit, recorre el resto de los bits comparando el bit actual con el anterior, 
### si es el mismo se agrega un 0 y si es distinto se agrega 1
def delta(prob):
  handshake= []
  for i in prob:
    delt = [i[0][0]]
    for n in range(1, len(i[0])):
      act = i[0][n]
      ant = i[0][n - 1]
      if act == ant:
        delt.append("0")
      else:
        delt.append("1")
    var=''.join(delt)
    handshake.append([i[0],var])
  print("Lista handshake de Delta\n",handshake[:5],"\n")
  return handshake

def codificar(uno, dos, paquetes, handshake):
  for i in range(len(paquetes)):
    for h in handshake:
      if paquetes[i][0] == h[dos]:
        paquetes[i][0] = h[uno]
        break
  return paquetes

tamaño = 1024
probabilidad_ruido = 15

contenido_binario = emisor()

paquetes, handshake = transmisor(contenido_binario,tamaño)

paquetes = canal(paquetes, probabilidad_ruido)

original = receptor(paquetes, handshake)

destino(original)