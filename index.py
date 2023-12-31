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
}

# Base de dados dos clientes (10 clientes)
clientes_10 = {
    0: {'posicao': [0, 0]},  # Sede da empresa
    1: {'posicao': [1, 13], 'pedido': 4},
    2: {'posicao': [30, 4], 'pedido': 1},
    3: {'posicao': [10, 0], 'pedido': 3},
    4: {'posicao': [15, 20], 'pedido': 2},
    5: {'posicao': [5, 7], 'pedido': 1},
    6: {'posicao': [25, 15], 'pedido': 2},
    7: {'posicao': [8, 3], 'pedido': 3},
    8: {'posicao': [20, 10], 'pedido': 1},
    9: {'posicao': [18, 18], 'pedido': 4},
}

clientes_30 = {
    0: {'posicao': [0, 0]},  # Sede da empresa
    1: {'posicao': [1, 13], 'pedido': 4},
    2: {'posicao': [30, 4], 'pedido': 1},
    3: {'posicao': [10, 0], 'pedido': 3},
    4: {'posicao': [15, 20], 'pedido': 2},
    5: {'posicao': [5, 7], 'pedido': 4},
    6: {'posicao': [25, 15], 'pedido': 2},
    7: {'posicao': [8, 3], 'pedido': 3},
    8: {'posicao': [20, 10], 'pedido': 1},
    9: {'posicao': [18, 18], 'pedido': 4},
    10: {'posicao': [2, 25], 'pedido': 3},
    11: {'posicao': [12, 5], 'pedido': 1},
    12: {'posicao': [6, 18], 'pedido':4},
    13: {'posicao': [17, 22], 'pedido': 3},
    14: {'posicao': [29, 8], 'pedido': 2},
    15: {'posicao': [9, 11], 'pedido': 4},
    16: {'posicao': [19, 19], 'pedido': 2},
    17: {'posicao': [22, 7], 'pedido': 3},
    18: {'posicao': [4, 28], 'pedido': 1},
    19: {'posicao': [8, 3], 'pedido': 3},
    20: {'posicao': [27, 25], 'pedido': 3},
    21: {'posicao': [3, 9], 'pedido': 1},
    22: {'posicao': [8, 10], 'pedido': 4},
    23: {'posicao': [16, 21], 'pedido': 1},
    24: {'posicao': [20, 20], 'pedido': 1},
    25: {'posicao': [26, 2], 'pedido': 4},
    26: {'posicao': [2, 6], 'pedido': 1},
    27: {'posicao': [21, 17], 'pedido': 3},
    28: {'posicao': [13, 24], 'pedido': 1},
    29: {'posicao': [25, 15], 'pedido': 2},
}

#Facilitar na hora de rodar outro banco de dados
cliente_atual = clientes_5

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
    clientes_ids = list(clientes.keys())  # Lista de IDs de clientes

    for _ in range(tamanho_populacao):
        ordem_entrega = clientes_ids[:] # Ignorar a sede na ordem de entrega
       
        # Adicionando voltas a sede
        for _ in range( random.randint(1, len(clientes) )):
            ordem_entrega.insert(0, 0) 
            
        random.shuffle(ordem_entrega)  # Embaralha a ordem de entrega dos clientes
        
        ordem_entrega.insert(0, 0)  # Insere a sede como primeiro elemento
        populacao.append([ordem_entrega[:], 0])  # Adiciona uma cópia da lista como um indivíduo

    return populacao

def getFitness(individuo, clientes):
    fitness = 0
    capacidade = 0  
    clientes_visitados = set()

    for i in range(len(individuo) - 1):
        cliente_atual = individuo[i]
        proximo_cliente = individuo[i + 1]

        # Penalizar se qualquer cliente (exceto a sede) aparecer mais de uma vez
        if cliente_atual != 0 and cliente_atual in clientes_visitados:
            fitness -= 10  # Penalidade por cliente repetido #MUDEI

        clientes_visitados.add(cliente_atual)

        if(cliente_atual == 0) & (proximo_cliente == 0):
            fitness -= 10  # Penalidade por dois pontos de entrega consecutivos sendo a sede

        tempo_entrega = calcularTempoEntrega(proximo_cliente, clientes)
        if(cliente_atual != 0):
            fitness += getSatisfacao(cliente_atual, proximo_cliente, tempo_entrega, clientes)

        if cliente_atual == 0:  # Verifique se o cliente atual é a sede
            capacidade = 4  # Atribua 4 à capacidade
        else:
            # Verifique se a capacidade é suficiente para o cliente atual
            if capacidade >= clientes[cliente_atual]['pedido']:
                capacidade -= clientes[cliente_atual]['pedido']  # Atualize a capacidade
            else:
                fitness -= 10  # Aplique uma punição no fitness se a capacidade não for suficiente

    # Penalize por clientes que não foram visitados
    clientes_nao_visitados = set(clientes.keys()) - clientes_visitados
    fitness -= len(clientes_nao_visitados) * 100  # Penalidade fixa para cada cliente não visitado

    return fitness


