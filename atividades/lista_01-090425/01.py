import random

def guessing_game():
    secret_number = random.randint(0, 100)
    guesses = []
    print("Tente adivinhar o número entre 0 e 100!")

    while True:
        try:
            guess = int(input("Digite seu palpite: "))
            guesses.append(guess)

            if guess < secret_number:
                print("Muito baixo! Tente novamente.")
            elif guess > secret_number:
                print("Muito alto! Tente novamente.")
            else:
                print("Parabéns! Você acertou!")
                break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    print("\n--- Resultado ---")
    print("Número de tentativas:", len(guesses))
    print("Seus palpites foram:", guesses)

guessing_game()