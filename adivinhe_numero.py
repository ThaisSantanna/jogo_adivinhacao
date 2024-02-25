import random

def jogar():
    nome_jogo = ("Jogo advinhe o número!")
    nome_jogo = nome_jogo.upper()
    print(nome_jogo)

    numero_secreto = random.randrange(1, 1001)
    total_tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade:")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Faça sua escolha: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 e 1000: ")
        print("Você Digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 1000):
            print("Você deve digitar um número entre 1 e 1000!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! Seu chute foi maior do que o número secreto!")
            elif (menor):
                print("Você errou! Seu chute foi menor do que o número secreto!")

            pontos = pontos - 10

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()
