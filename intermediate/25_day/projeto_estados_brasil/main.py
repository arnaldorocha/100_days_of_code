import turtle  

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/projeto_estados_brasil/mapa_do_brasil.gif"
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)
    # turtle.goto(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

# screen.exitonclick()
