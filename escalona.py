import sys
from collections import deque
import copy
import random

arquivo = ""
    
for line in sys.stdin: # recebendo arquivo pela entrada padrão
   arquivo += line

def converte(arquivo): #convertendo a entrada para uma lista de inteiros

    entrada = []
    listaString = arquivo.strip(' ').strip('\n').split('\n')

    for i in listaString:
        aux = i.split(' ')
        elemento = list(map(int, aux))
        entrada.append(elemento)
    
    return entrada

def prioridades(entrada): # PRIORIDADES DINÂMICAS

    retorno = 0
    resposta = 0
    espera = 0
    numProcessos = len(entrada)
    tempoTotal = 0

    for i in range(numProcessos):
        tempoTotal += entrada[i][1]
        entrada[i].append(5)
        entrada[i].append(False)

    i = 0

    while i <= tempoTotal:
      
        valor = 0
        flag = False
        
        for j in range(len(entrada)):
          
            if(entrada[j][0] <= i and (entrada[j][2] > entrada[valor][2] or not flag)):
                valor = j
                flag = True
            entrada[j][2] += 1
            if(entrada[j][0] <= i):
                espera += 1

        if not flag:
            i += 1
            continue
        
        entrada[valor][1] -= 1
        entrada[valor][2] -= 2
        espera -= 1

        if not entrada[valor][3]:
            entrada[valor][3] = True
            resposta += (i - entrada[valor][0])

        i += 1

        if entrada[valor][1] == 0:
            retorno += (i - entrada[valor][0])
            entrada.pop(valor)
            if len(entrada) == 0:
                break
        
    retorno /= numProcessos
    resposta /= numProcessos
    espera /= numProcessos

    print('PRI {:.2f} {:.2f} {:.2f}'.format(retorno, resposta, espera))

def loteria(entrada): # LOTERIA

    retorno = 0
    resposta = 0
    espera = 0
    
    numProcessos = len(entrada)
    tempoTotal = 0
    
    for i in range(numProcessos):
        tempoTotal += entrada[i][1]
        entrada[i].append(False)

    i = 0

    while i <= tempoTotal:
        cont = 0
        flag = False
        
        while cont < len(entrada)*3:
            valor = random.randrange(0, len(entrada))
            if(entrada[valor][0] <= i):
                flag = True
                break
            cont += 1
        
        if not flag:
            i += 1
            continue
        
        if entrada[valor][1] > 1:
            tempoExec = 2
        else: 
            tempoExec = 1

        entrada[valor][1] -= tempoExec

        if not entrada[valor][2]:
            entrada[valor][2] = True
            resposta += (i - entrada[valor][0])

        for j in range(len(entrada)):
            if(j != valor):
                if(entrada[j][0] <= i):
                    espera += tempoExec
                if(tempoExec == 2 and entrada[j][0] == i + 1):
                    espera += 1

        i += tempoExec

        if entrada[valor][1] == 0:
            retorno += (i - entrada[valor][0])
            entrada.pop(valor)
            if(len(entrada) == 0):
                break
        
    retorno /= numProcessos
    resposta /= numProcessos
    espera /= numProcessos

    print('LOT {:.2f} {:.2f} {:.2f}'.format(retorno, resposta, espera))

def roundRobin(entrada): # ROUND ROBIN

    retorno = 0
    resposta = 0
    espera = 0
    
    numProcessos = len(entrada)
    tempoTotal = 0
    filaCircular = deque()
    
    for i in range(numProcessos):
      
        tempoTotal += entrada[i][1]
        entrada[i].append(False)
        filaCircular.append(entrada[i])

    i = 0

    while i <= tempoTotal:
        flag = False
        for j in range(len(filaCircular)):
            if(filaCircular[0][0] <= i):
                flag = True
                break
            else:
                filaCircular.rotate(-1)

        if not flag:
            i += 1
            continue
        
        if filaCircular[0][1] > 1:
            tempoExec = 2
        else: 
            tempoExec = 1

        filaCircular[0][1] -= tempoExec

        if not filaCircular[0][2]:
            filaCircular[0][2] = True
            resposta += (i - filaCircular[0][0])

        for j in range(1, len(filaCircular)):
            if(filaCircular[j][0] <= i):
                espera += tempoExec
            if(tempoExec == 2 and filaCircular[j][0] == i + 1):
                espera += 1

        i += tempoExec

        if filaCircular[0][1] == 0:
            retorno += (i - filaCircular[0][0])
            filaCircular.rotate(-1)
            filaCircular.pop()
            if len(filaCircular) == 0:
                break
        else:
            filaCircular.rotate(-1)

    retorno /= numProcessos 
    resposta /= numProcessos
    espera /= numProcessos

    print('RR {:.2f} {:.2f} {:.2f}'.format(retorno, resposta, espera))

# CONVERTENDO O ARQUIVO DE ENTRADA
entradaConv = converte(arquivo)

# CHAMADA DAS FUNÇÕES
prioridades(copy.deepcopy(entradaConv))
loteria(copy.deepcopy(entradaConv))
roundRobin(copy.deepcopy(entradaConv))