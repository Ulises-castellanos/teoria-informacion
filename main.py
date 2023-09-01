def emisor():
  with open('prue.mp3', 'rb') as mp3_file:
    contenido_binario = mp3_file.read()
  return contenido_binario

def inversor(contenido_binario):
  return bytes([~x & 0xFF for x in contenido_binario])

def dividir_paquetes(contenido_binario, t_paquete):
  paquetes = []
  n=0
  for i in range(0, len(contenido_binario), t_paquete):
    n+=1
    #print("d", n)
    paquete = contenido_binario[i:i + t_paquete]
    paquetes.append(paquete)
  return paquetes

def unir_paquetes(paquetes):
  n=0
  contenido_binario = b""
  for paquete in paquetes:
    n+=1
    #print("u", n)
    contenido_binario += paquete
  return contenido_binario

def Destino(contenido_binario):
  with open('resultado.mp3', 'wb') as mp3_file:
    mp3_file.write(contenido_binario)

t_paquete = 4

contenido_binario = emisor()
contenido_i = inversor(contenido_binario)

paquetes = dividir_paquetes(contenido_i, t_paquete)

contenido_reensamblado = unir_paquetes(paquetes)

contenido_original = inversor(contenido_reensamblado)

Destino(contenido_original)
