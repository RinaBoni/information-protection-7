# alphabet = 'А, О, И, У, Н, Т, К, _'
# input = 'У_АНТОНА_ОКУНИ'

# def egcd(a, b): 
#   x,y, u,v = 0,1, 1,0
#   while a != 0: 
#     q, r = b//a, b%a 
#     m, n = x-u*q, y-v*q 
#     b,a, x,y, u,v = a,r, u,v, m,n 
#   gcd = b 
#   return gcd, x, y 

# def modinv(a, m): 
#   gcd, x, y = egcd(a, m) 
#   if gcd != 1: 
#     return None # modular inverse does not exist 
#   else: 
#     return x % m 
 
# def encrypt(text, key): 
#   #E = (a*x + b) % 26 
#   return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ]) 


# def decrypt(cipher, key): 
#   #D(E) = (a^-1 * (E - b)) % 26
#   return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 

# # Driver Code to test the above functions 
# def main(): 
#   text = 'VAMSI KRISHNA'
#   key = [7, 20] 

#   # calling encryption function 
#   enc_text = encrypt(text, key)
#   print('Input: {}'.format(text))

  
#   print('Encrypted Text: {}'.format(enc_text)) 

#   # calling decryption function 
#   print('Decrypted Text: {}'.format(decrypt(enc_text, key) )) 


# if __name__ == '__main__': 
#   main() 


# Функция для нахождения НОД(a, N)
def find_gcd(a, N):
    while N != 0:
        a, N = N, a % N
    return a

# Функция для нахождения мультипликативной инверсии a по модулю N
def mod_inverse(a, N):
    for x in range(1, N):
        if (a * x) % N == 1:
            return x
    return None  # Инверсия не существует

# Функция для шифрования текста
def encrypt(text, a, b):
    

    # Проверка, что НОД(a, N) = 1
    if find_gcd(a, N) != 1:
        return "Неверные параметры шифрования. НОД(a, N) должен быть равен 1."

    encrypted_text = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            encrypted_index = (a * char_index + b) % N
            encrypted_text += alphabet[encrypted_index]
        else:
            encrypted_text += char

    return encrypted_text

alphabet = "АОИУНТК_"
N = len(alphabet)

# Функция для дешифрования текста
def decrypt(ciphertext, a, b):
    

    # Проверка, что НОД(a, N) = 1
    if find_gcd(a, N) != 1:
        return "Неверные параметры дешифрования. НОД(a, N) должен быть равен 1."

    mod_inv_a = mod_inverse(a, N)
    if mod_inv_a is None:
        return "Инверсия для 'a' не существует."

    decrypted_text = ""
    for char in ciphertext:
        if char in alphabet:
            char_index = alphabet.index(char)
            decrypted_index = (mod_inv_a * (char_index - b)) % N
            decrypted_text += alphabet[decrypted_index]
        else:
            decrypted_text += char

    return decrypted_text

# Получение параметров a и b от пользователя
a = int(input("Введите значение 'a' (целое число): "))
b = int(input("Введите значение 'b' (целое число): "))

text = "У_АНТОНА_ОКУНИ"  # Текст для шифрования

print('Строка-оригинал:', text)

encrypted_text = encrypt(text, a, b)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = decrypt(encrypted_text, a, b)
print("Расшифрованный текст:", decrypted_text)
