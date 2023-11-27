alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '

# alphabet = 'abcdefghijklmnopqrstuvwxyz '

letter_to_index = dict(zip(alphabet, range(len(alphabet)))) #связываем алфавит с индексом в словарь(a-0, б - 1 .... я-32)
index_to_letter = dict(zip(range(len(alphabet)), alphabet)) #тоже само, но наоборот

def encrypt(message, key):
    """ разделить сообщение на длину ключа
        переобразавать сообщение из букв в индексы и добавить ключ (mod 33)
    """
    #зашифрованное сообщение
    encrypted = ''
    
    #делим сообщение на куски размером с ключ(старат, конец, шаг)
    split_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]
    
    #для каждого кусочка в разделенном сообщении выполняем
    for each_split in split_message:
        #следим на каком мы символе в ключе
        i = 0
        #для каждой буквы в кусочке выполняем
        for letter in each_split:
            #конвертируем букву из сообщения в индекс, довавляем индекс буквы ключа и делим на длину алфавита 
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            #конвертируем индекс в букву, довавляем букву к шифру
            encrypted += index_to_letter[number]
            #переходим к следующей букве в ключе
            i+=1
            
    return encrypted

def decrypt(cipher, key):
    """ разделить шифр на длину ключа
        переобразавать шифр из букв в индексы и отнять ключ (mod 33)
    """
    #дешифрованное сообщение
    decrypted = ''
    
    #делим шифр на куски размером с ключ(старат, конец, шаг)
    split_cipher = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))]
    
    #для каждого кусочка в разделенном щифре выполняем
    for each_split in split_cipher:
        #следим на каком мы символе в ключе
        i = 0
         #для каждой буквы в кусочке выполняем
        for letter in each_split:
            #конвертируем букву из шифра в индекс, вычитаем индекс буквы ключа и делим на длину алфавита 
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            #конвертируем индекс в букву, довавляем букву к шифру
            decrypted += index_to_letter[number]
            #переходим к следующей букве в ключе
            i+=1
            
    return decrypted
            

def main():
    message = input('Введите сообщение для шифровки: ').lower()
    key = input('Введите ключ: ').lower()
    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)
    
    print('Оригинальное сообщение: ', message)
    print('Зашифрованное сообщение: ', encrypted_message)
    print('Дешифрованное сообщение: ', decrypted_message)
    

main()