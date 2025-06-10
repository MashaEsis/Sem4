class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.graph = []  # Граф в виде списка ребер

    # Функция для добавления ребра в граф
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Нахождение компонент связности для каждой вершины
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Объединение двух компонент связности в одну
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Алгоритм Борувки для нахождения минимального остовного дерева
    def boruvka(self):
        parent = []
        rank = []
        cheapest = []

        # Инициализация массивов
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            cheapest = [-1] * self.V

        num_trees = self.V
        while num_trees > 1:
            for i in range(len(self.graph)):
                u, v, w = self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                if set1 != set2:
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]
                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]

            for node in range(self.V):
                if cheapest[node] != -1:
                    u, v, w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        self.union(parent, rank, set1, set2)
                        print(f"Ребро {u} -- {v} с весом {w}")
                        num_trees -= 1

            cheapest = [-1] * self.V


# Пример использования
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.boruvka()
