nomes = []
senhas = []
cont = 0
for i in range (5):
    nomes.append(input(f"Informe o nome do usuário {i}: "))
    senhas.append(input(f"Informe a senha do usuário {i}: "))
login = input("Informe o login: ")
senha_login = input("Informe a senha: ")
for j in range(5):
    if login == nomes[j] and senha_login == senhas[j]:
        print(f"Usuário: {nomes[j]}, login efetuado com sucesso!")
        break
    else:
        cont += 1
if cont == 5:
    print("Login incorreto!")
