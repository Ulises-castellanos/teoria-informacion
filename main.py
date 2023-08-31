def uno():
  with open('prue.mp3', 'rb') as mp3_file:
    contenido_binario = mp3_file.read()
  return contenido_binario

def dos(contenido_binario):
  return bytes([~x & 0xFF for x in contenido_binario])
 
def tres(contenido_binario):
  with open('resultado.mp3', 'wb') as mp3_file:
    mp3_file.write(contenido_binario)

var = uno()
jj = dos(var)
pp = dos(jj)
tres(pp)
