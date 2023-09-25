import math
import random

num_lanzamientos = 3

conteo = 0
prob = []

for i in range(num_lanzamientos):
    numero_random = random.randint(1, 2)
    if numero_random == 2:
        conteo += 1

prob_si = conteo / num_lanzamientos
prob_no = 1 - prob_si
print(prob_si)
print(prob_no)

if prob_si > 0:
    prob.append(prob_si)
if prob_no > 0:
    prob.append(prob_no)

entropia = 0
for p in prob:
    entropia -= (p * math.log2(p))
    print(entropia)

print(f"La entropía es {entropia} bits")
