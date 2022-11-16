import time

tempo_inicial = time.time()
mult = 0
lista = []

for n in range(2, 100):         #Percorre os números de 2 a 100

    for div in range(2, n-1):   #Percorre os divisores de 2 ao número a se verificar
        if (n % div == 0):      #Verifica se a divisão resulta em resto zero
            mult += 1           #Soma um à variável mult

    if (mult == 0):             #Verifica se a variável mult é nula
        lista.append(n)         #Acrescenta o número n à lista de números primos
    else:               
        mult = 0                #Zera a variável mult

print(lista)                    #Imprime a lista de números primos de 1 a 100

time.sleep(1)
tempo_final = time.time()
print(f"O programa demorou {tempo_final - tempo_inicial} segundos para executar")


