def format_name(name, last_name):
    print(f'1: {name.title()} {last_name.title()}')
format_name('arnaldo', 'rocha')


def format_name(name, last_name):
    formated_name = name.title()
    formated_last_name = last_name.title()
    return f"{formated_name} {formated_last_name}" 
formated_string = format_name('arnaldo', 'rocha')
print(f'2: {formated_string}')



def format_name(name, last_name):
    formated_name = name.title()
    formated_last_name = last_name.title()
    return f"3: {formated_name} {formated_last_name}" 
print(format_name('arnaLdO', 'RoChA'))
