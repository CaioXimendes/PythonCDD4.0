import random

palavra = ["smartphone","computador","impressora"]
palavra_recebida = random.choice(palavra)
vetor_aux2 = []
vetor_aux = ["_","_","_","_","_","_","_","_","_","_"]
# boneco = "cabeça, corpo, braço esq, braço direito, perna esq, perna direita, nesse caso sao 6 condições

print("Bem vindo ao jogo da forca! O tema do jogo é tecnologia!")
cont = 0
while vetor_aux2 != vetor_aux:
    for x in palavra_recebida:
        vetor_aux2.append(x)
    for y in palavra_recebida:
        print(vetor_aux)
        pergunta = input("Informe uma letra: ")
        if pergunta in palavra_recebida:
            print("palavra correta!")
            for n in range (10):
                if pergunta == vetor_aux2[n]:
                    del vetor_aux[n]
                    vetor_aux.insert(n,pergunta)
        else:
            cont+=1
        match cont:
            case 1:
                print("cabeça adicionada ao boneco!")
            case 2:
                print("cabeça, corpo adicionada ao boneco!")
            case 3:
                print("cabeça, corpo, braço esquerdo adicionada ao boneco!")
            case 4:
                print("cabeça, corpo, braço esq e direito adicionada ao boneco!")
            case 5:
                print("cabeça, corpo, braço esq+dir e perna esq adicionada ao boneco!")
            case 6:
                vetor_aux2 = vetor_aux
                print("boneco completado, você perdeu!")
                break