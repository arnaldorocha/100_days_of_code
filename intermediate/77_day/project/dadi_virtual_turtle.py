import turtle
import random
import time

# Configuração da janela
screen = turtle.Screen()
screen.title("Simulador de Dado Virtual 🎲")
screen.bgcolor("white")

# Criar a tartaruga que vai desenhar o dado
dice = turtle.Turtle()
dice.hideturtle()
dice.speed(0)

# Posições relativas dos pontos nas faces do dado
dots = {
    1: [(0, 0)],
    2: [(-30, 30), (30, -30)],
    3: [(-30, 30), (0, 0), (30, -30)],
    4: [(-30, 30), (30, 30), (-30, -30), (30, -30)],
    5: [(-30, 30), (30, 30), (0, 0), (-30, -30), (30, -30)],
    6: [(-30, 30), (30, 30), (-30, 0), (30, 0), (-30, -30), (30, -30)]
}

def draw_dice_face(number):
    dice.clear()
    dice.up()
    dice.goto(-50, 50)
    dice.down()

    # Desenha o quadrado do dado
    dice.pensize(3)
    for _ in range(4):
        dice.forward(100)
        dice.right(90)

    # Desenha os pontos da face
    dice.up()
    for x, y in dots[number]:
        dice.goto(x, y)
        dice.down()
        dice.begin_fill()
        dice.circle(5)
        dice.end_fill()
        dice.up()

def roll_dice_animation():
    for _ in range(15):  # Quantidade de "giros" antes de parar
        face = random.randint(1, 6)
        draw_dice_face(face)
        time.sleep(0.1)

def main():
    while True:
        input("\nPressione Enter para lançar o dado...")

        roll_dice_animation()

        final_face = random.randint(1, 6)
        draw_dice_face(final_face)

        print(f"\n🎉 Resultado final: {final_face} 🎉")

        again = input("\nJogar novamente? (s/n): ").strip().lower()
        if again != 's':
            break

    turtle.bye()

if __name__ == "__main__":
    main()
