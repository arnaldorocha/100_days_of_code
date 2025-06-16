import time
import winsound

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

# Frequência em Hertz (Hz) e duração em milissegundos
DOT_DURATION = 200  # duração do ponto (ms)
DASH_DURATION = DOT_DURATION * 3
FREQUENCY = 750  # frequência do som (Hz)
GAP = DOT_DURATION  # intervalo entre sons

def play_morse(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(FREQUENCY, DOT_DURATION)
        elif symbol == '-':
            winsound.Beep(FREQUENCY, DASH_DURATION)
        elif symbol == '/':
            time.sleep(GAP / 500)  # pausa entre palavras
        else:
            time.sleep(GAP / 1000)  # pausa entre letras
        time.sleep(GAP / 1000)  # pequena pausa entre símbolos

def text_to_morse(text):
    text = text.upper()
    morse = ''
    for char in text:
        if char in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[char] + ' '
        else:
            morse += '? '
    return morse.strip()

if __name__ == "__main__":
    print("=== Conversor Texto → Código Morse com Som ===")
    entrada = input("Digite o texto: ")
    morse_result = text_to_morse(entrada)
    print("\nCódigo Morse:")
    print(morse_result)
    print("\nReproduzindo som...")
    play_morse(morse_result)
