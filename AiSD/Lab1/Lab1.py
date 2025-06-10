from random import randint
import matplotlib.pyplot as plt
import time

def triple_sum(vector, A, B):
    triple_sum = 0
    for num in vector:
        if A <= num <= B:
            triple_sum += num * 3
    return triple_sum

def generate(size):
    return list(randint(-100, 100) for i in range(size))

N = [100, 1000, 10000, 100000]
A = -50
B = 50

durations = [] 

for n in N:
    vector = generate(n)
    start_time = time.perf_counter_ns()
    sum = triple_sum(vector, A, B)
    end_time = time.perf_counter_ns()
    duration = end_time - start_time
    durations.append(duration)
    print(f"Размер вектора: {n}, Длительность: {duration:.12f} секунд , Сумма: {sum}")
    sum = 0

plt.plot(N, durations)
plt.xlabel("Размер вектора")
plt.ylabel("Длительность (секунды)")
plt.title("Изменение времени выполнения в зависимости от размера вектора")
plt.show()
