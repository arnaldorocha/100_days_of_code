import random
import module

random_int = random.randint(0, 1)

print(random_int)

random_0_1_float = random.random()
print(random_0_1_float)

random_0_10_float = random.random()*10
print(random_0_10_float)

random_int = random.randint(0, 10)

print(random_int)

random_float = random.uniform(0, 10)  

print(round(random_float, 2))


if random_int == 0:
    print("Heads")
else:
    print("tails")

print(module.module_1)