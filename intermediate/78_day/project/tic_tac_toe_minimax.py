import tkinter as tk
from tkinter import messagebox
import random
import copy

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe (IA MiniMax) 🎮")
        self.mode = None
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.scores = {"X": 0, "O": 0, "IA": 0, "Empates": 0}

        self.create_mode_selection()

    def create_mode_selection(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Escolha o modo de jogo:", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Single Player (vs IA MiniMax)", font=("Arial", 12),
                  command=lambda: self.start_game("1")).pack(pady=5)
        tk.Button(self.root, text="Two Players", font=("Arial", 12),
                  command=lambda: self.start_game("2")).pack(pady=5)

    def start_game(self, mode):
        self.mode = mode
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_game_board()

    def create_game_board(self):
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
                self.handle_game_end(f"Jogador {self.current_player} venceu!")
                if self.mode == "1" and self.current_player == "O":
                    self.scores["IA"] += 1
                else:
                    self.scores[self.current_player] += 1
                return

            if self.check_tie():
                self.scores["Empates"] += 1
                self.handle_game_end("Empate!")
                return

            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"Vez do jogador {self.current_player}")

            if self.mode == "1" and self.current_player == "O":
                self.root.after(500, self.ai_move)

    def ai_move(self):
        _, move = self.minimax(self.board, True)
        if move:
            row, col = move
            self.player_move(row, col)

    def minimax(self, board, is_maximizing):
        winner = self.get_winner(board)
        if winner == "O":
            return 1, None
        elif winner == "X":
            return -1, None
        elif self.is_board_full(board):
            return 0, None

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
        for row in board:
            if row[0] == row[1] == row[2] != "":
                return row[0]
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]
        return None

    def is_board_full(self, board):
        return all(board[row][col] != "" for row in range(3) for col in range(3))

    def check_winner(self, player):
        return self.get_winner(self.board) == player

    def check_tie(self):
        return self.is_board_full(self.board) and self.get_winner(self.board) is None

    def handle_game_end(self, message):
        self.update_score_label()
        if messagebox.askyesno("Fim de Jogo", f"{message}\n\nJogar novamente?"):
            self.start_game(self.mode)
        else:
            self.create_mode_selection()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
