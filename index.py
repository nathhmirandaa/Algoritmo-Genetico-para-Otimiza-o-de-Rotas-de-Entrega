import random
import math
random.seed(10)

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
#Facilitar na hora de rodar outro banco de dados
cliente_atual = clientes_30

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
    #print(clientes)
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
    elif tempo_entrega > tempo_tolerancia: 
        if(tempo_tolerancia == 0):
           atraso_percentual = tempo_entrega # Atraso
        else:
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


def inicializarPopulacao(tamanho_populacao, clientes):
    populacao = []
    ordem_entrega = []
    for _ in range(tamanho_populacao):
        
        ordem_entrega = list(cliente_atual.keys())
       
        for i in range(0, random.randint(1,10) ):
            ordem_entrega.append(0 )
        
        random.shuffle(ordem_entrega)
        populacao.append([ordem_entrega, 0])

    return populacao

def getFitness(individuo, clientes):
    fitness = 0

    for i in range(len(individuo) - 1):
        cliente_atual = individuo[i]
        proximo_cliente = individuo[i + 1]

        # Corrigindo a chamada da função calcularTempoEntrega() para passar apenas dois argumentos
        tempo_entrega = calcularTempoEntrega(proximo_cliente, clientes)
        fitness += getSatisfacao(cliente_atual, proximo_cliente, tempo_entrega, clientes)

    return fitness


def cruzamento(pai1, pai2):
    ponto_corte1 = random.randint(1, len(pai1) - 1)
    ponto_corte2 = random.randint(1, len(pai2) - 1)

    filho1 = pai1[:ponto_corte1] + pai2[ponto_corte1:]
    filho2 = pai2[:ponto_corte2] + pai1[ponto_corte2:]

    return filho1, filho2

def mutacao(individuo):
    # Trocando aleatoriamente duas posições no indivíduo
    posicao1 = random.randint(0, len(individuo) - 1)
    posicao2 = random.randint(0, len(individuo) - 1)
    individuo[posicao1], individuo[posicao2] = individuo[posicao2], individuo[posicao1]
    return individuo


def main(populacao, clientes):
    individuos = []
    novos = []
    
    # Avaliar a população e armazenar os indivíduos e seus fitness
    for p in populacao:
        f = getFitness(p[0], clientes)  # O fitness é o segundo elemento da lista p
        individuos.append((p[0], f))

    # Ordenar os indivíduos com base no fitness
    individuos_ordenados = sorted(individuos, key=lambda x: x[1], reverse=True)
    
    # Print em ordem decrescente
    for individuo, fitness in individuos_ordenados:
        print("Indivíduo:", individuo, "Fitness:", fitness)
    
    # Selecionar os dois indivíduos com os maiores fitness
    pai1 = individuos_ordenados[0][0]
    pai2 = individuos_ordenados[1][0]
    
    print("Pais selecionados:", pai1, pai2)

    # Realizar cruzamento e adicionar os quatro filhos à lista de novos
    for _ in range(2):
        filho1, filho2 = cruzamento(pai1, pai2)
        novos.append((filho1, 0))  # O fitness inicial é definido como 0, pode ser recalculado posteriormente
        novos.append((filho2, 0)) 

        # Print dos filhos gerados
        print("Filho gerado:", filho1)
        print("Filho gerado:", filho2)

    # Adicionar os quatro filhos gerados à lista 'novos'
    filho3, filho4 = cruzamento(pai1, pai2)
    novos.append((filho3, 0))
    novos.append((filho4, 0))

    # Imprimir a lista 'novos' após adicionar os filhos
    print("Lista 'novos' com filhos adicionados:", novos)

    # Aplicar a mutação com 30% de probabilidade para cada indivíduo em 'novos'
    for i in range(len(novos)):
        if random.random() < 0.3:  # Probabilidade de 30%
            novos[i] = (mutacao(novos[i][0]), 0)

    # Imprimir a lista 'novos' após adicionar os filhos e aplicar a mutação
    print("Lista 'novos' com filhos e mutação:", novos)
    
# Exemplo de uso
tamanho_populacao = 5
populacao_inicial = inicializarPopulacao(tamanho_populacao, cliente_atual)
main(populacao_inicial, cliente_atual)

    
    #selecionar os melhores (2 ou 4) -> novos (feito - escolhendo 2 pais)
    #cruzamento -> novos  (feito) 
    #criar mais -> novos cruzando 2 pais resulta em 4 filhos
    #mutacao de novos
    #criterios atendidos 
        #sim - exibem
        #nao - main(novo, clientes)
    


 #populacao = inicializarPopulacao(10, clientes_30) 
 
 
#for c in list(clientes_30.values()):
 #   print(c['posicao'])

