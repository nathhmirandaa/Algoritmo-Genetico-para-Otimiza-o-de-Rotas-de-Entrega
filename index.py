import math

# Calcula a distância euclidiana entre dois pontos:
def getDistancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Exemplo de uso:
dist = getDistancia(1, 13, 30, 4)
print(dist)

def getDistanciaPorIndice(cliente1, cliente2, arr):
    x1, y1 = arr[cliente1]
    x2, y2 = arr[cliente2]
    return getDistancia(x1, y1, x2, y2)

# Exemplo de uso: 
arr = [[10, 0], [1, 13], [30, 4]]
distancia = getDistanciaPorIndice(1, 2, arr)
print(distancia)

def getSatisfacao(pos_cliente, tempo_entrega):
    tempo_tolerancia = (getDistanciaPorIndice(0, pos_cliente, arr)) * 1.5

    if tempo_entrega == tempo_tolerancia:
        return 6
    elif tempo_entrega < tempo_tolerancia / 2:
        return 10
    elif tempo_tolerancia >= tempo_entrega >= tempo_tolerancia / 2:
        return 8
    else:
        atraso_percentual = (tempo_entrega - tempo_tolerancia) / tempo_tolerancia

        if atraso_percentual <= 0.1:
            return 5
        elif atraso_percentual <= 0.2:
            return 4
        elif atraso_percentual <= 0.4:
            return 3
        elif atraso_percentual <= 0.6:
            return 2
        elif atraso_percentual <= 0.8:
            return 1
        else:
            return 0

# Exemplo de uso:
satisfacao_cliente = getSatisfacao(1, 45)
print(satisfacao_cliente)