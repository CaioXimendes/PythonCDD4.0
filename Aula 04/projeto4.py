i = 0
pin = "123"
senha = input("Olá! informe a sua senha: \n")
while senha != pin:
    senha = input("Senha incorreta, informe a senha novamente: \n ")
    i += 1
    if i >= 2 and senha!=pin:
        print(" Mais de 3 tentativas, a senha foi bloqueada!")
    else:
        print("Senha correta!")
        break
else:
    print("senha correta!")