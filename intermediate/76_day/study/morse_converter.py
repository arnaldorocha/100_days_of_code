# Criando um dicionário com o Código Morse
# Um dicionário em Python é como uma "tabela de tradução"
# Nele, cada letra ou símbolo tem uma "tradução" para o código Morse

MORSE_CODE_DICT = {
    'A': '.-',     # A = .-
    'B': '-...',   # B = -...
    'C': '-.-.',   # C = -.-.
    'D': '-..',    # D = -..
    'E': '.',      # E = .
    'F': '..-.',   # F = ..-.
    'G': '--.',    # G = --.
    'H': '....',   # H = ....
    'I': '..',     # I = ..
    'J': '.---',   # J = .---
    'K': '-.-',    # K = -.-
    'L': '.-..',   # L = .-..
    'M': '--',     # M = --
    'N': '-.',     # N = -.
    'O': '---',    # O = ---
    'P': '.--.',   # P = .--.
    'Q': '--.-',   # Q = --.-
    'R': '.-.',    # R = .-.
    'S': '...',    # S = ...
    'T': '-',      # T = -
    'U': '..-',    # U = ..-
    'V': '...-',   # V = ...-
    'W': '.--',    # W = .--
    'X': '-..-',   # X = -..-
    'Y': '-.--',   # Y = -.--
    'Z': '--..',   # Z = --..

    # Agora os números:
    '0': '-----',  # 0 = -----
    '1': '.----',  # 1 = .----
    '2': '..---',  # 2 = ..---
    '3': '...--',  # 3 = ...--
    '4': '....-',  # 4 = ....-
    '5': '.....',  # 5 = .....
    '6': '-....',  # 6 = -....
    '7': '--...',  # 7 = --...
    '8': '---..',  # 8 = ---..
    '9': '----.',  # 9 = ----.

    # Espaço entre palavras
    ' ': '/',      # Espaço no texto = / no Morse

    # Pontuação extra:
    '.': '.-.-.-', # Ponto final
    ',': '--..--', # Vírgula
    '?': '..--..', # Ponto de interrogação
    '!': '-.-.--'  # Exclamação
}

# Agora vamos criar uma função para fazer a conversão de texto para Morse
def text_to_morse(text):
    """Converte texto para código Morse"""
    
    # Deixa todas as letras em maiúsculas (pois o dicionário só tem letras maiúsculas)
    text = text.upper()

    # Criamos uma variável vazia para guardar o resultado final
    morse = ''

    # Agora vamos olhar cada letra (ou símbolo) do texto
    for char in text:
        # Se o caractere está no dicionário, converte para Morse
        if char in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[char] + ' '  # Adiciona o código e um espaço depois
        else:
            # Se o caractere não existe no dicionário, usamos um "?" para mostrar que não foi reconhecido
            morse += '? '

    # Por fim, removemos o espaço extra do final e devolvemos o resultado
    return morse.strip()

# Aqui criamos uma interface simples para rodar no terminal (modo texto)

# Este bloco só roda se o arquivo for executado diretamente (e não importado)
if __name__ == "__main__":
    # Exibimos um título legal pro usuário
    print("=== Conversor Texto → Código Morse ===")
    
    # Pedimos para o usuário digitar um texto
    entrada = input("Digite o texto para converter: ")
    
    # Chamamos a função para converter
    resultado = text_to_morse(entrada)
    
    # Mostramos o resultado final
    print("\nCódigo Morse:")
    print(resultado)
