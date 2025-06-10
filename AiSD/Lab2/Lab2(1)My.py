from datetime import datetime
import random
import time as t
import matplotlib.pyplot as plt

class S:
    def __init__(self, float_data, date, string):
        self.string = string
        self.float_data = float_data
        self.date = date

    def __str__(self):
        return f"float_data: {self.float_data}, date: {self.date}, string: {self.string}"
   
def Generate(N):
    array = []
    for _ in range(N):
        num = random.randint(0, 100)
        year = random.randint(1970, datetime.now().year)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        random_date = datetime(year, month, day, hour, minute, second)
        string = "".join(
            random.choices("abcdefghijklmnopqrstuvwxyz", k=10)
        )  # создание строки из 10 символос допуском пробелов
        s = S(num, random_date, string)
        array.append(s)
    return array

def Sort1(array, key):
    n = len(array)
    swaps = 0
    for i in range(1, n):
        j = i
        while j > 0 and getattr(array[j - 1], key) > getattr(array[j], key):
            array[j], array[j - 1] = array[j - 1], array[j]
            swaps += 1
            j -= 1
    return swaps

def Sort2(array, key1, key2):
    n = len(array)
    swaps = 0
    for i in range(1, n):
        j = i
        while j > 0 and (
            getattr(array[j - 1], key1) > getattr(array[j], key1) or (
                getattr(array[j - 1], key1) == getattr(array[j], key1) and
                getattr(array[j - 1], key2) > getattr(array[j], key2)
            )
        ):
            array[j], array[j - 1] = array[j - 1], array[j]
            swaps += 1
            j -= 1
    return swaps

def Sort3(array, key1, key2, key3):
    n = len(array)
    swaps = 0
    for i in range(1, n):
        j = i
        while j > 0 and (
            getattr(array[j - 1], key1) < getattr(array[j], key1) or (
                getattr(array[j - 1], key1) == getattr(array[j], key1) and (
                    getattr(array[j - 1], key2) < getattr(array[j], key2) or (
                        getattr(array[j - 1], key2) == getattr(array[j], key2) and
                        getattr(array[j - 1], key3) > getattr(array[j], key3)
                    )
                )
            )
        ):
            array[j], array[j - 1] = array[j - 1], array[j]
            swaps += 1
            j -= 1
    return swaps


def InterpolationSearch(array, key, value):
    low = 0
    high = len(array) - 1

    while low <= high and array[low].date <= value <= array[high].date:
        pos = low + int(((high - low) / (array[high].date - array[low].date).total_seconds()) * (value - array[low].date).total_seconds())

        if array[pos].date == value:
            return array[pos]

        if array[pos].date < value:
            low = pos + 1
        else:
            high = pos - 1

    return None

N = [100, 1000, 10000]
times1, times2, times3, swaps1, swaps2, swaps3 = [], [], [], [], [], []
for n in N:
    starttime = t.perf_counter_ns()
    data, count = Generate(n), 0
    copyData1 = data.copy()
    copyData2 = data.copy()
    copyData3 = data.copy()

    swaps1.append(Sort1(copyData1, 'string'))
    times1.append((t.perf_counter_ns() - starttime) * 10 ** (-9))

    swaps2.append(Sort2(copyData2, 'string', 'float_data'))
    times2.append((t.perf_counter_ns() - starttime) * 10 ** (-9))

    swaps3.append(Sort3(copyData3, 'string', 'float_data', 'date'))
    times3.append((t.perf_counter_ns() - starttime) * 10 ** (-9))

    print("Объем: %d" %n)
    print("--------------------------")
    print("Время на сортировку 1: %.10f c\nВремя на сортировку 2: %.10f c\nВремя на сортировку 3: %.10f c\n\n" % (times1[count], times2[count], times3[count]))
    count += 1

search_date = datetime(2023, 5, 10, 12, 30, 0)
result = InterpolationSearch(data, 'date', search_date)

if result is not None:
    print(f"Found: {result}")
else:
    print("Not found")

    
plt.subplot(1, 2, 1)
plt.plot(N, times1, marker='*', label='Сортировка 1')
plt.plot(N, times2, marker='*', label='Сортировка 2')
plt.plot(N, times3, marker='*', label='Сортировка 3')
plt.xlabel('Объем данных')
plt.ylabel('Время (секунды)')
plt.title('Зависимость времени выполнения от объема данных')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(N, swaps1, marker='*', label='Сортировка 1')
plt.plot(N, swaps2, marker='*', label='Сортировка 2')
plt.plot(N, swaps3, marker='*', label='Сортировка 3')
plt.xlabel('Объем данных')
plt.ylabel('Количество обменов')
plt.title('Зависимость количества обменов от объема данных')
plt.legend()

plt.tight_layout()
plt.show()
