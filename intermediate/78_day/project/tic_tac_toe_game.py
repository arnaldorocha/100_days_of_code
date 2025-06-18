import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe 🎮")
        self.mode = None
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.scores = {"X": 0, "O": 0, "IA": 0, "Empates": 0}

        self.create_mode_selection()

    def create_mode_selection(self):
        """Tela de seleção de modo de jogo"""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Escolha o modo de jogo:", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Single Player (vs IA)", font=("Arial", 12), command=lambda: self.start_game("1")).pack(pady=5)
        tk.Button(self.root, text="Two Players", font=("Arial", 12), command=lambda: self.start_game("2")).pack(pady=5)

    def start_game(self, mode):
        self.mode = mode
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_game_board()

    def create_game_board(self):
        """Cria o tabuleiro visual"""
        for widget in self.root.winfo_children():
            widget.destroy()

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                command=lambda r=row, c=col: self.player_move(r, c))
                btn.grid(row=row, column=col)
                button_row.append(btn)
            self.buttons.append(button_row)

        self.status_label = tk.Label(self.root, text=f"Vez do jogador {self.current_player}", font=("Arial", 12))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        self.update_score_label()

    def update_score_label(self):
        score_text = f"Placar - X: {self.scores['X']} | O: {self.scores['O']} | IA: {self.scores['IA']} | Empates: {self.scores['Empates']}"
        self.score_label = tk.Label(self.root, text=score_text, font=("Arial", 10))
        self.score_label.grid(row=4, column=0, columnspan=3)

    def player_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(self.current_player):
                self.end_game(f"Jogador {self.current_player} venceu!")
                if self.mode == "1" and self.current_player == "O":
                    self.scores["IA"] += 1
                else:
                    self.scores[self.current_player] += 1
                return

            if self.check_tie():
                self.scores["Empates"] += 1
                self.end_game("Empate!")
                return

            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"Vez do jogador {self.current_player}")

            # Se for modo IA e for a vez da IA
            if self.mode == "1" and self.current_player == "O":
                self.root.after(500, self.ai_move)  # Pequeno delay para parecer mais natural

    def ai_move(self):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
        row, col = random.choice(empty_cells)
        self.player_move(row, col)

    def check_winner(self, player):
        # Checa linhas
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Checa colunas
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Checa diagonais
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_tie(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def end_game(self, message):
        self.update_score_label()
        if messagebox.askyesno("Fim de Jogo", f"{message}\n\nJogar novamente?"):
            self.start_game(self.mode)
        else:
            self.create_mode_selection()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
