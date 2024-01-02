def upper_case_substring(s, i, j):
    """torna maiúsculas as letras entre os índices i e j da string s"""
    before = s[:i]
    uppercase = s[i:j].upper()
    after = s[j:]
    return before + uppercase + after

if __name__ == "__main__":
    frase = "cada minuto que passa é outra chance de mudar tudo"
    print(upper_case_substring(frase, 30, 36))

    # erro! nenhum argumento bate com os parâmetros!
    print(upper_case_substring(True, frase))
