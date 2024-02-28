def generate_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        return key * (len(string) // len(key)) + key[:len(string) % len(key)]

def vigenere_cipher(string, key, mode='encrypt'):
    result = []
    key_index = 0
    for char in string:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - ord('A')
            if mode == 'encrypt':
                result.append(chr((ord(char.upper()) + shift - ord('A')) % 26 + ord('A')))
            elif mode == 'decrypt':
                result.append(chr((ord(char.upper()) - shift - ord('A')) % 26 + ord('A')))
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)
    return ''.join(result)

def main():
    string = "Why are we here? Just to suffer?"
    key = "Ilikecyber"
    filtered_string = ''.join(filter(str.isalpha, string))
    key = generate_key(filtered_string, key)
    ciphered = vigenere_cipher(string, key)
    deciphered = vigenere_cipher(ciphered, key, mode='decrypt')
    print(f"Encrypted Text: {ciphered}\nDecrypted Text: {deciphered}")

    user_string = input("Enter a string to encrypt: ")
    user_key = input("Enter a key in order to encrypt and decrypt: ")
    filtered_user_string = ''.join(filter(str.isalpha, user_string))
    user_key = generate_key(filtered_user_string, user_key)
    ciphered_user = vigenere_cipher(user_string, user_key)
    deciphered_user = vigenere_cipher(ciphered_user, user_key, mode='decrypt')
    print(f"Here is your encrypted text: {ciphered_user}\nHere is your decrypted text: {deciphered_user}")

if __name__ == "__main__":
    main()
