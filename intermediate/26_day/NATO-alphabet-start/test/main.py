# 26. NATO Alphabet
import pandas as pd

# TODO 1: Create a dictionary in this format: {"A":Alfa, "B":Bravo, "C":Charlie}
nato_alphabet = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}

# TODO 2: Create a list of the phonetic alphabet code words that the user inputs.
def generate_phonetic_code():
    word = input("Enter a word: ").upper()
    try:
        phonetic_code = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic_code()
    else:
        print(phonetic_code)
        return phonetic_code
generate_phonetic_code()

# TODO 3: Create a DataFrame from the dictionary and print it
nato_df = pd.DataFrame(list(nato_alphabet.items()), columns=["Letter", "Code"])
print(nato_df)

# TODO 4: Save the DataFrame to a CSV file
nato_df.to_csv("nato_alphabet.csv", index=False)

# TODO 5: Read the CSV file and print its contents
nato_df_from_csv = pd.read_csv("nato_alphabet.csv")
print(nato_df_from_csv)

# TODO 6: Create a function to generate the phonetic code for a given word
def generate_phonetic_code_from_csv(word):
    word = word.upper()
    try:
        phonetic_code = [nato_df_from_csv[nato_df_from_csv["Letter"] == letter]["Code"].values[0] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic_code_from_csv(word)
    else:
        print(phonetic_code)
        return phonetic_code
generate_phonetic_code_from_csv("hello")

# TODO 7: Create a function to generate the phonetic code for a given word using the DataFrame
def generate_phonetic_code_from_df(word):
    word = word.upper()
    try:
        phonetic_code = [nato_df[nato_df["Letter"] == letter]["Code"].values[0] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic_code_from_df(word)
    else:
        print(phonetic_code)
        return phonetic_code
generate_phonetic_code_from_df("hello")

# TODO 8: Create a function to generate the phonetic code for a given word using the DataFrame and save it to a CSV file
def generate_phonetic_code_from_df_and_save(word):
    word = word.upper()
    try:
        phonetic_code = [nato_df[nato_df["Letter"] == letter]["Code"].values[0] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic_code_from_df_and_save(word)
    else:
        print(phonetic_code)
        nato_df.to_csv("nato_alphabet.csv", index=False)
        return phonetic_code
generate_phonetic_code_from_df_and_save("hello")