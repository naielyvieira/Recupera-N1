from random import randint

def jogo():
    numero_secreto = randint(1, 50)
    tentativas = 0

    print("Tente adivinhar o número secreto entre 1 e 50.")

    while True:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Palpite muito baixo. Tente novamente!")
        elif palpite > numero_secreto:
            print("Palpite muito alto. Tente novamente!")
        else:
            print("Parabéns! Você acertou o número secreto que é {} em {} tentativa(s)!".format(numero_secreto, tentativas))
            break

jogo()
