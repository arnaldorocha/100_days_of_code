import random
import my_module

random_inter = random.randint(1,  10)

print(random_inter)
print(my_module.my_number)

# gerar numeros float aleatórios 0 até 1
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# gerar numeros float aleatórios 0 até 10
random_number_0_to_10 = random.random() * 10
# O limite se da pela multiplicação depois do random
print(random_number_0_to_10)

float_random = random.uniform(1, 10)  # gerar numeros float aleatórios 1 até 10
print(round(float_random, 2))

heads_tails = round(random_number_0_to_1, 0)

if heads_tails == 1:
    print("heads")
else:
    print("tails")
