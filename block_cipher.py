import random

def binary_representation(character):
    code = ord(character)  # получаем числовое представление символа
    binary_code = bin(code)[2:]  # преобразуем в двоичное представление и убираем префикс '0b'
    padded_code = binary_code.zfill(16)  # добавляем лидирующие нули до 16 разрядов
    return padded_code

def convert_string_to_binary(string):
    binary_string = ""
    for char in string:
        binary_string += binary_representation(char)
    return binary_string




def random_permutation(decimal_list):
    for _ in range(64):  # выполняем 64 случайные перестановки
        i, j = random.sample(range(len(decimal_list)), 2)  # выбираем два случайных индекса
        decimal_list[i], decimal_list[j] = decimal_list[j], decimal_list[i]  # меняем местами элементы
    return decimal_list

# Пример использования:
input_list = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation_result = random_permutation(input_list)
print(permutation_result)
# Пример использования:
char = 'Ж'
binary = binary_representation(char)
print('Ж')
print(binary)
print('0000010000010110')

# Пример использования:
input_string = "ЖП"
binary_result = convert_string_to_binary(input_string)
print('ЖП')
print(binary_result)
print('00000100000101100000010000011111')