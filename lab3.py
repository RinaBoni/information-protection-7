import random

def binary_representation(character):
    '''функция принимает символ в качестве входного параметра и 
    возвращает его двоичное представление, дополненное нулями до 16 бит'''
    code = ord(character)  # получаем числовое представление символа
    binary_code = bin(code)[2:]  # преобразуем в двоичное представление и убираем префикс '0b'
    padded_code = binary_code.zfill(16)  # добавляем лидирующие нули до 16 разрядов
    return padded_code

def convert_string_to_binary(string):
    '''функция принимает строку в качестве входного параметра и 
    возвращает строку, содержащую двоичные представления 
    всех символов из входной строки'''
    binary_string = ""
    for char in string:
        binary_string += binary_representation(char)
    return binary_string




def random_permutation(decimal_list):
    for _ in range(64):  # выполняем 64 случайные перестановки
        i, j = random.sample(range(len(decimal_list)), 2)  # выбираем два случайных индекса
        decimal_list[i], decimal_list[j] = decimal_list[j], decimal_list[i]  # меняем местами элементы
    return decimal_list

# Подпрограмма для создания n случайных перестановок списка
def generate_unique_permutations(decimal_list, n):
    permutations = set()  # Используем множество для хранения уникальных перестановок
    permutations.add(tuple(decimal_list))  # Добавляем исходную перестановку

    while len(permutations) < n:
        shuffled = random_permutation(decimal_list.copy())  # Получаем случайную перестановку
        i = 0
        if shuffled == decimal_list:
            i+=1
            shuffled = random_permutation(decimal_list.copy())  # Получаем случайную перестановку
        permutations.add(tuple(shuffled))  # Добавляем в множество перестановок
        # print(shuffled)
        print (i)

    return [list(perm) for perm in permutations]  # Преобразуем обратно в список списков

def p_block(permutations_list, binary_list, n):
    for index, perm in enumerate(permutations_list, 1):
        if index == n:
            permutations = perm
    buf_binary_list = []
    for i in range(len(binary_list)):
        buf_binary_list.append(binary_list[permutations[i]])
    return buf_binary_list

# Пример использования
initial_list = list(range(10))  # Исходный список от 0 до 9
n_permutations = 10  # Количество случайных перестановок
print(initial_list)

random_permutations = generate_unique_permutations(initial_list, n_permutations)
for index, perm in enumerate(random_permutations, 1):
    print(f"Перестановка {index}: {perm}")


# Пример использования:
input_list = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(p_block(random_permutations, input_list, 3))

# Пример использования:
char = 'Д'
binary = binary_representation(char)
print('Д')
print(binary)
print('0000010000010110')

# Пример использования:
input_string = "ЖПД"
binary_result = convert_string_to_binary(input_string)
print('ЖПД')
print(binary_result)
print('000001000001011000000100000111110000010000010100')


# Пример использования
initial_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Исходный список:", initial_list)

# Вызов функции для случайной перестановки
shuffled_list = random_permutation(initial_list.copy())

print("Список после случайной перестановки:", shuffled_list)