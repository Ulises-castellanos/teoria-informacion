import pygame
import io
import os
import random
import math
from collections import Counter

entropia = 0
def emisor():
  with open('prue2.mp3', 'rb') as mp3_file:
    contenido_binario = mp3_file.read()
  return contenido_binario

def convertir_a_bits(bytes_data):
  bits = [format(byte, '08b') for byte in bytes_data]
  bits_str = ''.join(bits)
  return bits_str  

def inversor(contenido_binario):
  #return bytes([~x & 0xFF for x in contenido_binario])
  return contenido_binario

def transmisor(contenido_binario,t_paquete):
  contenido_i = inversor(contenido_binario)
  paquetes = dividir_paquetes(contenido_i, t_paquete)
  return paquetes

def receptor(paquetes_con_ruido):
  contenido_reensamblado = unir_paquetes(paquetes_con_ruido)
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
  n = 0
  for i in range(0, len(contenido_binario), t_paquete):
    n += 1
    print("d", n)
    paquete = contenido_binario[i:i + t_paquete]
    print(paquete)
    paquetes.append(paquete)
  return paquetes

def unir_paquetes(paquetes):
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

def bits_a_bytes(bits_str):
  grupos_de_bits = [bits_str[i:i+8] for i in range(0, len(bits_str), 8)]
  bytes_data = [int(bits, 2) for bits in grupos_de_bits]
  bytes_resultantes = bytes(bytes_data)
  return bytes_resultantes

t_paquete = 4
probabilidad_ruido = 0.0001
contenido_bytes = emisor()
contenido_binario =convertir_a_bits(contenido_bytes)

paquetes = transmisor(contenido_binario,t_paquete)

prob = probabilidad(paquetes)
num_ord = sorted(prob, key=lambda x: (x[1], x[0]))
print(num_ord)
print(len(num_ord))
paquetes_con_ruido = canal(paquetes, probabilidad_ruido)

contenido_original = receptor(paquetes_con_ruido)
print(entropia)
bytes_resultantes = bits_a_bytes(contenido_original)
Destino(bytes_resultantes)