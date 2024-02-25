import random

def jogar():

    erro_letra = False
    acerto_letra = False

    total_tentativas = 10
    numero_tentativas = 0
    pontos = 1000
    letra_existente = []

    mensagem_abertura()
    palavra_secreta = random_palavra_secreta()

    letras_acertadas = marcador_letra(palavra_secreta)
    print(letras_acertadas)

    while not erro_letra and not acerto_letra:

        # Imprimir a tentativa atual
        print(contador_tentativa(numero_tentativas, total_tentativas))

        chute = entrada_letra()

        # Verificar se o imput contém exatamente um caracterer

        if len(chute) != 1:
            print("Por favor, digite apenas uma letra por vez!")
            continue

        # Verificar se a letra existe na palavra, se a letra digitada é uma tentativa repetida e se é uma letra alfabética
        if chute in palavra_secreta:
            marcador_letra_correta(chute, letras_acertadas, palavra_secreta)
            numero_tentativas += 1
        else:
            if chute in letra_existente:
                print("Você já tentou essa letra. Tente outra!")
                continue

            elif not chute.isalpha():
                print("Por favor, digite apenas letras!")
                continue

            else:
                letra_existente.append(chute)

            numero_tentativas += 1

        pontos = pontos - 10
        erro_letra = numero_tentativas == total_tentativas
        acerto_letra = "_" not in letras_acertadas
        print(letras_acertadas)

    resultado(acerto_letra, palavra_secreta, pontos)

def mensagem_abertura():
    nome_jogo = "Jogo adivinhe a palavra!"
    nome_jogo = nome_jogo.upper()
    print(nome_jogo)

def random_palavra_secreta():
    arquivo = open("br-palavras.txt", "r", encoding="UTF-8")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def marcador_letra(palavra):
    return ["_" for letra in palavra]

def marcador_letra_correta(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index += 1
def entrada_letra():
    letra = input("Digite a letra: ")
    letra = letra.strip().upper()
    return letra

def resultado(acerto_palavra, palavra_secreta, pontos):
    if acerto_palavra:
        print("Você acertou e fez {} pontos!".format(pontos))
    else:
        print("Poxa! Não foi dessa vez!")
        print("A palavra secreta era: {}".format(palavra_secreta))

def contador_tentativa(numero_tentativas, total_tentativas):
    return "Tentativa {} de {}!".format(numero_tentativas + 1, total_tentativas)


if (__name__ == "__main__"):
    jogar()