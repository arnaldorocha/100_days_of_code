import random

letters = ['a','b','c','ç','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
letters_m = ['A','B','C','Ç','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = [',','@','!','$','%','¨','¬','*','(','"',"'",",",")",'_','-','+','=','§','|','?','<','>','.',':',';','^','~','`',"´","´",'{','}','}',']','.','[',']']

nr_letters = int(input(" how many letters do you want? "))
nr_letters_m = int(input(" how many letters do you want? "))
nr_numbers= int(input(" how many numbers do you want? "))
nr_symbols= int(input(" how many symbols do you want? "))

password = ""

for var in range(nr_letters):
    password += random.choice(letters)
for var in range(nr_letters_m):
    password += random.choice(letters_m)
for var in range(nr_numbers):
    password += random.choice(numbers)
for var in range(nr_symbols):
    password += random.choice(symbols)


print(password)