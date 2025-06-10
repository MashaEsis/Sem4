import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}  # Расстояния до всех вершин
    distances[start] = 0  # Расстояние до стартовой вершины равно 0
    path = {start: []}  # Пути до каждой вершины

    queue = [(0, start)]  # Очередь для выбора текущей вершины
    # выполняется пока очередь не пустая \/ наименьший элемент
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        # Если текущее расстояние до текущей вершины больше уже известного расстояния, пропускаем её
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Если найденное расстояние до соседней вершины меньше известного расстояния, обновляем его
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = path[current_vertex] + [current_vertex]
                heapq.heappush(queue, (distance, neighbor))

    return distances, path
graph = {
    1: {2: 2, 3: 1, 4: 3},
    2: {4: 4, 3: 3},
    3: {4: 1, 5: 4, 6: 4},
    4: {},
    5: {6: 3},
    6: {4: 5}
}

start_vertex = 1
distances, paths = dijkstra(graph, start_vertex)# словарь - хранит пути ко всем вершинам 
print("Пути и расстояния от вершины", start_vertex)
for vertex, distance in distances.items():
    path = paths[vertex] + [vertex]
    print("Вершина:", vertex)
    print("Расстояние:", distance)
    print("Путь:", " -> ".join(map(str, path)))
    print()