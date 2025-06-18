import tkinter as tk  # Importa o módulo Tkinter para criar a interface gráfica
from tkinter import messagebox  # Importa o messagebox para exibir mensagens de alerta
import random  # Importa o módulo random para gerar jogadas aleatórias da IA

class TicTacToe:
    def __init__(self, root):
        # Inicializa a janela principal
        self.root = root
        self.root.title("Tic Tac Toe (Dificuldades) 🎮")

        # Variáveis de controle do jogo
        self.mode = None  # Modo de jogo: Single player ou Two players
        self.difficulty = None  # Dificuldade da IA
        self.current_player = "X"  # Começa com o jogador X
        self.board = [["" for _ in range(3)] for _ in range(3)]  # Tabuleiro 3x3 vazio
        self.scores = {"X": 0, "O": 0, "IA": 0, "Empates": 0}  # Placar

        # Exibe a tela de seleção de modo
        self.create_mode_selection()

    def create_mode_selection(self):
        # Limpa a tela (remove todos os widgets existentes)
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria botões para selecionar o modo de jogo
        tk.Label(self.root, text="Escolha o modo de jogo:", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Single Player (vs IA)", font=("Arial", 12),
                  command=self.choose_difficulty).pack(pady=5)
        tk.Button(self.root, text="Two Players", font=("Arial", 12),
                  command=lambda: self.start_game("2")).pack(pady=5)

    def choose_difficulty(self):
        # Tela para escolher o nível de dificuldade da IA
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Escolha a dificuldade da IA:", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Fácil", font=("Arial", 12),
                  command=lambda: self.start_game("1", "easy")).pack(pady=5)
        tk.Button(self.root, text="Médio", font=("Arial", 12),
                  command=lambda: self.start_game("1", "medium")).pack(pady=5)
        tk.Button(self.root, text="Imbatível", font=("Arial", 12),
                  command=lambda: self.start_game("1", "hard")).pack(pady=5)

    def start_game(self, mode, difficulty=None):
        # Inicia o jogo com o modo e dificuldade selecionados
        self.mode = mode
        self.difficulty = difficulty
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_game_board()

    def create_game_board(self):
        # Cria o tabuleiro na tela
        for widget in self.root.winfo_children():
            widget.destroy()

        self.buttons = []  # Lista para armazenar os botões

        for row in range(3):
            button_row = []
            for col in range(3):
                # Cria cada botão do tabuleiro
                btn = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                command=lambda r=row, c=col: self.player_move(r, c))
                btn.grid(row=row, column=col)
                button_row.append(btn)
            self.buttons.append(button_row)

        # Exibe o status do jogador atual
        self.status_label = tk.Label(self.root, text=f"Vez do jogador {self.current_player}", font=("Arial", 12))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Exibe o placar
        self.update_score_label()

    def update_score_label(self):
        # Atualiza a exibição do placar
        score_text = f"Placar - X: {self.scores['X']} | O: {self.scores['O']} | IA: {self.scores['IA']} | Empates: {self.scores['Empates']}"
        self.score_label = tk.Label(self.root, text=score_text, font=("Arial", 10))
        self.score_label.grid(row=4, column=0, columnspan=3)

    def player_move(self, row, col):
        # Função chamada quando um jogador clica em um botão
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Verifica se houve vencedor
            if self.check_winner(self.current_player):
                self.handle_game_end(f"Jogador {self.current_player} venceu!")
                if self.mode == "1" and self.current_player == "O":
                    self.scores["IA"] += 1
                else:
                    self.scores[self.current_player] += 1
                return

            # Verifica empate
            if self.check_tie():
                self.scores["Empates"] += 1
                self.handle_game_end("Empate!")
                return

            # Alterna para o próximo jogador
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"Vez do jogador {self.current_player}")

            # Se for a vez da IA, executa a jogada da IA
            if self.mode == "1" and self.current_player == "O":
                self.root.after(500, self.ai_move)  # Pequeno delay para dar impressão de pensar

    def ai_move(self):
        # Define a jogada da IA com base na dificuldade escolhida
        if self.difficulty == "easy":
            self.random_move()
        elif self.difficulty == "medium":
            if random.random() < 0.8:
                self.best_move()
            else:
                self.random_move()
        elif self.difficulty == "hard":
            self.best_move()

    def random_move(self):
        # IA joga aleatoriamente (modo fácil ou erro intencional no médio)
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.player_move(row, col)

    def best_move(self):
        # IA joga o melhor movimento possível usando o algoritmo Minimax
        _, move = self.minimax(self.board, True)
        if move:
            row, col = move
            self.player_move(row, col)

    def minimax(self, board, is_maximizing):
        # Algoritmo Minimax: Faz a IA pensar nas melhores jogadas futuras
        winner = self.get_winner(board)
        if winner == "O":
            return 1, None  # Vitória da IA
        elif winner == "X":
            return -1, None  # Vitória do jogador humano
        elif self.is_board_full(board):
            return 0, None  # Empate

        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "":
                        board[row][col] = "O"
                        score, _ = self.minimax(board, False)
                        board[row][col] = ""
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "":
                        board[row][col] = "X"
                        score, _ = self.minimax(board, True)
                        board[row][col] = ""
                        if score < best_score:
                            best_score = score
                            best_move = (row, col)
            return best_score, best_move

    def get_winner(self, board):
        # Verifica todas as linhas
        for row in board:
            if row[0] == row[1] == row[2] != "":
                return row[0]
        # Verifica todas as colunas
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                return board[0][col]
        # Verifica diagonal principal
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        # Verifica diagonal secundária
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]
        # Se ninguém ganhou
        return None

    def is_board_full(self, board):
        # Verifica se o tabuleiro está cheio
        return all(board[row][col] != "" for row in range(3) for col in range(3))

    def check_winner(self, player):
        # Confirma se o jogador atual venceu
        return self.get_winner(self.board) == player

    def check_tie(self):
        # Verifica se houve empate
        return self.is_board_full(self.board) and self.get_winner(self.board) is None

    def handle_game_end(self, message):
        # Exibe o resultado do jogo e pergunta se o jogador quer jogar de novo
        self.update_score_label()
        if messagebox.askyesno("Fim de Jogo", f"{message}\n\nJogar novamente?"):
            self.start_game(self.mode, self.difficulty)
        else:
            self.create_mode_selection()

# Código principal: inicia o jogo
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
