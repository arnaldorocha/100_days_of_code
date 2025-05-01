import pandas as pd
import json
import os
import tkinter as tk
from tkinter import messagebox

JSON_PATH = "phonetic_output.json"

data = pd.read_csv("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/30_day/project/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Variável global para controle de edição
edit_index = None

def load_saved_data():
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, "r") as file:
            return json.load(file)
    return []

def save_all_data(data):
    with open(JSON_PATH, "w") as file:
        json.dump(data, file, indent=4)

def save_data(entry):
    data = load_saved_data()
    data.append(entry)
    save_all_data(data)

def update_listbox():
    listbox.delete(0, tk.END)
    data = load_saved_data()
    for entry in data:
        listbox.insert(tk.END, f"{entry['word']}: {', '.join(entry['phonetic'])}")

def generate_phonetic():
    global edit_index
    word = entry.get().upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        messagebox.showerror("Invalid Input", "Please enter only letters A-Z.")
    else:
        result_label.config(text=", ".join(output_list))
        data = load_saved_data()

        if edit_index is not None:
            data[edit_index] = {"word": word, "phonetic": output_list}
            save_all_data(data)
            edit_index = None
        else:
            save_data({"word": word, "phonetic": output_list})

        update_listbox()
        entry.delete(0, tk.END)

def edit_selected():
    global edit_index
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        data = load_saved_data()
        entry.delete(0, tk.END)
        entry.insert(0, data[index]['word'])
        result_label.config(text=", ".join(data[index]['phonetic']))
        edit_index = index

def delete_selected():
    global edit_index
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        data = load_saved_data()
        confirm = messagebox.askyesno("Confirm Delete", f"Delete '{data[index]['word']}'?")
        if confirm:
            data.pop(index)
            save_all_data(data)
            update_listbox()
            result_label.config(text="")
            entry.delete(0, tk.END)
            edit_index = None

# Tkinter UI
window = tk.Tk()
window.title("NATO Phonetic Generator")
window.geometry("550x600")
window.config(padx=20, pady=20)

entry_label = tk.Label(window, text="Enter a word:", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(window, width=30, font=("Arial", 12))
entry.pack(pady=5)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate / Save", command=generate_phonetic, font=("Arial", 12))
generate_button.grid(row=0, column=0, padx=5)

edit_button = tk.Button(button_frame, text="✏️ Edit", command=edit_selected, font=("Arial", 12))
edit_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="🗑️ Delete", command=delete_selected, font=("Arial", 12))
delete_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)

listbox_label = tk.Label(window, text="Saved Entries:", font=("Arial", 12))
listbox_label.pack()

listbox = tk.Listbox(window, width=60, height=10)
listbox.pack(pady=10)

update_listbox()
window.mainloop()
