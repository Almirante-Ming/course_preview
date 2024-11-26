1. input()
Descrição: Recebe uma entrada do usuário em forma de texto.
Exemplo:
nome = input("Digite seu nome: ")
print("Olá, ", nome)

2. int()
Descrição: Converte um valor (normalmente uma string) para um número inteiro.
Exemplo:

numero = int(input("Digite um número: "))
3. print()
Descrição: Exibe uma mensagem na tela.
Exemplo:
print("Olá, mundo!")
4. set()
Descrição: Cria um conjunto, uma coleção de elementos únicos e desordenados. Remove automaticamente duplicatas.
Exemplo:
palavras = set(["casa", "casa", "azul", "bonita"])  # {'casa', 'azul', 'bonita'}
5. sorted()
Descrição: Retorna uma lista ordenada dos elementos de qualquer iterável.
Exemplo:
numeros = {5, 3, 8, 1}
numeros_ordenados = sorted(numeros)  # [1, 3, 5, 8]

6. split()
Descrição: Divide uma string em uma lista de palavras com base em um separador (espaço, por padrão).
Exemplo:
frase = "A casa é azul"
palavras = frase.split()  # ['A', 'casa', 'é', 'azul']

7. join()
Descrição: Junta os elementos de uma lista em uma única string, separados por um delimitador especificado.
Exemplo:
palavras = ["casa", "é", "azul"]
frase = " ".join(palavras)  # 'casa é azul'

8. lower()
Descrição: Converte uma string para letras minúsculas.
Exemplo:
frase = "Casa Azul"
frase_min = frase.lower()  # 'casa azul'

9. strip()
Descrição: Remove espaços em branco extras no início e no final de uma string.
Exemplo:
texto = "  Olá mundo  "
texto_limpo = texto.strip()  # 'Olá mundo'

10. issubset()
Descrição: Verifica se todos os elementos de um conjunto estão contidos em outro conjunto.
Exemplo:
letras_alfabeto = set("abcdefghijklmnopqrstuvwxyz")
letras_frase = set("the quick brown fox jumps over the lazy dog")
letras_alfabeto.issubset(letras_frase)  # True

11. open()
Descrição: Abre um arquivo e retorna um objeto de arquivo, que permite ler ou escrever no arquivo.
Exemplo:
with open("arquivo.txt", "r") as f:
    conteudo = f.read()
12. read()
Descrição: Lê o conteúdo completo de um arquivo aberto.
Exemplo:

with open("arquivo.txt", "r") as f:
    conteudo = f.read()  # Lê todo o conteúdo do arquivo
13. isalpha()
Descrição: Verifica se todos os caracteres em uma string são letras do alfabeto (sem considerar números e pontuações).
Exemplo:

palavra = "casa"
palavra.isalpha()  # True
14. union()
Descrição: Retorna a união de dois conjuntos, contendo todos os elementos presentes em pelo menos um dos conjuntos.
Exemplo:
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)  # {1, 2, 3, 4, 5}
15. intersection()
Descrição: Retorna a interseção de dois conjuntos, contendo apenas os elementos presentes em ambos os conjuntos.
Exemplo:
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
interseccao = conjunto1.intersection(conjunto2)  # {3}

Módulo string
Descrição: Contém constantes para manipulação de strings, como ascii_lowercase para letras minúsculas (a a z).
Exemplo:
import string
letras = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'