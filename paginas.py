import sys
import copy
from collections import deque

arquivo = ""

for line in sys.stdin: # recebendo arquivo pela entrada padrão
    arquivo += line

def converte(arquivo): # convertendo a entrada para uma lista de inteiros
  
    referencias = []
    listaString = arquivo.strip(' ').strip('\n').split('\n')
    numQuadros = int(listaString[0])
    listaString.pop(0)

    for i in listaString:
        referencias.append(int(i))
    
    return (referencias, numQuadros)

def segundaChance(referencias, numQuadros): # SEGUNDA CHANCE
  
    faltas = 0
    refCont = 0
    memoria = [[None, 0] for x in range(numQuadros)]
    filaCircular = deque()
    
    for i in range(len(referencias)):
      
        flag = False
        
        for j in range(numQuadros):
          
            if memoria[j][0] == None:
                memoria[j][0] = referencias[i]
                memoria[j][1] = 1
                filaCircular.append(j)
                faltas += 1
                flag = True
                break
            
            if memoria[j][0] == referencias[i]:
                memoria[j][1] = 1
                flag = True
                break
        
        if not flag:
            index = filaCircular[0]
            
            while memoria[index][1] != 0:
                filaCircular.rotate(-1)
                index = filaCircular[0]
            
            filaCircular.rotate(-1)

            memoria[index][0] = referencias[i]
            memoria[index][1] = 1
            faltas += 1

        refCont += 1
        
        if refCont == 4:
            refCont = 0
            
            for j in range(numQuadros):
                memoria[j][1] = 0

    print('SC {}'.format(faltas))

def otimo(referencias, numQuadros): # ALGORITMO ÓTIMO
  
    faltas = 0
    memoria = [[None, 0] for x in range(numQuadros)]
    
    for i in range(len(referencias)):
      
        flag = False
        
        for j in range(numQuadros):
          
            if memoria[j][0] == None:
                memoria[j][0] = referencias[i]
                faltas += 1
                flag = True
                break
            
            if memoria[j][0] == referencias[i]:
                flag = True
                break
        
        if not flag:
            ultimaRef = 0
            refCont = 0
            
            for j in range(numQuadros):
                sera_ref = False

                for k in range(i, len(referencias)):
                    if referencias[k] == memoria[j][0]:
                        sera_ref = True
                        break
                    refCont += 1
                
                if sera_ref:
                    memoria[j][1] = refCont
                else:
                    memoria[j][1] = None

            for j in range(numQuadros):
                if memoria[j][1] == None:
                    ultimaRef = j
                    break
                if memoria[j][1] > memoria[ultimaRef][1]:
                    ultimaRef = j

            memoria[ultimaRef][0] = referencias[i]
            faltas += 1

    print('OTM {}'.format(faltas))

def conjuntoDeTrabalho(referencias, numQuadros): # CONJUNTO DE TRABALHO
  
    faltas = 0
    refCont = 0
    tempoVirtual = 0
    limiar = int(numQuadros/2) + 1
    memoria = [[None, 0, 0] for x in range(numQuadros)]
    
    for i in range(len(referencias)):
      
        tempoVirtual += 1
        flag = False
        
        for j in range(numQuadros):
          
            if memoria[j][0] == None:
                memoria[j][0] = referencias[i]
                memoria[j][1] = 1
                memoria[j][2] = tempoVirtual
                faltas += 1
                flag = True
                break
            
            if memoria[j][0] == referencias[i]:
                memoria[j][1] = 1
                memoria[j][2] = tempoVirtual
                flag = True
                break
        
        if not flag:
            troca = 0
            
            for j in range(numQuadros):
                if memoria[j][1] == 0:
                    idade = tempoVirtual - memoria[j][2]
                    if idade > limiar:
                        troca = j
                        break
                    if idade > (tempoVirtual - memoria[troca][2]):
                        troca = j
                         
            memoria[troca][0] = referencias[i]
            memoria[troca][1] = 1
            memoria[troca][2] = tempoVirtual

            faltas += 1

        refCont += 1
        
        if refCont == 4:
            refCont = 0
            
            for j in range(numQuadros):
                memoria[j][1] = 0

    print('CT {}'.format(faltas))

# CONVERTENDO O ARQUIVO DE ENTRADA
referencias, numQuadros = converte(arquivo)

# CHAMADA DAS FUNÇÕES
segundaChance(copy.deepcopy(referencias), numQuadros)
otimo(copy.deepcopy(referencias), numQuadros)
conjuntoDeTrabalho(copy.deepcopy(referencias), numQuadros)