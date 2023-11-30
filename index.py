import math

# Função para calcular a distância euclidiana entre dois pontos
def getDistancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Função para calcular a distância entre dois clientes usando os índices
def getDistanciaEntreClientes(cliente1, cliente2, clientes):
    x1, y1 = clientes[cliente1]['posicao']
    x2, y2 = clientes[cliente2]['posicao']
    return getDistancia(x1, y1, x2, y2)

# Função para calcular o tempo de entrega entre a sede e um cliente
def calcularTempoEntrega(cliente, clientes):
    distancia_sede_cliente = getDistanciaEntreClientes(0, cliente, clientes)
    # Simulação do tempo de entrega considerando 1 unidade de distância = 1 minuto de tempo de entrega
    return distancia_sede_cliente

# Função para calcular a satisfação do cliente com base no tempo de entrega
def getSatisfacao(cliente, tempo_entrega, clientes):
    tempo_tolerancia = getDistanciaEntreClientes(0, cliente, clientes) * 1.5

    if tempo_entrega == tempo_tolerancia:
        return 8
    elif tempo_entrega < tempo_tolerancia / 2:
        return 10
    elif tempo_tolerancia >= tempo_entrega >= tempo_tolerancia / 2:
        return 8
    else:
        atraso_percentual = (tempo_entrega - tempo_tolerancia) / tempo_tolerancia

        if atraso_percentual <= 0.05:
            return 7
        elif atraso_percentual <= 0.1:
            return 6
        elif atraso_percentual <= 0.2:
            return 5
        elif atraso_percentual <= 0.3:
            return 4
        elif atraso_percentual <= 0.4:
            return 3
        else:
            return 2



# Base de dados dos clientes
clientes_5 = {
    0: {'posicao': [0, 0]},  # Sede da empresa
    1: {'posicao': [1, 13], 'pedido': 4},
    2: {'posicao': [30, 4], 'pedido': 1},
    3: {'posicao': [10, 0], 'pedido': 3},
    4: {'posicao': [15, 20], 'pedido': 2},
    5: {'posicao': [5, 7], 'pedido': 5}
}

# Base de dados dos clientes (10 clientes)
clientes_10 = {
    0: {'posicao': [0, 0]},  # Sede da empresa
    1: {'posicao': [1, 13], 'pedido': 4},
    2: {'posicao': [30, 4], 'pedido': 1},
    3: {'posicao': [10, 0], 'pedido': 3},
    4: {'posicao': [15, 20], 'pedido': 2},
    5: {'posicao': [5, 7], 'pedido': 5},
    6: {'posicao': [25, 15], 'pedido': 2},
    7: {'posicao': [8, 3], 'pedido': 3},
    8: {'posicao': [20, 10], 'pedido': 1},
    9: {'posicao': [18, 18], 'pedido': 4},
    10: {'posicao': [2, 25], 'pedido': 3},
}

# Base de dados dos clientes (30 clientes)
clientes_30 = {
    0: {'posicao': [0, 0]},  # Sede da empresa
    1: {'posicao': [1, 13], 'pedido': 4},
    2: {'posicao': [30, 4], 'pedido': 1},
    3: {'posicao': [10, 0], 'pedido': 3},
    4: {'posicao': [15, 20], 'pedido': 2},
    5: {'posicao': [5, 7], 'pedido': 5},
    6: {'posicao': [25, 15], 'pedido': 2},
    7: {'posicao': [8, 3], 'pedido': 3},
    8: {'posicao': [20, 10], 'pedido': 1},
    9: {'posicao': [18, 18], 'pedido': 4},
    10: {'posicao': [2, 25], 'pedido': 3},
    11: {'posicao': [12, 5], 'pedido': 1},
    12: {'posicao': [6, 18], 'pedido': 5},
    13: {'posicao': [17, 22], 'pedido': 3},
    14: {'posicao': [29, 8], 'pedido': 2},
    15: {'posicao': [9, 11], 'pedido': 4},
    16: {'posicao': [19, 19], 'pedido': 2},
    17: {'posicao': [22, 7], 'pedido': 3},
    18: {'posicao': [4, 28], 'pedido': 1},
    20: {'posicao': [27, 25], 'pedido': 3},
    21: {'posicao': [3, 9], 'pedido': 4},
    23: {'posicao': [16, 21], 'pedido': 1},
    25: {'posicao': [26, 2], 'pedido': 4},
    27: {'posicao': [21, 17], 'pedido': 3},
    28: {'posicao': [13, 24], 'pedido': 1},
    29: {'posicao': [25, 15], 'pedido': 2},
    30: {'posicao': [8, 3], 'pedido': 3}
}

# Função para calcular a satisfação de todos os clientes
def getSatisfacaoTodosClientes(clientes):
    satisfacao_clientes = {}
    for cliente in clientes:
        if cliente > 0:  # Ignorar a sede da empresa
            tempo_entrega = calcularTempoEntrega(cliente, clientes)
            satisfacao = getSatisfacao(cliente, tempo_entrega, clientes)
            satisfacao_clientes[cliente] = satisfacao
    return satisfacao_clientes

# Calculando a satisfação de todos os clientes
satisfacao_todos_clientes = getSatisfacaoTodosClientes(clientes_30)

# Exibindo a satisfação de todos os clientes
for cliente, satisfacao in satisfacao_todos_clientes.items():
    print(f"Satisfação do cliente {cliente}: {satisfacao}")
