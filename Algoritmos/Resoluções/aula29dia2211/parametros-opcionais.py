def construir_nome(primeiro_nome, ultimo_nome, nome_do_meio="", prefixo="", sufixo=""):

    nome_completo = ""

    if prefixo != "":
        nome_completo = prefixo + " "

    nome_completo += primeiro_nome

    if nome_do_meio != "":
        nome_completo += f" {nome_do_meio}"

    nome_completo += f" {ultimo_nome}"

    if sufixo != "":
        nome_completo += f" {sufixo}"

    return nome_completo


print(construir_nome("Maria", "da Silva"))
print(construir_nome("José", "Ferreira", "dos Santos"))
print(construir_nome("Pedro", "de Bragança", sufixo="II", prefixo="Dom"))
