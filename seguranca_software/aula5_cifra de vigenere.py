def vigenere_cipher(text, key, decrypt=False):
    text = text.upper()
    key = key.upper()
    key_length = len(key)
    result = []
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if decrypt:
                shift = -shift
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

text = input("Digite o texto: ")
key = input("Digite a chave: ")
option = input("Escolha 'C' para cifrar ou 'D' para decifrar: ").upper()

if option == 'C':
    encrypted_text = vigenere_cipher(text, key)
    print(f"Texto cifrado: {encrypted_text}")
elif option == 'D':
    decrypted_text = vigenere_cipher(text, key, decrypt=True)
    print(f"Texto decifrado: {decrypted_text}")
else:
    print("Opção inválida.")
