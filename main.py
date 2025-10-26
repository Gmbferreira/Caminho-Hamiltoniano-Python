from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list)
    def add_edge(self, u, v, directed=False):
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    def _hamiltonian_path_util(self, v, visited, path):
        visited[v] = True
        path.append(v)
        if len(path) == self.V:
            return True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self._hamiltonian_path_util(neighbor, visited, path):
                    return True
        path.pop()
        visited[v] = False
        return False

    def find_hamiltonian_path(self):
        for start_vertex in range(self.V):
            path = []
            visited = [False] * self.V
            if self._hamiltonian_path_util(start_vertex, visited, path):
                print(f"Caminho Hamiltoniano encontrado (iniciando em {start_vertex}):")
                print(" -> ".join(map(str, path)))
                return path

        print("Nenhum Caminho Hamiltoniano foi encontrado.")
        return None
if __name__ == "__main__":
    print("--- Exemplo 1: Grafo Não Orientado (com caminho) ---")
    g1 = Graph(5)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(3, 4)
    g1.add_edge(1, 3) 
    g1.add_edge(1, 4) 
    g1.find_hamiltonian_path()

    print("\n--- Exemplo 2: Grafo 'Completo' K4 (com caminho) ---")
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(0, 3)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)
    g2.find_hamiltonian_path()

    print("\n--- Exemplo 3: Grafo Desconexo (sem caminho) ---")
    g3 = Graph(5)
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(3, 4) 
    g3.find_hamiltonian_path()
    
    print("\n--- Exemplo 4: Grafo Orientado (com caminho) ---")
    g4 = Graph(4)
    g4.add_edge(0, 1, directed=True)
    g4.add_edge(1, 2, directed=True)
    g4.add_edge(2, 3, directed=True)
    g4.add_edge(1, 3, directed=True) 
    g4.find_hamiltonian_path()

    print("\n--- Exemplo 5: Grafo Orientado (sem caminho) ---")
    g5 = Graph(4)
    g5.add_edge(0, 1, directed=True)
    g5.add_edge(1, 2, directed=True)
    g5.add_edge(3, 2, directed=True) 
    g5.add_edge(0, 3, directed=True)
    g5.find_hamiltonian_path()