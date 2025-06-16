# Importa o módulo random para gerar números aleatórios
import random

# Importa o módulo time para criar pausas (delays) na execução
import time

# Importa o módulo os (não é usado, pode ser removido se quiser)
import os

# Tenta importar o módulo winsound (disponível apenas no Windows) para tocar sons
try:
    import winsound
    SOUND_ENABLED = True  # Se o import funcionar, ativa os sons
except ImportError:
    SOUND_ENABLED = False  # Se não funcionar (ex.: no Linux), desativa os sons

# Função para exibir a animação de rolagem do dado
def roll_dice_animation():
    print("\nRolando o dado... 🎲\n")  # Mensagem inicial antes da rolagem

    # Faz 10 "rolagens rápidas" para simular o movimento do dado
    for _ in range(10):
        num = random.randint(1, 6)  # Gera um número aleatório de 1 a 6
        print(f"\rNúmero: {num}", end='', flush=True)  # Atualiza o número na mesma linha do terminal

        # Se o som estiver disponível (no Windows), toca um beep para cada número
        if SOUND_ENABLED:
            winsound.Beep(1000 + num * 200, 100)  # Frequência varia conforme o número (fica mais divertido)

        time.sleep(0.1)  # Pausa de 0,1 segundo para criar o efeito de "animação"

    print()  # Pula uma linha depois da animação

# Função principal do programa
def main():
    while True:  # Loop para permitir que o usuário jogue várias vezes
        input("\nPressione Enter para lançar o dado...")  # Aguarda o usuário pressionar Enter

        roll_dice_animation()  # Chama a função que faz a animação de rolagem

        final_result = random.randint(1, 6)  # Gera o resultado final do dado (de 1 a 6)
        print(f"\n🎉 Resultado final: {final_result} 🎉")  # Exibe o resultado para o usuário

        # Se o som estiver ativado, toca uma sequência de beeps para comemorar
        if SOUND_ENABLED:
            for freq in [800, 1000, 1200]:  # Frequências diferentes para criar um "efeito de vitória"
                winsound.Beep(freq, 150)  # Cada beep dura 150 milissegundos

        # Pergunta se o usuário deseja jogar novamente
        choice = input("\nQuer jogar novamente? (s/n): ").strip().lower()  # Converte resposta para minúscula

        if choice != 's':  # Se a resposta não for "s" (sim), encerra o programa
            print("\nObrigado por jogar! Até a próxima. 👋")
            break  # Sai do loop

# Verifica se o arquivo está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    main()  # Chama a função principal
