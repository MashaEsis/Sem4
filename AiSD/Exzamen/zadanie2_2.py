from heapq import heappop, heappush, heapify

def prim(graph):
    start_node = list(graph.keys())[0]  # произвольная вершина
    visited = set([start_node])  # Множество посещенных вершин
    minimum_spanning_tree = {}  # Остовное дерево
    edges = [
        (cost, start_node, next_node)
        for next_node, cost in graph[start_node].items()
    ]# вес, 1 вершина, 2 вершина , дерём из графа 
    heapify(edges)  # Куча на основе списка ребер

    while edges:
        cost, start, next_node = heappop(edges)#наименьшей стоимости ребро
        if next_node not in visited:    
            visited.add(next_node)
            minimum_spanning_tree.setdefault(start, {})#создаёт первую отметку
            minimum_spanning_tree[start][next_node] = cost

            for neighbor, neighbor_cost in graph[next_node].items():# рассматриваем соседа
                if neighbor not in visited:
                    heappush(edges, (neighbor_cost, next_node, neighbor))

    return minimum_spanning_tree

def dijkstra_minimum_spanning_tree(graph, start_node):
    minimum_spanning_tree = {}  # Остовное дерево
    distances = {node: float('inf') for node in graph}  # Расстояния от начальной вершины
    distances[start_node] = 0
    heap = [(0, start_node, None)]  # Куча с приоритетом: вес, текущая , предыдущая 

    while heap:
        current_distance, current_node, previous_node = heappop(heap)# наименьшее расстояние

        if current_distance > distances[current_node]:# если рассмотрели, вон
            continue

        if previous_node is not None:
            minimum_spanning_tree.setdefault(previous_node, {})
            minimum_spanning_tree[previous_node][current_node] = current_distance

        for neighbor, neighbor_distance in graph[current_node].items():
            distance = neighbor_distance

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(heap, (distance, neighbor, current_node))

    return minimum_spanning_tree
graph = {
    1: {2: 2, 3: 1, 4: 3},
    2: {4: 4, 3: 3},
    3: {4: 1, 5: 4, 6: 4},
    4: {},
    5: {6: 3},
    6: {4: 5}
}

# Прима
minimum_spanning_tree_prim = prim(graph)
print("Остовное дерево (алгоритм Прима):")
print(minimum_spanning_tree_prim)
# Дейкстры
start_node = 1  # Начальная вершина 
minimum_spanning_tree_dijkstra = dijkstra_minimum_spanning_tree(graph, start_node)
print("Минимальное остовное дерево (алгоритм Дейкстры):")
print(minimum_spanning_tree_dijkstra)