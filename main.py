import pygame
import io
import os
import random
import math

entropia = 0
def emisor():
  with open('prue.mp3', 'rb') as mp3_file:
    contenido_binario = mp3_file.read()
  return contenido_binario

def inversor(contenido_binario):
  return bytes([~x & 0xFF for x in contenido_binario])

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
    paquetes.append(paquete)
  return paquetes

def unir_paquetes(paquetes):
  n = 0
  contenido_binario = b""
  for paquete in paquetes:
    n += 1
    print("u", n)
    contenido_binario += paquete
  return contenido_binario

def canal(paquetes, probabilidad_ruido):
  paquetes_con_ruido = [introducir_ruido(paquete, probabilidad_ruido) for paquete in paquetes]
  return paquetes_con_ruido

def Destino(contenido_binario):
  os.environ['SDL_AUDIODRIVER'] = 'directsound'
  pygame.init()
  mp3_stream = io.BytesIO(contenido_binario)
  pygame.mixer.music.load(mp3_stream)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

t_paquete = 1024
probabilidad_ruido = 0.0001
contenido_binario = emisor()

paquetes = transmisor(contenido_binario,t_paquete)
paquetes_con_ruido = canal(paquetes, probabilidad_ruido)

contenido_original = receptor(paquetes_con_ruido)
print(entropia)
Destino(contenido_original)
