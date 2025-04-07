import random
import module

random_int = random.randint(0, 10) # aleatório integer
random_float = random.random() * 10
random_float_uniform = random.uniform(0,10) # aleatório float

print(random_int)
print(random_float)
print(random_float_uniform)

print(round(random_float, 2))
print(round(random_float_uniform, 2))

print(module.module_1)
