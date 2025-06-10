def convert_to_binary(number):
    try:
        decimal_values = [ord(char) for char in number]
        binary_number = ''.join([bin(value)[2:].zfill(8) for value in decimal_values])

        return binary_number
    except TypeError:
        return "Ошибка! Введены некорректные данные."
number = input("Введите число: ")
binary_number = convert_to_binary(number)
print("Двоичная запись числа:", binary_number)