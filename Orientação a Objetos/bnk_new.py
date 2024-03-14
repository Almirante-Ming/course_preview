from cad_bnk import Cadastro

print("Bem vindo, pressione 1 para cadastrar, ou 0 para encerrar: ")
cad=int(input())

while cad == 1:
    print("Digite seu login completo: ")
    n1=input()
    
    while len(n1) > 15 or len(n1) < 5:
        if len(n1) > 15:
            print("login muito grande, digite um login com no máximo 15 caracteres: ")
            n1=input()
        elif len(n1) < 5:
            print("login muito curto, digite um login com no mínimo 5 caracteres: ")
        n1=input()
        
    print("agora, digite sua senha: ")
    s1=input()
    
    while len(s1) < 7:    
        print("senha muito curta, digite uma senha com no mínimo 8 caracteres: ")
        s1=input()
            
    p1=Cadastro(login=n1, senha=s1)
    print("seja bem vindo", p1.login)
    
    print("Deseja adicionar outro usuário ? 1 para sim, 0 para não: ")
    n1=int(input())
    if n1 == 0:
        print("Obrigado por utilizar nossos serviços, até a próxima!")
        break
    
else:
    print("Obrigado por utilizar nossos serviços, até a próxima!")   