class Nodo:
  def __init__(self, nombre, dato):
    self.nombre = nombre
    self.dato = dato
    self.izquierda = None
    self.derecha = None
    self.valor_binario = ""

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

#prueba = [['0111', 0.05357971322995639], ['1110', 0.054764126999721635], ['1111', 0.055956727961443783], ['1101', 0.056832757500832366], ['1011', 0.0570510826196831], ['0011', 0.057659663888479526], ['1100', 0.0576896835923215], ['0110', 0.06082537811181521], ['0101', 0.06360083618520519], ['1010', 0.06374820564042945], ['0001', 0.0641029839585619], ['1001', 0.06486712187453947], ['1000', 0.0661934469715577], ['0010', 0.06994590995180473], ['0100', 0.07369564386806612], ['0000', 0.07948671764558192]]
#prueba = [['11111000', 0.0023360787717028814], ['11111100', 0.0024452413311282497], ['01111100', 0.0025325713786685444], ['10111110', 0.002565320146496155], ['01111110', 0.0026089851702663022], ['10111100', 0.002619901426208839], ['11110000', 0.0026744827059215232], ['11111001', 0.0027454383695480126], ['10111111', 0.0027618127534618175], ['00101111', 0.002794561521289428], ['00110111', 0.002794561521289428], ['00111111', 0.0028054777772319648], ['11101111', 0.002876433440858454], ['01111000', 0.0029091822086860647], ['11011110', 0.002914640336657333], ['11110111', 0.002914640336657333], ['10011111', 0.0029200984646286015], ['01011111', 0.00292555659259987], ['11011100', 0.00292555659259987], ['11001111', 0.002941930976513675], ['00011111', 0.0029473891044849436], ['11011111', 0.003007428512168896], ['11001110', 0.003018344768111433], ['11100000', 0.003018344768111433], ['11110010', 0.0030238028960827014], ['01110111', 0.0030401772799965067], ['01111001', 0.003056551663910312], ['01011110', 0.0030674679198528488], ['10110011', 0.0030674679198528488], ['11000111', 0.0030674679198528488], ['00111110', 0.003072926047824117], ['01101111', 0.0030783841757953856], ['10011110', 0.0030893004317379224], ['11110011', 0.0031165910715942645], ['11111101', 0.0031329654555080698], ['11110001', 0.003149339839421875], ['11101110', 0.0031657142233356803], ['11000110', 0.0031711723513069487], ['01111111', 0.003176630479278217], ['11100010', 0.003176630479278217], ['11010111', 0.0031820886072494855], ['11001101', 0.003187546735220754], ['00001111', 0.0031930048631920224], ['11011101', 0.0031930048631920224], ['00111011', 0.0031984629911632908], ['10001111', 0.0031984629911632908], ['10011011', 0.0032312117589909013], ['00110101', 0.0032475861429047065], ['00010111', 0.0032585023988472434], ['11100011', 0.0032585023988472434], ['00011110', 0.00326941865478978], ['01111011', 0.00326941865478978], ['01110011', 0.0032748767827610486], ['11100111', 0.0032748767827610486], ['00011101', 0.003280334910732317], ['10101111', 0.003280334910732317], ['10111011', 0.003291251166674854], ['11100001', 0.0033021674226173907], ['01111101', 0.003307625550588659], ['10110110', 0.003307625550588659], ['10110111', 0.003307625550588659], ['10111000', 0.0033130836785599275], ['11101101', 0.0033130836785599275], ['00000111', 0.0033239999345024644], ['00111010', 0.0033403743184162696], ['11011011', 0.0033512905743588064], ['11110110', 0.0033512905743588064], ['10111101', 0.0033622068303013433], ['11110101', 0.0033676649582726117], ['11000000', 0.00337312308624388], ['01100111', 0.0033785812142151485], ['00110011', 0.003384039342186417], ['11011000', 0.0034058718540714906], ['10101110', 0.003411329982042759], ['01001111', 0.0034277043659565643], ['11111110', 0.0034331624939278327], ['10101011', 0.003438620621899101], ['11111010', 0.0034440787498703695], ['01111010', 0.003449536877841638], ['10111010', 0.003449536877841638], ['11000001', 0.003449536877841638], ['11011010', 0.0034549950058129063], ['01110110', 0.0034932019016117853], ['10011101', 0.0034932019016117853], ['11010110', 0.0034932019016117853], ['00100111', 0.0034986600295830537], ['00111000', 0.0034986600295830537], ['10110010', 0.003504118157554322], ['11000011', 0.003531408797410664], ['00110110', 0.0035368669253819326], ['11011001', 0.0035368669253819326], ['00011011', 0.0035477831813244694], ['10100011', 0.003553241309295738], ['10011100', 0.0035586994372670063], ['11010000', 0.0035641575652382747], ['01101100', 0.003569615693209543], ['01010111', 0.0035750738211808115], ['01110001', 0.0035750738211808115], ['00000110', 0.0035859900771233483], ['11001001', 0.0036023644610371536], ['11010011', 0.0036023644610371536], ['00101011', 0.0036132807169796904], ['01100110', 0.003618738844950959], ['00111001', 0.0036241969729222273], ['10011010', 0.0036405713568360325], ['10100110', 0.0036405713568360325], ['01100000', 0.0036514876127785693], ['01100011', 0.0036514876127785693], ['11010101', 0.0036514876127785693], ['00101101', 0.0036569457407498378], ['10010111', 0.003673320124663643], ['00001110', 0.0036787782526349114], ['01101110', 0.0036787782526349114], ['10000111', 0.0036787782526349114], ['10111001', 0.0036787782526349114], ['11101011', 0.00368423638060618], ['11100100', 0.003700610764519985], ['01110100', 0.0037060688924912535], ['10010011', 0.003711527020462522], ['01000011', 0.0037169851484337903], ['11000101', 0.0037224432764050588], ['11001011', 0.0037224432764050588], ['11001100', 0.0037224432764050588], ['01011011', 0.0037333595323475956], ['10000011', 0.0037333595323475956], ['11101000', 0.0037333595323475956], ['01101010', 0.0037442757882901324], ['00000011', 0.003749733916261401], ['01110000', 0.0037606501722039377], ['10001110', 0.0037606501722039377], ['10110101', 0.0037606501722039377], ['10000001', 0.0037715664281464745], ['11100101', 0.0037715664281464745], ['01000111', 0.0037824826840890113], ['01001110', 0.0037824826840890113], ['01010110', 0.0037824826840890113], ['01110101', 0.0037824826840890113], ['00000101', 0.0037879408120602798], ['11010100', 0.003815231451916622], ['00100110', 0.0038534383477155008], ['11100110', 0.0038588964756867687], ['10110001', 0.003864354603658037], ['01101011', 0.0038916452435143792], ['10010101', 0.0038916452435143792], ['00010011', 0.0039080196274281845], ['00001101', 0.003913477755399453], ['00010110', 0.00392439401134199], ['00011001', 0.00392439401134199], ['00010101', 0.003929852139313258], ['01001101', 0.003929852139313258], ['10101000', 0.003929852139313258], ['00011010', 0.003935310267284527], ['10101100', 0.003940768395255795], ['01100010', 0.003946226523227064], ['10100001', 0.003946226523227064], ['11000100', 0.003946226523227064], ['11101010', 0.003946226523227064], ['01001011', 0.003951684651198332], ['11001000', 0.003951684651198332], ['01011101', 0.003957142779169601], ['10100000', 0.0039680590351121375], ['10110100', 0.003989891546997211], ['10101101', 0.003995349674968479], ['11001010', 0.004011724058882285], ['00011100', 0.004017182186853553], ['10011001', 0.004017182186853553], ['10000101', 0.004022640314824822], ['00001011', 0.0040335565707673585], ['00110001', 0.0040335565707673585], ['01101101', 0.0040335565707673585], ['01001100', 0.0040390146987386265], ['11110100', 0.0040390146987386265], ['01011100', 0.004055389082652432], ['01010011', 0.0040608472106237], ['00111100', 0.004066305338594969], ['11010010', 0.004066305338594969], ['01000110', 0.004077221594537506], ['10010110', 0.004082679722508774], ['10100101', 0.004093595978451311], ['01011000', 0.004126344746278921], ['01011010', 0.004126344746278921], ['11101100', 0.00413180287425019], ['00110100', 0.004142719130192727], ['10000110', 0.004142719130192727], ['10110000', 0.004148177258163995], ['10011000', 0.0041700097700490685], ['01110010', 0.004175467898020337], ['01010101', 0.004180926025991605], ['10001101', 0.004191842281934142], ['10010001', 0.004191842281934142], ['11000010', 0.004197300409905411], ['00111101', 0.004208216665847948], ['01011001', 0.004208216665847948], ['01101000', 0.0042355073057042895], ['00100011', 0.004246423561646826], ['10001100', 0.004246423561646826], ['10101010', 0.004273714201503169], ['00101110', 0.004279172329474437], ['10101001', 0.004284630457445706], ['10100111', 0.004290088585416974], ['00010001', 0.0042955467133882425], ['00100101', 0.0042955467133882425], ['00000001', 0.004328295481215853], ['10100010', 0.004328295481215853], ['11010001', 0.004344669865129658], ['10000010', 0.004350127993100927], ['00110010', 0.004355586121072195], ['00001100', 0.004388334888899805], ['00001010', 0.004421083656727416], ['01000101', 0.004426541784698684], ['01000001', 0.0044319999126699525], ['00110000', 0.004442916168612489], ['00100001', 0.004448374296583757], ['01100100', 0.004453832424555026], ['01100101', 0.004459290552526294], ['10001011', 0.004464748680497563], ['00011000', 0.0045029555762964414], ['00101100', 0.0045029555762964414], ['01000010', 0.004519329960210247], ['11101001', 0.004519329960210247], ['00101001', 0.004535704344124052], ['01010000', 0.004552078728037858], ['01101001', 0.004573911239922931], ['10000100', 0.004617576263693079], ['01010100', 0.004639408775578152], ['01000000', 0.004677615671377031], ['10001000', 0.0046939900552908365], ['00010100', 0.004748571335003521], ['01100001', 0.0047649457189173254], ['10001001', 0.004770403846888594], ['10010000', 0.004808610742687473], ['01001010', 0.004874108278342694], ['01010001', 0.004874108278342694], ['00101000', 0.004879566406313963], ['00101010', 0.004906857046170304], ['00001000', 0.004912315174141573], ['00001001', 0.004917773302112841], ['10010010', 0.004934147686026647], ['01001001', 0.004939605813997915], ['00010010', 0.004945063941969184], ['01010010', 0.004945063941969184], ['00100010', 0.004977812709796794], ['00010000', 0.004999645221681868], ['10100100', 0.0050269358615382094], ['10001010', 0.005076059013279626], ['00100000', 0.005190679700676262], ['01001000', 0.005201595956618799], ['00000100', 0.005228886596475141], ['00100100', 0.005523625506923635], ['11111011', 0.005687369346061687], ['10000000', 0.005867487569113546], ['00000010', 0.007242935817873186], ['01000100', 0.007324807737442212], ['10010100', 0.0073848471451261645], ['11111111', 0.008858541697368636], ['00000000', 0.015784906092908255]]
paquetes =  ["nueve","uno","dos","dos","tres","tres","tres","cuatro","cuatro","cuatro","cuatro","cinco","cinco","cinco","cinco","cinco","seis","seis","seis","seis","seis","seis","siete","siete","siete","siete","siete","siete","siete","ocho","ocho","ocho","ocho","ocho","ocho","ocho","ocho","nueve","nueve","nueve","nueve","nueve","nueve","nueve","nueve"]
num_ord = [["uno",1],["dos",2],["tres",3],["cuatro",4],["cinco",5],["seis",6],["siete",7],["ocho",8],["nueve",9]]

nodos = []
for nombre, numero in num_ord:
  nodo = Nodo(nombre, numero)
  nodos.append(nodo)

nodos = sf(nodos)
lista_h=[]
for i in nodos:
  lista_h.append([i.nombre,i.valor_binario])
