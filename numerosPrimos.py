import timeit

tempo_inicial=timeit.default_timer() # em segundos

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

tempo_final=timeit.default_timer() # em segundos
print(f"{tempo_final - tempo_inicial} segundos")


