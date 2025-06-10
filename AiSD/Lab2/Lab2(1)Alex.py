import random
import string
import time as t
import matplotlib.pyplot as plt

class S:
    def __init__(self):
        self.stringData = ''
        self.floatData = 0.0
        self.intData = 0

    def Print(self):
        print(f"%s %.2f %d" % (self.stringData, self.floatData, self.intData))

def Generate(N):
    result = []
    for _ in range(N):
        item = S()
        item.stringData = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1,50)))
        item.int = random.randint(-100,100)
        item.floatData = random.uniform(-100,100)
        result.append(item)

    return result

def Sort1(array, key):
    n = len(array)
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if getattr(array[j], key) < getattr(array[min_idx], key):
                min_idx = j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            swaps += 1

    #print(swaps)
    return swaps

def Sort2(array, key1, key2):
    n = len(array)
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if getattr(array[j], key1) < getattr(array[min_idx], key1):
                min_idx = j
            elif getattr(array[j], key1) == getattr(array[min_idx], key1):
                if getattr(array[j], key2) > getattr(array[min_idx], key2):
                    min_idx = j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            swaps += 1

    #print(swaps)

    return swaps

def Sort3(array, key1, key2, key3):
    n = len(array)
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if getattr(array[j], key1) > getattr(array[min_idx], key1):
                min_idx = j
            elif getattr(array[j], key1) == getattr(array[min_idx], key1):
                if getattr(array[j], key2) < getattr(array[min_idx], key2):
                    min_idx = j
                elif getattr(array[j], key2) == getattr(array[min_idx], key2):
                    if getattr(array[j], key3) > getattr(array[min_idx], key3):
                        min_idx = j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            swaps += 1
    #print(swaps)

    return swaps

def search(list, key, value):
    for i in range(len(list)):
        if getattr(list[i], key) == value:
            return list[i]
        
    return None

N = [100, 1000, 10000]
times1, times2, times3, swaps1, swaps2,swaps3, = [], [], [], [], [], []
for n in N:
    starttime = t.perf_counter_ns()
    data, count = Generate(n), 0
    copyData1 = data.copy()
    copyData2 = data.copy()
    copyData3 = data.copy()

    swaps1.append(Sort1(copyData1, 'stringData'))
    times1.append((t.perf_counter_ns() - starttime) * 10 ** (-9))

    swaps2.append(Sort2(copyData2, 'stringData', 'floatData'))
    times2.append((t.perf_counter_ns() - starttime) * 10 ** (-9))

    swaps3.append(Sort3(copyData3, 'stringData', 'floatData', 'intData'))
    times3.append((t.perf_counter_ns() - starttime) * 10 ** (-9))

    print("Объем: %d" %n)
    print("--------------------------")
    print("Время на сортировку 1: %.2f c\nВремя на сортировку 2: %.2f c\nВремя на сортировку 1: %f c\n\n" % (times1[count], times2[count], times3[count]))
    count += 1

# Построение графиков
plt.subplot(1,2,1)
plt.plot(N, times1, label="Сортировка по одному полю")
plt.plot(N, times2, label="Сортировка по двум полям")
plt.plot(N, times3, label="Сортировка по трем полям")
plt.xlabel("Размерность набора")
plt.ylabel("Время (сек)")
plt.title("Зависимость времени сортировки от размерности набора")
plt.legend()

plt.subplot(1,2,2)
plt.plot(N, swaps1, label="Сортировка по одному полю")
plt.plot(N, swaps2, label="Сортировка по двум полям")
plt.plot(N, swaps3, label="Сортировка по трем полям")
plt.xlabel("Размерность набора")
plt.ylabel("Количество обменов")
plt.title("Зависимость количества обменов от размерности набора")
plt.legend()
plt.show()
