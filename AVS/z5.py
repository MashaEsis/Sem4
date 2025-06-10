def add_numbers(number1, number2, base):
    try:
        decimal_number1 = int(number1, base)
        decimal_number2 = int(number2, base)
        decimal_sum = decimal_number1 + decimal_number2
        result = format(decimal_sum, 'x' if base == 16 else 'o')

        return result
    except ValueError:
        return "Ошибка! Введены некорректные данные."


def subtract_numbers(number1, number2, base):
    try:
        decimal_number1 = int(number1, base)
        decimal_number2 = int(number2, base)
        decimal_difference = decimal_number1 - decimal_number2
        result = format(decimal_difference, 'x' if base == 16 else 'o')

        return result
    except ValueError:
        return "Ошибка! Введены некорректные данные."
number1 = input("Введите первое число: ")
number2 = input("Введите второе число: ")
base = 11 
sum_result = add_numbers(number1, number2, base)
print("Сумма чисел:", sum_result)

difference_result = subtract_numbers(number1, number2, base)
print("Разность чисел:", difference_result)