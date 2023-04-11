import sys
import copy
from collections import deque

arquivo = ""

for line in sys.stdin: # recebendo arquivo pela entrada padrão
    arquivo += line

def converte(arquivo): # convertendo a entrada para uma lista de inteiros
  
    requisicoes = []

    listaString = arquivo.strip(' ').strip('\n').split('\n')
    ultimoCil = int(listaString[0])
    posInicial = int(listaString[1])

    listaString.pop(0)
    listaString.pop(0)

    for i in listaString:
        aux = int(i)
        requisicoes.append(aux)
    
    return (requisicoes, posInicial)

def FCFS(requisicoes, posInicial): # FIRST TO COME FIRST TO SERVE
  
    anterior = posInicial
    percorridos = 0

    for i in requisicoes:
        percorridos += abs(i - anterior)
        anterior = i

    print('FCFS {}'.format(percorridos))

def SSTF(requisicoes, posInicial): # SHORTEST SEEK TIME FIRST
  
    anterior = posInicial
    total_req = len(requisicoes)
    percorridos = 0

    for i in range(total_req):
        maisProximo = 0
        dist_i = abs(requisicoes[maisProximo] - anterior)

        for j in range(len(requisicoes)):
            dist_j = abs(requisicoes[j] - anterior)

            if dist_j < dist_i and dist_j > 0:
                dist_i = dist_j
                maisProximo = j

        percorridos += dist_i
        anterior = requisicoes[maisProximo]
        requisicoes.pop(maisProximo)

    print('SSTF {}'.format(percorridos))
        
def elevador(requisicoes, posInicial): # ALGORITMO DO ELEVADOR
  
    anterior = posInicial
    requisicoes.sort()
    atual = 0
    percorridos = 0

    for i in range(len(requisicoes)):
        atual = i

        if requisicoes[i] > anterior:
            break
    
    if atual == (len(requisicoes) - 1):
        atual += 1
    else:
        for i in range(atual, len(requisicoes)):
            percorridos += abs(requisicoes[i] - anterior)
            anterior = requisicoes[i]

    if atual > 0:
        for i in range(atual - 1, -1, -1):
            percorridos += abs(requisicoes[i] - anterior)
            anterior = requisicoes[i]

    print('ELEVADOR {}'.format(percorridos))

# convertendo o arquivo de entrada  
requisicoes, posInicial = converte(arquivo)

# chamada das funções 
FCFS(copy.deepcopy(requisicoes), posInicial)
SSTF(copy.deepcopy(requisicoes), posInicial)
elevador(copy.deepcopy(requisicoes), posInicial)