import turtle  
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/project_states_eua/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/project_states_eua/50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/project_states_eua/missing_states.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        print(state_data.x, state_data.y)
        print(state_data.state)

screen.exitonclick()
