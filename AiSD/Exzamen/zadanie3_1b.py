from collections import deque

def isolate_vertex(graph, vertex):
    
    for v in graph:
        if v != vertex:
            graph[v].pop(vertex, None)
    graph[vertex] = {}

def isolate_connected_vertices(graph, vertex1, vertex2):
   
    for v in graph:
        if v != vertex1 and v != vertex2:
            graph[v].pop(vertex1, None)
            graph[v].pop(vertex2, None)
        else:
            if v == vertex1 and vertex1 in graph[v]:
                graph[v] = {vertex2: graph[v][vertex1]}
            elif v == vertex2 and vertex2 in graph[v]:
                graph[v] = {vertex1: graph[v][vertex2]}

def bfs(graph, start):
    
    visited = set()
    components = []
    
    def bfs_helper(vertex):
        component = []
        queue = deque([vertex])
        while queue:
            v = queue.popleft()
            if v not in visited:
                visited.add(v)
                component.append(v)
                for neighbor in graph[v]:
                    queue.append(neighbor)
        if component:
            components.append(component)
    
    for vertex in graph:
        if vertex not in visited:
            bfs_helper(vertex)
    
    return components

# Граф
graph = {
    1: {2: 2, 3: 1, 4: 3},
    2: {4: 4, 3: 3},
    3: {4: 1, 5: 4, 6: 4},
    4: {},
    5: {6: 3},
    6: {4: 5}
}

isolate_vertex(graph, 6)
isolate_connected_vertices(graph, 3, 5)
components = bfs(graph, 1)
# Вывод результатов
print("Вершины, входящие в компоненты:")
for i, component in enumerate(components):
    print(f"Компонента {i+1}: {list(component)}")
# Проверяем связность графа между всеми компонентами
if len(components) == 1:
    print("Граф является связным между всеми компонентами.")
else:
    print("Граф несвязный и состоит из нескольких компонент связности.")