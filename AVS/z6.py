def multiply_numbers(number1, number2, base):
    try:
        decimal_number1 = int(number1, base)
        decimal_number2 = int(number2, base)
        decimal_product = decimal_number1 * decimal_number2
        result = format(decimal_product, "x" if base == 16 else "o")

        return result
    except ValueError:
        return "Ошибка! Введены некорректные данные."


def divide_numbers(number1, number2, base):
    try:

        decimal_number1 = int(number1, base)
        decimal_number2 = int(number2, base)
        decimal_quotient = decimal_number1 // decimal_number2
        result = format(decimal_quotient, "x" if base == 16 else "o")

        return result
    except ValueError:
        return "Ошибка! Введены некорректные данные."
    except ZeroDivisionError:
        return "Ошибка! Деление на ноль."


number1 = input("Введите первое число: ")
number2 = input("Введите второе число: ")
base = 14
product_result = multiply_numbers(number1, number2, base)
print("Произведение чисел:", product_result)

quotient_result = divide_numbers(number1, number2, base)
print("Частное чисел:", quotient_result)
