def format_name(name, last_name):
    if name == "" or last_name == "":
        return "\nVoce não inseriu um nome\n"

    formated_name = name.title()
    formated_last_name = last_name.title()
    return f"\nResultado do nome: {formated_name} {formated_last_name}\n" 

print(format_name(input('\nQual é seu primeiro nome: '), input('\nQual é seu sobrenome: ')))
