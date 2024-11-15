print("Let's go to the market!")
print("Your child is hungry, but he doesn't like some things. Let's see if you can guess what he likes.")

# Pergunta sobre a seção de frutas
fruit_section = input("You entered the supermarket and went to the fruit section. "
                      "What would you like to buy? Among the options, he likes: "
                      "banana, apple, orange, and grape. ")

# Verifica a fruta escolhida
if fruit_section == "grape":
    print("You guessed it! Let's keep shopping.")
    
    # Pergunta sobre o doce favorito
    candy = input("Now try to guess which candy he likes: ")

    if candy == "chocolate":
        # Pergunta sobre a bebida favorita
        drink = input("Very well, now all that's left is something to drink: ")

        if drink == "grape juice":
            print("Very well, just pay for your purchases and leave.")
        else:
            print("Invalid option for drink!")
    else:
        print("He doesn't like that candy.")
        
elif fruit_section == "orange":
    print("What bad luck! This fruit is spoiled.")

elif fruit_section == "apple":
    print("Unfortunately, this fruit is out of stock.")

elif fruit_section == "banana":
    print("Your son didn't want this fruit today.")

else:
    print("Invalid option for fruit!")
