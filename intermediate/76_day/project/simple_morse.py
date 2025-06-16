# Dicionário com o código Morse
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    ' ': '/',      '.': '.-.-.-', ',': '--..--',
    '?': '..--..', '!': '-.-.--'
}

def text_to_morse(text):
    """Converte texto para código Morse"""
    text = text.upper()
    morse = ''
    for char in text:
        if char in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[char] + ' '
        else:
            morse += '? '  # caractere desconhecido
    return morse.strip()

# Interface simples no terminal
if __name__ == "__main__":
    print("=== Conversor Texto → Código Morse ===")
    entrada = input("Digite o texto para converter: ")
    resultado = text_to_morse(entrada)
    print("\nCódigo Morse:")
    print(resultado)
