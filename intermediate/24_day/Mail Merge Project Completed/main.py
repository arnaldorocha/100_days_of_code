import os

PLACEHOLDER = "[name]"

# Caminho base onde está o script
base_path = os.path.dirname(__file__)

# Caminhos absolutos para os arquivos e pastas
names_path = os.path.join(base_path, "Input", "Names", "invited_names.txt")
letter_path = os.path.join(base_path, "Input", "Letters", "starting_letter.txt")
output_dir = os.path.join(base_path, "Output", "ReadyToSend")

# Garante que o diretório de saída existe
os.makedirs(output_dir, exist_ok=True)

# Lê os nomes
with open(names_path) as names_file:
    names = names_file.readlines()

# Lê o conteúdo da carta
with open(letter_path) as letter_file:
    letter_contents = letter_file.read()

# Gera uma carta personalizada para cada nome
for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    output_path = os.path.join(output_dir, f"letter_for_{stripped_name}.txt")
    with open(output_path, mode="w") as completed_letter:
        completed_letter.write(new_letter)




# PLACEHOLDER = "[name]"


# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()

# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)

