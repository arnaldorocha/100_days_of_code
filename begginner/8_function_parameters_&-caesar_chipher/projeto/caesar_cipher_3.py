# Importa o módulo art, que deve conter uma arte em ASCII chamada logo
import art
print(art.logo)  # Exibe o logo do programa

# Lista com as letras do alfabeto
alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Variável de controle para repetir o programa
should_continue = True

# Loop principal do programa
while should_continue:

    # Solicita ao usuário se deseja codificar ou decodificar
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Solicita a mensagem
    text = input('Type your message:\n').lower()

    # Solicita o número de posições para o deslocamento
    shift = int(input('Type the shift number:\n'))

    # Define a função que executa a cifra de César
    def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ''  # Variável para armazenar o resultado final

        # Se o usuário escolheu "decode", inverte o sinal do deslocamento
        if encode_or_decode == 'decode':
            shift_amount *= -1

        # Percorre cada letra da mensagem
        for letter in original_text:

            # Se o caractere não estiver no alfabeto, adiciona como está (espaços, símbolos, etc.)
            if letter not in alphabeth:
                output_text += letter
            else:
                # Encontra o índice da letra no alfabeto
                shifted_position = alphabeth.index(letter) - shift_amount

                # Garante que o índice não ultrapasse o final da lista
                shifted_position %= len(alphabeth)

                # Adiciona a nova letra (deslocada) ao resultado
                output_text += alphabeth[shifted_position]

        # Mostra o resultado final da codificação/decodificação
        print(f"Here is the {encode_or_decode}d result: {output_text}")

    # Chama a função para executar a cifra
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Pergunta se o usuário quer rodar novamente
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. ")
    if restart == 'no':
        should_continue = False  # Sai do loop
        print('Goodbye')  # Mensagem de despedida
