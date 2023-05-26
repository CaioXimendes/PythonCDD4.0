print("Olá, seja bem vindo ao jogo da velha!")

def imprimir_jg_da_velha():
    print(vetor1)
    print(vetor2)
    print(vetor3)

vetor1 = ["_"] * 3
vetor2 = ["_"] * 3
vetor3 = ["_"] * 3
ganhou = False

jogador_1 = input("Olá jogador1, você quer jogar com X ou O? ")
if jogador_1 in "xX":
    jogador_1 = "X"
    jogador_2 = "O"
    print(f"O jogador2 irá jogar com {jogador_2}")
else:
    jogador_2 = "X"
    print(f"O jogador2 irá jogar com {jogador_2}")
imprimir_jg_da_velha()
#pergunta = int(input("Informe o quadrado de 1 a 9 que você quer jogar: "))
for x in range(9):
    if x % 2 == 0:
        jogador_1_pergunta = int(input("Jogador 1, Informe o quadrado de 1 a 9 que você quer jogar: "))
        match jogador_1_pergunta:
            case 1:
                vetor1[0] = jogador_1
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_1 and vetor1[1] == jogador_1 and vetor1[2] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor2[0] == jogador_1 and vetor2[1] == jogador_1 and vetor2[2] == jogador_1:
                    ganhou = True
                elif vetor3[0] == jogador_1 and vetor3[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
            case 2:
                vetor1[1] = jogador_1
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_1 and vetor1[1] == jogador_1 and vetor1[2] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor2[0] == jogador_1 and vetor2[1] == jogador_1 and vetor2[2] == jogador_1:
                    ganhou = True
                elif vetor3[0] == jogador_1 and vetor3[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
            case 3:
                vetor1[2] = jogador_1
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_1 and vetor1[1] == jogador_1 and vetor1[2] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor2[0] == jogador_1 and vetor2[1] == jogador_1 and vetor2[2] == jogador_1:
                    ganhou = True
                elif vetor3[0] == jogador_1 and vetor3[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
            case 4:
                vetor2[0] = jogador_1
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_1 and vetor1[1] == jogador_1 and vetor1[2] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor2[0] == jogador_1 and vetor2[1] == jogador_1 and vetor2[2] == jogador_1:
                    ganhou = True
                elif vetor3[0] == jogador_1 and vetor3[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
            case 5:
                vetor2[1] = jogador_1
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_1 and vetor1[1] == jogador_1 and vetor1[2] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor2[0] == jogador_1 and vetor2[1] == jogador_1 and vetor2[2] == jogador_1:
                    ganhou = True
                elif vetor3[0] == jogador_1 and vetor3[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
            case 6:
                vetor2[2] = jogador_1
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_1 and vetor1[1] == jogador_1 and vetor1[2] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor2[0] == jogador_1 and vetor2[1] == jogador_1 and vetor2[2] == jogador_1:
                    ganhou = True
                elif vetor3[0] == jogador_1 and vetor3[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
            case 7:
                vetor3[0] = jogador_1
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_1 and vetor1[1] == jogador_1 and vetor1[2] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor2[0] == jogador_1 and vetor2[1] == jogador_1 and vetor2[2] == jogador_1:
                    ganhou = True
                elif vetor3[0] == jogador_1 and vetor3[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
            case 8:
                vetor3[1] = jogador_1
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_1 and vetor1[1] == jogador_1 and vetor1[2] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor2[0] == jogador_1 and vetor2[1] == jogador_1 and vetor2[2] == jogador_1:
                    ganhou = True
                elif vetor3[0] == jogador_1 and vetor3[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
            case 9:
                vetor3[2] = jogador_1
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_1 and vetor1[1] == jogador_1 and vetor1[2] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
                    ganhou = True
                elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
                    ganhou = True
                elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
                elif vetor2[0] == jogador_1 and vetor2[1] == jogador_1 and vetor2[2] == jogador_1:
                    ganhou = True
                elif vetor3[0] == jogador_1 and vetor3[1] == jogador_1 and vetor3[2] == jogador_1:
                    ganhou = True
        if ganhou:
            print("Você ganhou!")
            break
    else:
        jogador_2_pergunta = int(input("Jogador 2, Informe o quadrado de 1 a 9 que você quer jogar: "))
        match jogador_2_pergunta:
            case 1:
                vetor1[0] = jogador_2
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_2 and vetor1[1] == jogador_2 and vetor1[2] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[0] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[1] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[1] == jogador_2 and vetor2[1] == jogador_2 and vetor3[1] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[2] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor2[0] == jogador_2 and vetor2[1] == jogador_2 and vetor2[2] == jogador_2:
                    ganhou = True
                elif vetor3[0] == jogador_2 and vetor3[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
            case 2:
                vetor1[1] = jogador_2
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_2 and vetor1[1] == jogador_2 and vetor1[2] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[0] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[1] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[1] == jogador_2 and vetor2[1] == jogador_2 and vetor3[1] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[2] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor2[0] == jogador_2 and vetor2[1] == jogador_2 and vetor2[2] == jogador_2:
                    ganhou = True
                elif vetor3[0] == jogador_2 and vetor3[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
            case 3:
                vetor1[2] = jogador_2
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_2 and vetor1[1] == jogador_2 and vetor1[2] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[0] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[1] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[1] == jogador_2 and vetor2[1] == jogador_2 and vetor3[1] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[2] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor2[0] == jogador_2 and vetor2[1] == jogador_2 and vetor2[2] == jogador_2:
                    ganhou = True
                elif vetor3[0] == jogador_2 and vetor3[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
            case 4:
                vetor2[0] = jogador_2
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_2 and vetor1[1] == jogador_2 and vetor1[2] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[0] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[1] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[1] == jogador_2 and vetor2[1] == jogador_2 and vetor3[1] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[2] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor2[0] == jogador_2 and vetor2[1] == jogador_2 and vetor2[2] == jogador_2:
                    ganhou = True
                elif vetor3[0] == jogador_2 and vetor3[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
            case 5:
                vetor2[1] = jogador_2
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_2 and vetor1[1] == jogador_2 and vetor1[2] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[0] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[1] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[1] == jogador_2 and vetor2[1] == jogador_2 and vetor3[1] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[2] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor2[0] == jogador_2 and vetor2[1] == jogador_2 and vetor2[2] == jogador_2:
                    ganhou = True
                elif vetor3[0] == jogador_2 and vetor3[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
            case 6:
                vetor2[2] = jogador_2
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_2 and vetor1[1] == jogador_2 and vetor1[2] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[0] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[1] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[1] == jogador_2 and vetor2[1] == jogador_2 and vetor3[1] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[2] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor2[0] == jogador_2 and vetor2[1] == jogador_2 and vetor2[2] == jogador_2:
                    ganhou = True
                elif vetor3[0] == jogador_2 and vetor3[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
            case 7:
                vetor3[0] = jogador_2
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_2 and vetor1[1] == jogador_2 and vetor1[2] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[0] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[1] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[1] == jogador_2 and vetor2[1] == jogador_2 and vetor3[1] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[2] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor2[0] == jogador_2 and vetor2[1] == jogador_2 and vetor2[2] == jogador_2:
                    ganhou = True
                elif vetor3[0] == jogador_2 and vetor3[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
            case 8:
                vetor3[1] = jogador_2
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_2 and vetor1[1] == jogador_2 and vetor1[2] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[0] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[1] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[1] == jogador_2 and vetor2[1] == jogador_2 and vetor3[1] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[2] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor2[0] == jogador_2 and vetor2[1] == jogador_2 and vetor2[2] == jogador_2:
                    ganhou = True
                elif vetor3[0] == jogador_2 and vetor3[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
            case 9:
                vetor3[2] = jogador_2
                imprimir_jg_da_velha()
                if vetor1[0] == jogador_2 and vetor1[1] == jogador_2 and vetor1[2] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[0] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[0] == jogador_2 and vetor2[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[1] == jogador_2 and vetor3[0] == jogador_2:
                    ganhou = True
                elif vetor1[1] == jogador_2 and vetor2[1] == jogador_2 and vetor3[1] == jogador_2:
                    ganhou = True
                elif vetor1[2] == jogador_2 and vetor2[2] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
                elif vetor2[0] == jogador_2 and vetor2[1] == jogador_2 and vetor2[2] == jogador_2:
                    ganhou = True
                elif vetor3[0] == jogador_2 and vetor3[1] == jogador_2 and vetor3[2] == jogador_2:
                    ganhou = True
        if ganhou:
            print("Você ganhou!")
            break
if not ganhou:
    print("Empate!!!")

# if vetor1[0] == jogador_1 and vetor1[1] == jogador_1 and vetor1[2] == jogador_1:
#     print("O jogador 1 venceu a partida!")
#     break
# elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
#     print("O jogador 1 venceu a partida!")
#     break
# elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
#     print("O jogador 1 venceu a partida!")
#     break
# elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
#     print("O jogador 1 venceu a partida!")
#     break
# elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
#     print("O jogador 1 venceu a partida!")
#     break
# elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
#     print("O jogador 1 venceu a partida!")
#     break
# elif vetor2[0] == jogador_1 and vetor2[1] == jogador_1 and vetor2[2] == jogador_1:
#     print("O jogador 1 venceu a partida!")
#     break
# elif vetor3[0] == jogador_1 and vetor3[1] == jogador_1 and vetor3[2] == jogador_1:
#     print("O jogador 1 venceu a partida!")
#     break

# if vetor1[0] == jogador_2 and vetor1[1] == jogador_2 and vetor1[2] == jogador_2:
#     print("O jogador 2 venceu a partida!")
#     break
# elif vetor1[0] == jogador_2 and vetor2[0] == jogador_2 and vetor3[0] == jogador_2:
#     print("O jogador 2 venceu a partida!")
#     break
# elif vetor1[0] == jogador_2 and vetor2[1] == jogador_2 and vetor3[2] == jogador_2:
#     print("O jogador 2 venceu a partida!")
#     break
# elif vetor1[2] == jogador_2 and vetor2[1] == jogador_2 and vetor3[0] == jogador_2:
#     print("O jogador 2 venceu a partida!")
#     break
# elif vetor1[1] == jogador_2 and vetor2[1] == jogador_2 and vetor3[1] == jogador_2:
#     print("O jogador 2 venceu a partida!")
#     break
# elif vetor1[2] == jogador_2 and vetor2[2] == jogador_2 and vetor3[2] == jogador_2:
#     print("O jogador 2 venceu a partida!")
#     break
# elif vetor2[0] == jogador_2 and vetor2[1] == jogador_2 and vetor2[2] == jogador_2:
#     print("O jogador 2 venceu a partida!")
#     break
# elif vetor3[0] == jogador_2 and vetor3[1] == jogador_2 and vetor3[2] == jogador_2:
#     print("O jogador 2 venceu a partida!")
#     break


# if (vetor1.count(jogador_1)) == 3 or (vetor2.count(jogador_1)) == 3 or (vetor3.count(jogador_1)) == 3:
#     print("jogador 1 ganhou!")
#     return ganhou == 1
# elif vetor1[0] == jogador_1 and vetor2[0] == jogador_1 and vetor3[0] == jogador_1:
#     print("Jogador 1 ganhou!")
#     return ganhou == 1
# elif vetor1[1] == jogador_1 and vetor2[1] == jogador_1 and vetor3[1] == jogador_1:
#     print("Jogador 1 ganhou!")
#     return ganhou == 1
# elif vetor1[2] == jogador_1 and vetor2[2] == jogador_1 and vetor3[2] == jogador_1:
#     print("Jogador 1 ganhou!")
#     return ganhou == 1
# elif vetor1[0] == jogador_1 and vetor2[1] == jogador_1 and vetor3[2] == jogador_1:
#     print("Jogador 1 ganhou!")
#     return ganhou == 1
# elif vetor1[2] == jogador_1 and vetor2[1] == jogador_1 and vetor3[0] == jogador_1:
#     print("Jogador 1 ganhou!")
#     return ganhou == 1

