for number in range(1, 101):  # Percorre de 1 a 100
    if number % 3 == 0 and number % 5 == 0:  # Divisível por 3 e 5
        print("FizzBuzz")
    elif number % 3 == 0:  # Divisível por 3
        print("Fizz")
    elif number % 5 == 0:  # Divisível por 5
        print("Buzz")
    else:  # Não é divisível por 3 nem por 5
        print(number)