from collections import deque

def bfs(graph, start):
    visited = set()  # Множество посещенных вершин
    queue = deque([start])  # Очередь для обхода вершин

    while queue:
        vertex = queue.popleft()  # Извлекаем вершину из очереди
        print(vertex)  # Можно заменить на нужные операции над вершиной

        if vertex not in visited:
            visited.add(vertex)  # Помечаем вершину как посещенную
            neighbors = graph[vertex]  # Получаем соседей текущей вершины

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)  # Добавляем соседей в очередь

# Пример графа в виде словаря смежности
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_vertex = 'A'
bfs(graph, start_vertex)