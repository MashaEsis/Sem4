def convert_to_decimal(base, number):
    for digit in number:
        if ord(digit) >= ord('A') + base:
            print("Ошибка: цифра {} не соответствует системе счисления!".format(digit))
            return None
    decimal = 0
    power = len(number) - 1
    for digit in number:
        if digit.isdigit():
            decimal += int(digit) * (base ** power)
        else:
            decimal += (ord(digit) - ord('A') + 10) * (base ** power)
        power -= 1
    
    return decimal
base = int(input("Введите основание системы счисления: "))
number = input("Введите число: ")
decimal = convert_to_decimal(base, number)
if decimal is not None:
    print("Десятичное число:", decimal)