import random

def print_board(board):
    """Exibe o tabuleiro atual."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print()

def check_winner(board, player):
    """Verifica se o jogador atual venceu."""
    # Linhas
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Colunas
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonais
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Verifica se o tabuleiro está cheio (empate)."""
    return all(cell != " " for row in board for cell in row)

def get_player_move(board):
    """Pega a jogada do jogador humano."""
    while True:
        try:
            row = int(input("Escolha a linha (0, 1 ou 2): "))
            col = int(input("Escolha a coluna (0, 1 ou 2): "))
        except ValueError:
            print("Entrada inválida! Use apenas números 0, 1 ou 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Posição fora do tabuleiro! Tente novamente.")
        elif board[row][col] != " ":
            print("Essa posição já está ocupada! Escolha outra.")
        else:
            return row, col

def get_ai_move(board):
    """IA básica: escolhe uma posição aleatória vazia."""
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def play_game(mode, scores):
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Vez do jogador {current_player}")

        # Escolhe jogada (Humano ou IA)
        if mode == "1" and current_player == "O":
            row, col = get_ai_move(board)
            print(f"IA jogou na posição: Linha {row}, Coluna {col}")
        else:
            row, col = get_player_move(board)

        board[row][col] = current_player

        # Verifica vitória
        if check_winner(board, current_player):
            print_board(board)
            if mode == "1" and current_player == "O":
                print("🤖 A IA venceu!")
                scores["IA"] += 1
            else:
                print(f"🏆 Jogador {current_player} venceu!")
                scores[current_player] += 1
            break

        # Verifica empate
        if is_full(board):
            print_board(board)
            print("⚖️ Empate!")
            scores["Empates"] += 1
            break

        # Alterna jogador
        current_player = "O" if current_player == "X" else "X"

def main():
    print("🎮 Bem-vindo ao Tic Tac Toe (Jogo da Velha) 🎮")
    scores = {"X": 0, "O": 0, "IA": 0, "Empates": 0}

    while True:
        print("\nEscolha o modo de jogo:")
        print("1 - Single Player (Você vs IA)")
        print("2 - Two Players (Jogador X vs Jogador O)")

        mode = input("Digite 1 ou 2: ").strip()

        if mode not in ["1", "2"]:
            print("Modo inválido. Escolha 1 ou 2.")
            continue

        play_game(mode, scores)

        # Mostra o placar atual
        print("\n📊 Placar Atual:")
        print(f"Jogador X: {scores['X']} vitórias")
        print(f"Jogador O: {scores['O']} vitórias")
        if mode == "1":
            print(f"IA: {scores['IA']} vitórias")
        print(f"Empates: {scores['Empates']}")

        # Pergunta se quer jogar novamente
        again = input("\nJogar novamente? (s/n): ").strip().lower()
        if again != "s":
            print("\nObrigado por jogar! Até a próxima 👋")
            break

if __name__ == "__main__":
    main()
