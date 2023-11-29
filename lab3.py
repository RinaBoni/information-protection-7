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
    '''Подпрограмма для 64 случайных перестановок'''
    for _ in range(64):  # выполняем 64 случайные перестановки
        i, j = random.sample(range(len(decimal_list)), 2)  # выбираем два случайных индекса
        decimal_list[i], decimal_list[j] = decimal_list[j], decimal_list[i]  # меняем местами элементы
    return decimal_list


def generate_unique_permutations(decimal_list, n):
    '''Подпрограмма для создания n случайных перестановок списка'''
    permutations = set()  # Используем множество для хранения уникальных перестановок
    permutations.add(tuple(decimal_list))  # Добавляем исходную перестановку
    while len(permutations) < n:
        shuffled = random_permutation(decimal_list.copy())  # Получаем случайную перестановку
        permutations.add(tuple(shuffled))  # Добавляем в множество перестановок
    return [list(perm) for perm in permutations]  # Преобразуем обратно в список списков


def generate_permutations(decimal_list, n):
    '''Подпрограмма для создания n случайных перестановок списка'''
    permutations = set()  # Используем множество для хранения уникальных перестановок
    original_tuple = tuple(decimal_list)  # Преобразуем исходный список в кортеж
    while len(permutations) < n:
        shuffled = random_permutation(decimal_list.copy())  # Получаем случайную перестановку
        shuffled_tuple = tuple(shuffled)  # Преобразуем в кортеж
        # Проверяем, что полученная перестановка отличается от исходного списка
        if shuffled_tuple != original_tuple:
            permutations.add(shuffled_tuple)  # Добавляем в множество перестановок
    return [list(perm) for perm in permutations]  # Преобразуем обратно в список списков


def p_block_encrypt(permutations_list, binary_list, n):
    for index, perm in enumerate(permutations_list, 1):
        if index == n:
            permutations = perm
    buf_binary_list = []
    for i in range(len(binary_list)):
        buf_binary_list.append(binary_list[permutations[i]])
    return buf_binary_list


def p_block_decrypt(permutations_list, binary_list, n):
    for index, perm in enumerate(permutations_list, 1):
        if index == n:
            permutations = perm
    buf_binary_list = []
    for i in range(len(binary_list)):
        buf_binary_list.append(binary_list[permutations.index(i)])
    return buf_binary_list


def list_to_str(list):
    '''конвертирует список в строку'''
    return ''.join(str(elem) for elem in list)


def binary_to_decimal(binary_str):
    '''преобразование строки с двоичным числом в десятичное число'''
    decimal_num = int(binary_str, 2)
    return decimal_num


def decimal_to_binary(decimal_num, width):
    '''преобразование десятичного числа в строку двоичного числа заданной разрядности'''
    binary_str = format(int(decimal_num), f'0{width}b')
    return list(binary_str)


def s_block_encrypt(binary_message):
    '''S-блок шифровки'''
    decimal = binary_to_decimal(binary_message)
    if decimal == 0:
        new_decimal = 6
    elif decimal == 1:
        new_decimal = 8
    elif decimal == 2:
        new_decimal = 12
    elif decimal == 3:
        new_decimal = 14
    elif decimal == 4:
        new_decimal = 2
    elif decimal == 5:
        new_decimal = 11
    elif decimal == 6:
        new_decimal = 13
    elif decimal == 7:
        new_decimal = 10
    elif decimal == 8:
        new_decimal = 4
    elif decimal == 9:
        new_decimal = 3
    elif decimal == 10:
        new_decimal = 15
    elif decimal == 11:
        new_decimal = 0
    elif decimal == 12:
        new_decimal = 7
    elif decimal == 13:
        new_decimal = 9
    elif decimal == 14:
        new_decimal = 5
    elif decimal == 15:
        new_decimal = 1
    new_binary = decimal_to_binary(new_decimal, 4)
    return new_binary


