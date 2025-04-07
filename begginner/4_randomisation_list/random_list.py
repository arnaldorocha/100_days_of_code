import random
friends = ["Mara", "Diogo", "Lara", "Thiago"]

#1st option
print(random.choice(friends))

#2st option
random_index = random.randint(0, 3)
print(friends[random_index])