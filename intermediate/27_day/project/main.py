from tkinter import *

# Função para converter milhas em quilômetros
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometer_result_label.config(text=f"{km:.2f}")

# Janela principal
window = Tk()
window.title("Conversor de Milhas para Km")
window.config(padx=20, pady=20)

# Entrada de texto
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Label "Miles"
miles_label = Label(text="Milhas")
miles_label.grid(column=2, row=0)

# Label "is equal to"
is_equal_label = Label(text="é igual a")
is_equal_label.grid(column=0, row=1)

# Resultado da conversão
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Label "Km"
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Botão para converter
calculate_button = Button(text="Converter", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
