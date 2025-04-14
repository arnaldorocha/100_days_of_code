from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]  # não encontra a posição 6, por que não tem posição 6, lista [0:5]
dice_num = randint(1, 6) 
print(dice_images[dice_num])

#testar código mais de uma ou duas vezes, até reproduzir o erro
