# Vamos criar um objeto a partir de um plano que outra pessoa tem
#e a planta vive noutro módulo chamado tartaruga    
import outro_modulo
print(outro_modulo.outra_variavel)

import turtle #basicamente fez a mesma coisa que o de cima, mas sem criar o arquivo extra
timmy = turtle.Turtle()  #agora podemos guardar tudo isto num objeto real que passamos a nomear



from turtle import Turtle, Screen # encurta a criançao do novo objeto
#object e class
marco = Turtle() 
print(marco)
marco.shape("turtle")
marco.color("green")

marco.forward(100)

my_screen = Screen()
print(my_screen.canvheight)  # attribute
my_screen.exitonclick()      # method


#não apenas a tartarura, mas todo um mundo projetos(embalagens) que pode explorar
#e pode começar a utilizar esses pacotes de código que outros programadores tem ja desenvolvido
# simplesmente criando objetos a partir das plantas existentes e lendo a documentação 
#para conseguir fazer varias coisas que deseja