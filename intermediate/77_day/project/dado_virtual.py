import random
import time
import os

try:
    import winsound
    SOUND_ENABLED = True
except ImportError:
    SOUND_ENABLED = False

def roll_dice_animation():
    print("\nRolando o dado... 🎲\n")
    for _ in range(10):
        num = random.randint(1, 6)
        print(f"\rNúmero: {num}", end='', flush=True)
        if SOUND_ENABLED:
            # Faz um som rápido de beep
            winsound.Beep(1000 + num * 200, 100)
        time.sleep(0.1)
    print()

def main():
    while True:
        input("\nPressione Enter para lançar o dado...")

        roll_dice_animation()

        final_result = random.randint(1, 6)
        print(f"\n🎉 Resultado final: {final_result} 🎉")

        if SOUND_ENABLED:
            # Pequena comemoração com sons mais longos
            for freq in [800, 1000, 1200]:
                winsound.Beep(freq, 150)

        choice = input("\nQuer jogar novamente? (s/n): ").strip().lower()
        if choice != 's':
            print("\nObrigado por jogar! Até a próxima. 👋")
            break

if __name__ == "__main__":
    main()
