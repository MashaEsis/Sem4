import itertools

def find_optimal_route(cities, matrix):
    permutations = list(itertools.permutations(cities))
    optimal_route = None
    optimal_distance = float('inf')
    counter = 0

    # Проходимся по всем перестановкам городов
    for permutation in permutations:
        distance = 0
        # Вычисляем суммарное расстояние для текущей перестановки
        for i in range(len(permutation) - 1):
            from_city = permutation[i]
            to_city = permutation[i + 1]
            distance += matrix[from_city][to_city]

        counter += 1
        print(f"Маршрут[{counter}]: {permutation}, общая дистанция: {distance}")

        # Если текущая перестановка имеет меньшую длину, обновляем оптимальный маршрут
        if distance < optimal_distance:
            optimal_distance = distance
            optimal_route = permutation

    return [optimal_route, optimal_distance]

cities = [0, 1, 2, 3, 4]
matrix = [
    [float('inf'), 16, 17, 18, 19],
    [1, float('inf'), 3, 4, 16],
    [2, 1, float('inf'), 6, 17],
    [1, 2, 1, float('inf'), 18],
    [5, 6, 7, 8, float('inf')]
]

result = find_optimal_route(cities=cities, matrix=matrix)
print(f"Оптимальный маршрут {result[0]} с дистацнией {result[1]}")