#Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()



#Glocal Scope

player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)


#BAD CODE
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)


