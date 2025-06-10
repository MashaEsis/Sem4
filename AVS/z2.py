def convert_number(decimal_number, base):
    new_number = ""
    while decimal_number > 0:
        remainder = decimal_number % base
        if remainder < 10:
            new_number = str(remainder) + new_number
        else:
            new_number = chr(ord('A') + remainder - 10) + new_number
        decimal_number = decimal_number // base
    return new_number

decimal_number = int(input("Введите десятичное число: "))
student_number = int(input("Введите порядковый номер студента: "))
base = student_number + 3
new_number = convert_number(decimal_number, base)
ascii_number = ""
for digit in new_number:
    ascii_number += chr(ord('A') + int(digit))
print("Число в новой системе счисления:", ascii_number)