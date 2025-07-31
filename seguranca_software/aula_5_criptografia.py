
ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
TAMANHO_ALFABETO = len(ALFABETO)
CHAVE_FIXA = 3

def criptografar(texto_claro, chave):
    texto_cifrado = ""
    texto_claro = texto_claro.lower()
    for char in texto_claro:
        if char in ALFABETO:
            posicao_original = ALFABETO.find(char)
            nova_posicao = (posicao_original + chave) % TAMANHO_ALFABETO
            texto_cifrado += ALFABETO[nova_posicao]
        else:
            texto_cifrado += char
    return texto_cifrado

def descriptografar(texto_cifrado, chave):
    texto_claro = ""
    texto_cifrado = texto_cifrado.lower()

    for char in texto_cifrado:
        if char in ALFABETO:
            posicao_cifrada = ALFABETO.find(char)
            posicao_original = (posicao_cifrada - chave + TAMANHO_ALFABETO) % TAMANHO_ALFABETO
            texto_claro += ALFABETO[posicao_original]
        else:
            texto_claro += char
    return texto_claro

def descriptografar_forca_bruta(texto_cifrado):
    possiveis_textos = []
    for chave_tentativa in range(TAMANHO_ALFABETO):
        texto_descriptografado = descriptografar(texto_cifrado, chave_tentativa)
        possiveis_textos.append((chave_tentativa, texto_descriptografado))
    return possiveis_textos

def main():
    while True:
        print("\n--- Cifra de Substituição ---")
        print("Escolha uma opção:")
        print("1. Criptografar texto")
        print("2. Descriptografar texto")
        print("3. Descriptografar texto (tentar todas as chaves) - Opcional")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            texto = input("Digite o texto claro: ")
            chave_str = input(f"Digite a chave (número de 0 a {TAMANHO_ALFABETO - 1}, deixe em branco para usar a chave fixa {CHAVE_FIXA}): ")
            if chave_str.strip() == "":
                chave = CHAVE_FIXA
                print(f"Usando chave fixa: {chave}")
            else:
                try:
                    chave = int(chave_str)
                    if not (0 <= chave < TAMANHO_ALFABETO):
                        print(f"Chave inválida. Usando chave fixa: {CHAVE_FIXA}")
                        chave = CHAVE_FIXA
                except ValueError:
                    print(f"Entrada de chave inválida. Usando chave fixa: {CHAVE_FIXA}")
                    chave = CHAVE_FIXA

            texto_cifrado_resultado = criptografar(texto, chave)
            print(f"Texto Cifrado: {texto_cifrado_resultado}")

        elif escolha == '2':
            texto_cif = input("Digite o texto cifrado: ")
            try:
                chave = int(input(f"Digite a chave (número de 0 a {TAMANHO_ALFABETO - 1}): "))
                if not (0 <= chave < TAMANHO_ALFABETO):
                    print("Chave inválida. A chave deve ser um número entre 0 e 25.")
                    continue
            except ValueError:
                print("Entrada de chave inválida. Por favor, insira um número.")
                continue

            texto_claro_resultado = descriptografar(texto_cif, chave)
            print(f"Texto Descriptografado: {texto_claro_resultado}")

        elif escolha == '3':
            texto_cif_bruto = input("Digite o texto cifrado: ")
            print("\n--- Tentativas de Descriptografia (Força Bruta) ---")
            resultados_brutos = descriptografar_forca_bruta(texto_cif_bruto)
            for chave_tentativa, texto_possivel in resultados_brutos:
                print(f"Chave {chave_tentativa:02d}: {texto_possivel}")

        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()