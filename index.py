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
    sede = clientes[0]['posicao']  # Posição da sede (índice 0)
    posicao_cliente = clientes[cliente]['posicao']  # Posição do cliente

    # Extrair as coordenadas x, y da sede e do cliente
    x_sede, y_sede = sede
    x_cliente, y_cliente = posicao_cliente

    # Calcular a distância entre a sede e o cliente
    distancia_sede_cliente = getDistancia(x_sede, y_sede, x_cliente, y_cliente)

    # Simulação do tempo de entrega considerando 1 unidade de distância = 1 minuto de tempo de entrega
    return distancia_sede_cliente

# Função para calcular a satisfação do cliente com base no tempo de entrega
def getSatisfacao(cliente1, cliente2, tempo_entrega, clientes):
    tempo_tolerancia = getDistanciaEntreClientes(cliente1, cliente2, clientes) * 1.5    
   
    if tempo_entrega == tempo_tolerancia:
        return 6  # Saída para entrega no tempo de tolerância
    elif tempo_entrega < tempo_tolerancia / 2:
        return 10  # Saída para entrega antes da metade do tempo de tolerância
    elif tempo_entrega > tempo_tolerancia:  # Atraso
        atraso_percentual = (tempo_entrega - tempo_tolerancia) / tempo_tolerancia

        if atraso_percentual <= 0.1:
            return 5  # Saída para 10% ou menos de atraso
        elif atraso_percentual <= 0.2:
            return 4  # Saída para 20% ou menos de atraso
        elif atraso_percentual <= 0.4:
            return 3  # Saída para 40% ou menos de atraso
        elif atraso_percentual <= 0.6:
            return 2  # Saída para 60% ou menos de atraso
        elif atraso_percentual <= 0.8:
            return 1  # Saída para 80% ou menos de atraso
        else:
            return 0  # Saída para mais de 100% de atraso
    else:  # Tempo entre a metade e o tempo de tolerância
        return 8  # Saída para entrega entre a metade e o tempo de tolerância





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
    ordem_clientes = list(clientes.keys())  # Obtendo a ordem dos clientes

    for i in range(len(ordem_clientes) - 1):
        cliente_atual = ordem_clientes[i]
        proximo_cliente = ordem_clientes[i + 1]

        # Corrigindo a chamada da função calcularTempoEntrega() para passar apenas dois argumentos
        tempo_entrega = calcularTempoEntrega(proximo_cliente, clientes)
        satisfacao = getSatisfacao(cliente_atual, proximo_cliente, tempo_entrega, clientes)

        satisfacao_clientes[cliente_atual] = satisfacao

    return satisfacao_clientes

# Chame a função corrigida passando os dados corretos dos clientes
satisfacao_todos_clientes = getSatisfacaoTodosClientes(clientes_30)

# Exibindo a satisfação de todos os clientes
for cliente, satisfacao in satisfacao_todos_clientes.items():
    print(f"Satisfação do cliente {cliente}: {satisfacao}")


# Calculando a satisfação de todos os clientes
satisfacao_todos_clientes = getSatisfacaoTodosClientes(clientes_30)

# Exibindo a satisfação de todos os clientes
for cliente, satisfacao in satisfacao_todos_clientes.items():
    print(f"Satisfação do cliente {cliente}: {satisfacao}")
