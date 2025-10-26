# Projeto: Caminho Habiltoniano em Python

## Descrição do Projeto

Este projeto implementa um algoritmo em Python para resolver o problema do Caminho Hamiltoniano em grafos orientados ou não orientados. Um Caminho Hamiltoniano é um caminho em um grafo que visita cada vértice exatamente uma vez.

Este é um problema NP-Completo, o que significa que não existe um algoritmo conhecido que o resolva eficientemente (em tempo polinomial) para todos os casos. A abordagem implementada utiliza **backtracking** (retrocesso), que explora sistematicamente todos os caminhos possíveis no grafo até encontrar um que satisfaça a condição.

### Lógica do Algoritmo (Análise do `main.py`)

O algoritmo é centrado em uma classe `Graph` que usa uma lista de adjacência para armazenar o grafo. A lógica principal de busca é dividida em duas funções:

1.  **`find_hamiltonian_path(self)`**: Esta é a função "ponto de entrada". Como não sabemos qual vértice inicia o caminho, esta função itera por todos os vértices (`for start_vertex in range(self.V)`) e tenta iniciar a busca a partir de cada um deles. Ela inicializa um array `visited` (para rastrear os nós já visitados) e um array `path` (para construir o caminho) para cada tentativa.

2.  **`_hamiltonian_path_util(self, v, visited, path)`**: Esta é a função recursiva de backtracking principal.

    - **`LINHA 1: visited[v] = True; path.append(v)`**

      - **Lógica:** Ao entrar na função, seleciona-se o vértice `v`. Nós o marcamos como visitado e o adicionamos ao caminho que estamos construindo.

    - **`LINHA 2: if len(path) == self.V:`**

      - **Lógica:** Esta é a **condição de base (sucesso)** da recursão. Se o número de vértices no nosso caminho for igual ao número total de vértices no grafo, significa que visitamos todos os vértices exatamente uma vez. Encontramos o caminho e retornamos `True`.

    - **`LINHA 3: for neighbor in self.graph[v]:`**

      - **Lógica:** O algoritmo explora suas opções. Ele itera sobre todos os vizinhos do vértice `v` (os nós diretamente conectados a ele).

    - **`LINHA 4: if not visited[neighbor]:`**

      - **Lógica:** Verificamos se o vizinho já está no nosso caminho. Se `visited[neighbor]` for `False`, significa que é um vértice válido para explorar.

    - **`LINHA 5: if self._hamiltonian_path_util(neighbor, visited, path): return True`**

      - **Lógica:** Esta é a **chamada recursiva**. O algoritmo tenta avançar para o vizinho. Se essa chamada recursiva (e todas as suas sub-chamadas) eventualmente retornar `True`, significa que a partir desse vizinho foi possível encontrar um caminho completo. Propagamos o `True` de volta pela pilha de recursão.

    - **`LINHA 6: path.pop(); visited[v] = False; return False`**
      - **Lógica:** Este é o **passo de backtracking (retrocesso)** e a **condição de base (falha)**. Se o loop `for` terminar (ou seja, exploramos todos os vizinhos de `v`) e nenhum deles levou a uma solução (nenhuma chamada recursiva retornou `True`), significa que a escolha de `v` _neste ponto do caminho_ foi um beco sem saída.
      - O algoritmo "desfaz" sua escolha: remove `v` do caminho (`path.pop()`) e o marca como não visitado (`visited[v] = False`). Isso permite que `v` seja visitado novamente como parte de um _outro_ caminho (por exemplo, A -> B -> C falhou, mas A -> C -> B pode funcionar).
      - Ele então retorna `False`, sinalizando para a chamada anterior que este ramo da busca falhou.

## Como Executar o Projeto

1.  **Pré-requisitos:**

    - Python
    - Um compilador de código como visual studio code(Com uma extenção apra python, como Pylance)

2.  **Clone o repositório da url:**

    - https://github.com/Gmbferreira/Caminho-Hamiltoniano-Python.git

