
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

mode = input('Для атаки полным перебором введите "а", для шифрования/дешифрования с заданным смещением ввведите "с": ').lower()


if mode == 'с':

    shift = int(input('Введите смещение (максимум 33): '))
    output = ''
    

    type = input('Для шифрования введите "ш", для дешифрования введите "д" :').lower()

    if type == 'ш':
        message = input('Введите сообщение для шифровки: ').lower()
        for i in message:
            if i in alphabet:
                number_in_alphabet = alphabet.find(i)   #находим индекс буквы в алфавите 
                number_in_alphabet_with_shift = number_in_alphabet + shift  #узнаем индекс в смещенном алфавите
            
                output += alphabet[number_in_alphabet_with_shift]   #записываем в шифрованную строку
            else:
                output += i
        print('Зашифрованное сообщение: ', output)

    if type == 'д':
        message = input('Введите сообщение для дешифровки: ').lower()
        for i in message:
            if i in alphabet:
                number_in_alphabet = alphabet.find(i)   #находим номер буквы в алфавите 
                number_in_alphabet_with_shift = number_in_alphabet - shift  #узнаем номер в смещенном алфавите
            
                output += alphabet[number_in_alphabet_with_shift]
            else:
                output += i
        print('Дешифрованное сообщение: ', output)

if mode == 'а':
    type = input('Для шифрования введите "ш", для дешифрования введите "д" :').lower()

    if type == 'ш':
        message = input('Введите сообщение для шифровки: ').lower()
        for i in range (1, 34):
            output = ''
            for j in message:
                
                if j in alphabet:
                    number_in_alphabet = alphabet.find(j)   #находим индекс буквы в алфавите 
                    number_in_alphabet_with_shift = number_in_alphabet + i  #узнаем индекс в смещенном алфавите
                
                    output += alphabet[number_in_alphabet_with_shift]   #записываем в шифрованную строку
                else:
                    output += j
            print('Смещение: ', i,' Зашифрованное сообщение: ', output)

    if type == 'д':
        message = input('Введите сообщение для дешифровки: ').lower()
        for i in range (1, 34):
            output = ''
            for j in message:
                
                if j in alphabet:
                    number_in_alphabet = alphabet.find(i)   #находим номер буквы в алфавите 
                    number_in_alphabet_with_shift = number_in_alphabet - i  #узнаем номер в смещенном алфавите
                
                    output += alphabet[number_in_alphabet_with_shift]
                else:
                    output += j
            print('Смещение: ', i,' Дешифрованное сообщение: ', output)


