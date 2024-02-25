import adivinhe_palavra
import adivinhe_numero

def escolher_jogo():
    escolher_jogo = ("Escolha seu jogo:")
    escolher_jogo = escolher_jogo.upper()
    print(escolher_jogo)

    print("(1) Adivinhe a palavra\n(2) Adivinhe o número")

    jogo = int(input("Faça sua escolha: "))

    if(jogo == 1):
        adivinhe_palavra.jogar()
    elif(jogo == 2):
        adivinhe_numero.jogar()

if(__name__ == "__main__"):
    escolher_jogo()