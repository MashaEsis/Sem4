def validate_binary_number(binary_number):
    for digit in binary_number:
        if digit != '0' and digit != '1':
            return False
    return True

def convert_to_hex(binary_number):
    decimal_number = int(binary_number, 2)
    hex_number = hex(decimal_number).upper()[2:]
    return hex_number

binary_number = input("Введите двоичное число: ")
if not validate_binary_number(binary_number):
    print("Ошибка: Введено некорректное двоичное число")
else:
    hex_number = convert_to_hex(binary_number)
    print("Шестнадцатеричное представление:", hex_number)
    print("Двоичное представление:", binary_number)