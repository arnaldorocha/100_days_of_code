import turtle   
import pandas as pd

screen = turtle.Screen()
screen.title("Jogo dos Estados do Brasil")
image = "c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/projeto_estados_brasil/map.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/projeto_estados_brasil/estados.csv")
all_states = data.estado.to_list()

guessed_states = []

while len(guessed_states) < 27:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/27 Estados Corretos", prompt="Qual é o nome de outro estado? ")
    print(answer_state)

    if answer_state is None or answer_state.lower() == "sair":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/projeto_estados_brasil/estados_perdidos.csv")
        break

    answer_state = answer_state

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("Black")  # Muda a cor do texto
        state_data = data[data.estado == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.sigla.item(), align="center", font=("Arial", 12, "bold"))
        print(state_data.x, state_data.y)
        print(state_data.estado)

screen.exitonclick()
