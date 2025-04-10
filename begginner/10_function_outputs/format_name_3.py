def format_name(name, last_name):
    """ Take a first and last name and format
    it to return the title case version of the name """


    formated_name = name.title()
    formated_last_name = last_name.title()
    return f"{formated_name} {formated_last_name}\n" 

formatted_name = format_name('arnaldo', 'rocha')
length = len(formatted_name)

print(formatted_name)
print(length)