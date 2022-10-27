import time

tempo_inicial = time.time()
mult = 0
lista = []

for n in range(2, 100):

    for div in range(2, n-1):
        if (n % div == 0):
            mult += 1

    if (mult == 0):
        lista.append(n)
        print(lista)
    else:
        mult = 0

time.sleep(1)
tempo_final = time.time()
print(f"{tempo_final - tempo_inicial} segundos")


