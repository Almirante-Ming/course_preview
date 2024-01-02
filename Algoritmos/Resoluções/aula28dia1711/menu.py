def menu():
    print("Escolha uma opção...")
    print("1) Criar")
    print("2) Buscar")
    print("3) Editar")
    print("4) Remover")
    print("0) Sair")


if __name__ == "__main__":
    while True:
        menu()
        user_input = int(input())
        if user_input == 0:
            break
        else:
            print("Opção ainda não implementada!")