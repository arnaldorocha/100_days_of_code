import random
import time
import os

# Variável global: usada em todo o programa
secret_number = 0

# Função para limpar o terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para simular um carregamento com arte
def loading_screen():
    print("\nCarregando novo jogo", end="")
    for _ in range(5):
        time.sleep(0.4)
        print(".", end="", flush=True)
    time.sleep(0.3)
    print("\n")

# Função para definir dificuldade e retornar tentativas
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10
    else:
        return 5

# Verifica se o chute está correto
def check_guess(guess, secret_number):
    if guess > secret_number:
        print("Too high.")
        return False
    elif guess < secret_number:
        print("Too low.")
        return False
    else:
        print(f"🎉 You got it! The answer was {secret_number}.")
        return True

# Função principal do jogo
def game():
    global secret_number
    clear_terminal()
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts_remaining = set_difficulty()

    while attempts_remaining > 0:
        print(f"\nYou have {attempts_remaining} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        is_correct = check_guess(guess, secret_number)

        if is_correct:
            break

        attempts_remaining -= 1

        if attempts_remaining > 0:
            print("Guess again.")
        else:
            print(f"💥 You've run out of guesses. The number was {secret_number}. Game Over.")

# Loop principal: repete o jogo se o jogador quiser
def main():
    while True:
        game()
        replay = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("\n👋 Thanks for playing. See you next time!")
            break
        loading_screen()

# Inicia o programa
main()