def cruzamento(pai1, pai2):
    ponto_corte1 = random.randint(1, len(pai1) - 1)
    ponto_corte2 = random.randint(1, len(pai2) - 1)
    filho1 = pai1[:ponto_corte1] + pai2[ponto_corte1:]
    filho2 = pai2[:ponto_corte2] + pai1[ponto_corte2:]

    return filho1, filho2

def mutacao(individuo):
   
    posicao1 = random.randint(0, len(individuo) - 1)
    posicao2 = random.randint(0, len(individuo) - 1)
    
    individuo[posicao1], individuo[posicao2] = individuo[posicao2], individuo[posicao1]
    return individuo

def criterio_parada(populacao, geracao_atual, max_geracoes=10, fitness_minimo=1000):
    melhores_fitness = [getFitness(individuo[0], cliente_atual) for individuo in populacao]
    
    if max(melhores_fitness) >= fitness_minimo or geracao_atual >= max_geracoes:
        return True
    else:
        return False

def main(populacao, clientes):
    individuos = []
    novos = []
    geracao = 0
    ngeracoes = 5000
    #ADICIONEI
    ind = 0
    while geracao < ngeracoes:  # Critério de parada: x gerações
        # Avaliar a população e armazenar os indivíduos e seus fitness
        
        for p in populacao:
            f = getFitness(p[0], clientes)  # O fitness é o segundo elemento da lista p
            individuos.append([p[0], f])

        # Ordenar os indivíduos com base no fitness
        individuos_ordenados = sorted(individuos, key=lambda x: x[1], reverse=True)

        #novos.append(individuos_ordenados[0])
        #novos.append(individuos_ordenados[1]) 
        
        # Selecionar os dois indivíduos com os maiores fitness
        pai1 = individuos_ordenados[0][0]
        pai2 = individuos_ordenados[1][0]
        print("Melhor fitness: ", individuos_ordenados[0][1], "/ Geração: ", geracao)
        #ind += 2
        # Realizar cruzamento e adicionar os quatro filhos à lista de novos
        #MUDEI - nao precisa do for
        filho1, filho2 = cruzamento(pai1, pai2)
        fitness_filho1 = getFitness(filho1, clientes)
        fitness_filho2 = getFitness(filho2, clientes)
        novos.append([filho1, fitness_filho1])
        novos.append([filho2, fitness_filho2]) 
        #ADICIONEI
        ind += 2
        # Adicionar os quatro filhos gerados à lista 'novos'
        filho3, filho4 = cruzamento(pai1, pai2)
        fitness_filho3 = getFitness(filho3, clientes)
        fitness_filho4 = getFitness(filho4, clientes)
        novos.append([filho3, fitness_filho3])
        novos.append([filho4, fitness_filho4])
        #ADICIONEI
        ind += 2
        #controlando. tamanho da populacao #MUDEI
        gerados = inicializarPopulacao(tamanho_populacao - ind, clientes)
        for g in gerados:
            f = getFitness(g[0], clientes)  # O fitness é o segundo elemento da lista p
            novos.append([g[0], f])

        # Aplicar a mutação com 50% de probabilidade para cada indivíduo em 'novos'
        for i in range(len(novos)):
            if random.random() < 0.5:  # Probabilidade de 50%
                novos[i] = (mutacao(novos[i][0]), 0)

        # Atualizar a população com os novos indivíduos
        populacao = novos
        novos = []  # Limpar a lista de novos para a próxima geração
        geracao += 1
    
    # Imprimir quando o critério de x gerações for atingido
    if geracao==ngeracoes:
        melhor_individuo, melhor_fitness = individuos_ordenados[0]
        print(f"Melhor indivíduo da geração {geracao} Fitness: {melhor_fitness}")
        print("Indivíduo:", melhor_individuo)
        print("Critério de parada atingido.",ngeracoes ,"gerações completas.")
    
# Exemplo de uso
#MUDEI
tamanho_populacao = 50
populacao_inicial = inicializarPopulacao(tamanho_populacao, cliente_atual)
main(populacao_inicial, cliente_atual)