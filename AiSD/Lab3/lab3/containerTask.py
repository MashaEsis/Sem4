import itertools

def FindMax(masses, costs, maxMass):
    n = len(masses)
    maxValue = 0    

    for r in range(1, n + 1):
        for combination in itertools.combinations(range(n), r):
            totalMass = sum(masses[i] for i in combination)
            totalCost = sum(costs[i] for i in combination)

        if totalMass < maxMass and totalCost > maxValue:
            maxValue = totalCost

    return [maxMass, maxValue]

mass = [12, 16, 15]
value = [400, 500, 600]
maxMass = 326

result = FindMax(mass, value, maxMass)
print(f"Максимальная ценность лежажих в рюкзаке предметах с массами {mass} и ценами {value}:\nМаксимальная масса {result[0]}\nМаксимальная стоимость {result[1]}")