3.  **Execute o arquivo main.py:**

    - Rode o código

4.  **Saída Esperada:**
    - O script executará os 5 exemplos de grafos definidos no bloco `if __name__ == "__main__":` e imprimirá no console se um Caminho Hamiltoniano foi encontrado para cada um, mostrando o caminho se ele existir.

## Relatório Técnico

### Análise da Complexidade Computacional

#### 1. Classes P, NP, NP-Completo e NP-Difícil

- **P (Polinomial):** Classe de problemas de decisão que podem ser resolvidos em tempo polinomial por uma Máquina de Turing determinística. Exemplo: ordenação de uma lista.
- **NP (Não-determinístico Polinomial):** Classe de problemas de decisão onde uma solução candidata pode ser verificada em tempo polinomial.
  - O Problema do Caminho Hamiltoniano (PCH) está em NP. Se alguém lhe fornecer um caminho (uma sequência de $V$ vértices), você pode verificar em tempo polinomial se todos os vértices estão presentes exatamente uma vez e se cada aresta no caminho existe no grafo.
- **NP-Completo (NPC):** Classe de problemas que estão em NP e são NP-Difíceis. São os problemas "mais difíceis" em NP.
  - O PCH **é NP-Completo**. Foi provado que qualquer problema em NP pode ser reduzido ao PCH em tempo polinomial.
- **NP-Difícil (NP-Hard):** Classe de problemas que são "pelo menos tão difíceis quanto" os problemas NP-Completos. Um problema NP-Difícil não precisa estar em NP.
  - O PCH **é NP-Difícil** (pois todo problema NPC é, por definição, NP-Difícil).

#### 2. Justificativa e Relação com o Problema do Caixeiro Viajante (TSP)

O Problema do Caixeiro Viajante (TSP) pergunta: "dado um grafo com pesos, qual é o ciclo hamiltoniano de menor custo?". O problema de decisão do TSP é NP-Completo.

A relação é direta: O Problema do Ciclo Hamiltoniano (um caminho hamiltoniano que começa e termina no mesmo vértice) é um caso especial do TSP, onde todas as arestas têm peso 1 e perguntamos se existe um ciclo de custo $V$ (ou $V+1$, dependendo da contagem).

O Problema do **Caminho** Hamiltoniano (PCH) pode ser reduzido ao Problema do Ciclo Hamiltoniano. Basta criar um novo grafo $G'$ a partir do grafo original $G$, adicionar um novo nó "universal" $X$ e conectar $X$ a todos os $V$ nós de $G$. Um Ciclo Hamiltoniano em $G'$ corresponde a um Caminho Hamiltoniano em $G$.

Como o PCH, o Ciclo Hamiltoniano e o TSP estão todos interligados e são NP-Completos (em suas formas de decisão), eles representam a mesma classe de "problemas intratáveis".

### Análise da Complexidade Assintótica de Tempo

#### 1. Complexidade Temporal do Algoritmo

A complexidade de tempo do algoritmo de backtracking implementado é **$O(V \times V!)$** (Fatorial de $V$) no pior caso.

#### 2. Determinação da Complexidade (Método: Análise da Árvore de Recursão)

1.  **Loop Externo:** A função `find_hamiltonian_path` possui um loop que tenta iniciar a busca a partir de cada um dos $V$ vértices. Isso multiplica o custo total por $V$.
2.  **Árvore de Recursão (Backtracking):** A função `_hamiltonian_path_util` gera uma árvore de busca.
    - No primeiro nível da recursão (após o loop externo), o algoritmo pode ter que escolher entre (no máximo) $V-1$ vizinhos.
    - No segundo nível, ele terá que escolher entre $V-2$ vizinhos.
    - No terceiro, $V-3$, e assim por diante.
