#Calcula a DIFERENÇA entre dois vetores
import random
vetorA = [0]*5
vetorB = [0]*3
n = len(vetorA)
m = len(vetorB)

def preencheVetor():
    for x in range(n):
        vetorA[x] = random.randint(0,10)
    print(vetorA)
    for x in range(m):
        vetorB[x] = random.randint(0,10)
    print(vetorB)

def diferença():
    lista = []
    for x in range(n):
        for i in range(m):
            if vetorA[x] == vetorB[i]:
                if vetorA[x] in lista:
                    index = lista.index(vetorA[x])
                    del lista[index]
                break
            if vetorA[x] != vetorB[i]:
                if vetorA[x] not in lista:
                    lista.append(vetorA[x])

    print(f'Diferença entre os dois vetores: {lista}')


preencheVetor()
diferença()