def s_block_decrypt(encrypted_binary):
    '''S-блок для расшифровки'''
    decimal = binary_to_decimal(encrypted_binary)
    if decimal == 6:
        new_decimal = 0
    elif decimal == 8:
        new_decimal = 1
    elif decimal == 12:
        new_decimal = 2
    elif decimal == 14:
        new_decimal = 3
    elif decimal == 2:
        new_decimal = 4
    elif decimal == 11:
        new_decimal = 5
    elif decimal == 13:
        new_decimal = 6
    elif decimal == 10:
        new_decimal = 7
    elif decimal == 4:
        new_decimal = 8
    elif decimal == 3:
        new_decimal = 9
    elif decimal == 15:
        new_decimal = 10
    elif decimal == 0:
        new_decimal = 11
    elif decimal == 7:
        new_decimal = 12
    elif decimal == 9:
        new_decimal = 13
    elif decimal == 5:
        new_decimal = 14
    elif decimal == 1:
        new_decimal = 15
    decrypted_binary = decimal_to_binary(new_decimal, 4)
    return decrypted_binary


def battery_s_block_encrypt(input_sequence):
    '''делит 32-битную последовательность на части по 4 бита и зашифровывает каждую с помощью S-блока'''
    encrypted_message=''
    for i in range(0, 32, 4):
        input_part = input_sequence[i:i+4]
        encrypted_message += list_to_str(s_block_encrypt(list_to_str(input_part)))
    return encrypted_message


def battery_s_block_decrypt(input_sequence):
    '''делит 32-битную последовательность на части по 4 бита и расшифровывает каждую с помощью S-блока'''
    decrypted_message=''
    for i in range(0, 32, 4):
        input_part = input_sequence[i:i+4]
        decrypted_message += list_to_str(s_block_decrypt(list_to_str(input_part)))
    return decrypted_message


def binary_to_char(binary_char):
    '''конвертирование 16-битной последовательности в символ'''
    decimal_value = int(binary_char, 2)
    char_value = chr(decimal_value)
    return char_value


def convert_binary_to_string(binary_string):
    '''конвертирование бинарной строки в строку символов'''
    string = ""
    for i in range(0, 32, 16):
        input_part = binary_string[i:i+16]
        string += binary_to_char(input_part)
    return string



print('\n\n\n')



print('========== Шифрование ==========')

input_string = "ЖП"
binary_string = convert_string_to_binary(input_string)
print('Исходное сообщение: ',input_string)
print('Битовая форма исходного сообщения:            ', binary_string)


initial_list = list(range(32))  # Исходный список от 0 до 9
n_permutations = 10  # Количество случайных перестановок

random_permutations = generate_permutations(initial_list, n_permutations)

# for index, perm in enumerate(random_permutations, 1):
#     print(f"Перестановка {index}: {perm}")

p_block_encrypted1 = p_block_encrypt(random_permutations, binary_string, 3)
print('Зашифрованная p-блоком битовая форма:         ', list_to_str(p_block_encrypted1))


s_block_encrypted = battery_s_block_encrypt(p_block_encrypted1)
print('Зашифрованная батареей s-блоков битовая форма:', s_block_encrypted)

p_block_encrypted2 = p_block_encrypt(random_permutations, s_block_encrypted, 3)
print('Зашифрованная p-блоком битовая форма:         ', list_to_str(p_block_encrypted2))

encrypted_string = convert_binary_to_string(list_to_str(p_block_encrypted2))
print('Зашифрованное сообщение:', encrypted_string)


print('\n')
print('========== Расшифрование ==========')

print('Зашифрованное сообщение:', encrypted_string)

p_block_decrypted2 = p_block_decrypt(random_permutations, p_block_encrypted2, 3)
print('Расшифрованная p-блоком битовая форма:         ', list_to_str(p_block_decrypted2))

s_block_decrypted = battery_s_block_decrypt(p_block_decrypted2)
print('Расшифрованная батареей s-блоков битовая форма:', s_block_decrypted)

p_block_decrypted1 = p_block_decrypt(random_permutations, s_block_decrypted, 3)
print('Расшифрованная p-блоком битовая форм:          ', list_to_str(p_block_decrypted1))

decrypted_string = convert_binary_to_string(list_to_str(p_block_decrypted1))
print('Расшифрованное сообщение: ',decrypted_string)

print('\n\n\n')

