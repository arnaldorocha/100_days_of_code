# Importamos duas bibliotecas que já vêm com o Python:

import time         # Esta biblioteca permite fazer o programa "esperar" por alguns segundos ou milissegundos (pausas entre os sons)
import winsound     # Esta só funciona no Windows. Ela permite tocar sons simples (tipo um beep) com frequência e duração escolhidas.

# Agora vamos criar um dicionário chamado MORSE_CODE_DICT
# Ele transforma cada letra ou número em seu equivalente em código Morse

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
    '9': '----.', ' ': '/'  # Para representar espaço entre palavras usamos uma barra /
}

# Agora vamos criar algumas configurações sobre o som:

DOT_DURATION = 200          # Duração de um ponto (em milissegundos). Aqui: 200ms = 0,2 segundos
DASH_DURATION = DOT_DURATION * 3  # Duração de um traço é 3 vezes a do ponto
FREQUENCY = 750             # Frequência do som (quanto mais alto o número, mais agudo o som). Aqui usamos 750 Hz.
GAP = DOT_DURATION          # Intervalo de tempo entre cada som (pausa entre um ponto ou traço e o próximo)

# Função para TOCAR o código Morse com som
def play_morse(morse_code):
    # Vamos percorrer cada símbolo no código Morse (ponto, traço, espaço, etc)
    for symbol in morse_code:
        if symbol == '.':
            # Se for um ponto, toca um beep curto
            winsound.Beep(FREQUENCY, DOT_DURATION)
        elif symbol == '-':
            # Se for um traço, toca um beep longo
            winsound.Beep(FREQUENCY, DASH_DURATION)
        elif symbol == '/':
            # Se for uma barra (ou seja, espaço entre palavras), faz uma pausa maior
            time.sleep(GAP / 500)
        else:
            # Se for outro caractere (como espaço entre letras), faz uma pausa curta
            time.sleep(GAP / 1000)
        
        # Pequena pausa depois de cada símbolo (ponto ou traço)
        time.sleep(GAP / 1000)

# Função para CONVERTER texto normal para código Morse
def text_to_morse(text):
    text = text.upper()  # Deixa o texto todo em letras maiúsculas (para combinar com as chaves do dicionário)
    morse = ''           # Criamos uma string vazia para guardar o código Morse final
    for char in text:
        if char in MORSE_CODE_DICT:
            # Se o caractere está no dicionário, adicionamos o código correspondente e um espaço
            morse += MORSE_CODE_DICT[char] + ' '
        else:
            # Se o caractere não existe no dicionário (ex: emoji), colocamos um ponto de interrogação
            morse += '? '
    return morse.strip()  # Tiramos o espaço extra do final

# Este bloco só roda se o programa for executado direto (não se for importado)
if __name__ == "__main__":
    print("=== Conversor Texto → Código Morse com Som ===")
    
    # Pedimos ao usuário para digitar algum texto
    entrada = input("Digite o texto: ")
    
    # Chamamos a função para converter o texto para código Morse
    morse_result = text_to_morse(entrada)
    
    # Mostramos o código Morse na tela
    print("\nCódigo Morse:")
    print(morse_result)
    
    # Agora tocamos o código Morse com som!
    print("\nReproduzindo som...")
    play_morse(morse_result)