3.  **Número de Caminhos:** O número máximo de caminhos explorados (folhas na árvore de recursão) é o número de permutações de vértices, que é $V!$ (V Fatorial).
4.  **Custo por Caminho:** Para cada nó na árvore de recursão, o algoritmo itera sobre seus vizinhos. Em um grafo denso (completo), isso pode levar tempo $O(V)$.

Portanto, o número total de operações é proporcional a $V$ (do loop inicial) multiplicado pelo custo de explorar a árvore de busca, que é $V!$. Isso resulta em uma complexidade de pior caso de $O(V \times V!)$.

_Nota: Algoritmos mais otimizados usando programação dinâmica (como Held-Karp, para o TSP) alcançam $O(V^2 \times 2^V)$, que ainda é exponencial, mas significativamente mais rápido que $O(V!)$._

### Aplicação do Teorema Mestre

**Não é possível aplicar o Teorema Mestre** neste algoritmo.

**Justificativa:** O Teorema Mestre é uma ferramenta para analisar a complexidade de algoritmos de **divisão e conquista**. Ele se aplica a relações de recorrência da forma:

$T(n) = aT(n/b) + f(n)$

Onde:

- $T(n)$ é o tempo para um problema de tamanho $n$.
- $a$ é o número de subproblemas.
- $n/b$ é o tamanho de cada subproblema (o problema é _dividido_).
- $f(n)$ é o custo de dividir o problema e combinar as soluções.

A relação de recorrência do nosso algoritmo de backtracking não segue este formato. A recorrência se parece mais com:

$T(n) = (n-1) \times T(n-1) + O(n-1)$

Onde $n$ é o número de vértices restantes a visitar. O problema é reduzido em tamanho (de $n$ para $n-1$), mas é multiplicado por $(n-1)$ subproblemas, não por uma constante $a$. O Teorema Mestre não se aplica a recorrências onde o número de subproblemas ($a$) ou o fator de divisão ($b$) dependem de $n$.

### Análise dos Casos de Complexidade

#### 1. Pior Caso

- **O que é:** Ocorre quando o algoritmo é forçado a explorar a maior parte (ou a totalidade) da árvore de busca $V!$.
- **Exemplo:** Um **grafo completo** (K*n), onde todos os vértices se conectam a todos os outros. O algoritmo tentará todas as $V!$ permutações de vértices. Outro exemplo é um grafo que \_quase* tem um caminho, mas falha no último vértice, forçando o backtracking a retroceder por toda a árvore.
- **Complexidade:** $O(V \times V!)$
- **Impacto:** O desempenho é extremamente lento. O algoritmo se torna computacionalmente inviável para grafos com mais do que um número muito pequeno de vértices (ex: $V > 20$).

#### 2. Melhor Caso

- **O que é:** Ocorre quando o algoritmo encontra o caminho hamiltoniano na primeira tentativa, sem precisar fazer backtracking.
- **Exemplo:** Um grafo que é uma simples "linha" (ex: 0-1-2-3-4) e o algoritmo, por sorte, escolhe o vértice `0` como `start_vertex`. A recursão seguirá 0 -> 1 -> 2 -> 3 -> 4. Em cada passo, o primeiro vizinho explorado é o correto.
- **Complexidade:** $O(V)$
- **Impacto:** O algoritmo é extremamente rápido, linear ao número de vértices. Ele simplesmente percorre o caminho.

#### 3. Caso Médio

- **O que é:** O desempenho esperado para um grafo "médio" ou aleatório.
- **Análise:** A análise do caso médio para PCH é complexa. No entanto, o desempenho ainda é considerado **exponencial**. A vantagem do backtracking é que, em grafos esparsos ou estruturados, muitos ramos da árvore de busca são "podados" rapidamente (um nó pode não ter vizinhos não visitados, causando um retrocesso imediato).
- **Impacto:** Embora seja geralmente mais rápido que o pior caso (pois $V!$ não é totalmente explorado), a complexidade ainda é intratável e cresce exponencialmente com $V$. O desempenho depende muito da densidade (número de arestas) e da estrutura do grafo.
