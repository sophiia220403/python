class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'

    def play(self):
        while not self.game_over():
            self.print_board()
            row, col = self.get_move()
            self.board[row][col] = self.player
            self.player = 'O' if self.player == 'X' else 'X'
        self.print_board()
        if self.winner() is None:
            print("It's a tie!")
        else:
            print(f'{self.winner()} wins!')

    def get_move(self):
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if row in range(3) and col in range(3) and self.board[row][col] == ' ':
                    return row, col
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Invalid input, try again.")

    def game_over(self):
        return self.winner() is not None or all(
            [all(cell != ' ' for cell in row) for row in self.board]
        )

    def winner(self):
        for player in ('X', 'O'):
            for row in self.board:
                if row == [player] * 3:
                    return player
            for col in range(3):
                if all(row[col] == player for row in self.board):
                    return player
            if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
                return player
            if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
                return player
        return None

    def print_board(self):
        for row in self.board:
            print('|'.join(row))


game = TicTacToe()
game.play()
