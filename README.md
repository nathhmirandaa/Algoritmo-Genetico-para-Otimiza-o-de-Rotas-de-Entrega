# 🚚 Algoritmo Genético para Otimização de Entregas

Projeto desenvolvido no **IFBA** como estudo de **algoritmos genéticos aplicados à logística**.  
O objetivo é simular rotas de entrega de uma empresa, considerando **distâncias, tempos, capacidade de carga** e **satisfação dos clientes**, buscando a melhor solução por meio de heurísticas evolutivas.

---

## 📌 Funcionalidades
- Criação de diferentes bases de clientes (5, 10 e 30 pontos de entrega);
- Cálculo da **distância euclidiana** entre clientes e sede;
- Estimativa do **tempo de entrega**;
- Medição da **satisfação do cliente** com base em atrasos e prazos;
- Uso de **algoritmo genético**:
  - Geração inicial de populações;
  - Avaliação com função de *fitness*;
  - Operadores de cruzamento e mutação;
  - Critérios de parada;
- Consideração de **restrições de capacidade do veículo**.

---

## 🛠️ Tecnologias utilizadas
- [Python 3](https://www.python.org/)
- Bibliotecas padrão:
  - `random`
  - `math`

---

## 📂 Estrutura do código
- **Base de dados**: clientes (posição e pedido);
- **Funções auxiliares**:
  - `getDistancia` → calcula a distância entre dois pontos;
  - `calcularTempoEntrega` → estima o tempo entre sede e cliente;
  - `getSatisfacao` → mede satisfação de acordo com prazo;
- **Algoritmo Genético**:
  - `inicializarPopulacao` → gera indivíduos iniciais;
  - `getFitness` → avalia qualidade da solução;
  - `cruzamento` e `mutacao` → operadores genéticos;
  - `main` → executa o processo evolutivo.



Desenvolvido por Isadora Marques e Nathalia Miranda
